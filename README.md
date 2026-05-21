# 🎬 Movie Recommender System

A content-based movie recommendation system built using the TMDB 5000 dataset. Select any movie and instantly get **5 similar recommendations** with live posters fetched from the TMDB API.

---

## 🖥️ Demo

![App Screenshot](screenshot.png)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | CountVectorizer + Cosine Similarity |
| Streamlit | Web app deployment |
| TMDB API | Live movie poster fetching |
| Pickle | Model serialization |

---

## 📂 Project Structure

```
movies-recommender-system/
├── app.py                  # Streamlit web app
├── model_generation.py     # Script to generate model files
├── requirements.txt        # Python dependencies
├── model/
│   ├── movie_list.pkl      # Processed movie dataframe
│   └── similarity.pkl      # Cosine similarity matrix
├── tmdb_5000_movies.csv    # Raw dataset (movies)
├── tmdb_5000_credits.csv   # Raw dataset (credits)
└── README.md
```

---

## ⚙️ How It Works

1. Merges the movies and credits datasets on movie title
2. Extracts **genres**, **keywords**, **top 3 cast members**, and **director** from raw JSON columns
3. Combines all features into a single `tags` column per movie
4. Applies **CountVectorizer** (5000 features, stop words removed) to convert tags into vectors
5. Computes a **Cosine Similarity matrix** across all 4800+ movies
6. On user selection, finds the top 5 most similar movies and fetches their posters live via the **TMDB API**

---

## 🚀 How To Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/movies-recommender-system.git
cd movies-recommender-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Download the **TMDB 5000 Movie Dataset** from Kaggle and place both CSV files in the project root folder:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

🔗 [Kaggle Dataset Link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### 4. Generate model files
```bash
python model_generation.py
```
This creates `model/movie_list.pkl` and `model/similarity.pkl`.

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📊 Dataset

- **Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) on Kaggle
- Contains 5000 movies with metadata including genres, keywords, cast, crew, and overview
- Two files merged on movie title: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`

---

## 🔮 Future Improvements

- Add collaborative filtering for user-based recommendations
- Include movie ratings and popularity score in ranking
- Deploy on Streamlit Cloud for public access
- Add movie details page on poster click
- Implement search autocomplete

---

## 📬 Contact

**Prem C**
- LinkedIn: [your-linkedin-url]
- GitHub: [your-github-url]
- Email: [your-email]
