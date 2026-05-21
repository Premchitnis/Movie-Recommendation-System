"""
app.py  –  Movie Recommender System (Streamlit)

Run:  streamlit run app.py
Requires: model/movie_list.pkl and model/similarity.pkl
          (generate them first with model_generation.py)
"""

import os
import pickle
import requests
import streamlit as st

# ─── Config ───────────────────────────────────────────────────────────────────

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR  = os.path.join(BASE_DIR, 'model')
API_KEY    = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_URL   = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
POSTER_URL = "https://image.tmdb.org/t/p/w500{}"
FALLBACK   = "https://via.placeholder.com/500x750?text=No+Poster"

# ─── Helpers ──────────────────────────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def load_models():
    """Load pickled model files (cached after first load)."""
    movies     = pickle.load(open(os.path.join(MODEL_DIR, 'movie_list.pkl'), 'rb'))
    similarity = pickle.load(open(os.path.join(MODEL_DIR, 'similarity.pkl'), 'rb'))
    return movies, similarity


def fetch_poster(movie_id: int) -> str:
    """Fetch poster URL from TMDB API. Returns fallback image on failure."""
    try:
        response = requests.get(TMDB_URL.format(movie_id, API_KEY), timeout=5)
        response.raise_for_status()
        data = response.json()
        path = data.get('poster_path')
        return POSTER_URL.format(path) if path else FALLBACK
    except Exception:
        return FALLBACK


def recommend(movie: str, movies, similarity):
    """Return top-5 recommended movie names and poster URLs."""
    index     = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# ─── Page Setup ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommender System")
st.markdown("Select a movie you like, and we'll recommend 5 similar ones!")

# ─── Load Models ──────────────────────────────────────────────────────────────

try:
    movies, similarity = load_models()
except FileNotFoundError:
    st.error(
        "⚠️ Model files not found!\n\n"
        "Run `python model_generation.py` first to generate:\n"
        "- `model/movie_list.pkl`\n"
        "- `model/similarity.pkl`"
    )
    st.stop()

# ─── UI ───────────────────────────────────────────────────────────────────────

movie_list     = movies['title'].values
selected_movie = st.selectbox("Type or select a movie:", movie_list)

if st.button("🔍 Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie, movies, similarity)

    st.subheader("Top 5 Recommendations")
    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, width=300)
            st.caption(name)