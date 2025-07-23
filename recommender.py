import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tmdb_api import get_popular_movies


movies = get_popular_movies(pages=5)


df = pd.DataFrame(movies)

df = df.dropna(subset=["overview"])

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])

similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend(title, top_n=5):
    if title not in df["title"].values:
        return f"'{title}' adlı film bulunamadı."

    idx = df[df["title"] == title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]  # ilk film kendisi, onu atla

    recommendations = df.iloc[[i[0] for i in sim_scores]]
    return recommendations[["title", "overview", "poster_path"]]

print(df)
