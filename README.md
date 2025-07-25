# Movie Recommendation System

This is a content-based movie recommendation system built with Python and Streamlit.

> **Live App**: (https://movie-recommender-b7adrvyq6x85bc3voxu6ac.streamlit.app)

## Features
- Recommends similar movies based on plot descriptions
- Uses TF-IDF and cosine similarity for text analysis
- Fetches real-time movie data from TMDB API
- Displays poster, title, and overview in a clean Streamlit interface
- User-friendly with visible movie list and smart error handling

## Tech Stack
- Python
- Pandas
- scikit-learn
- Streamlit
- TMDB API

## How It Works
1. Pulls movie data (title, overview, poster) from TMDB
2. Cleans and vectorizes overviews using TF-IDF
3. Computes similarity between movies
4. Suggests top 5 similar movies when a user enters a film name

## Installation (for local use)
```bash
git clone https://github.com/Mustafa-Temizel/movie-recommender
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
