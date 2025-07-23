import requests

API_KEY = "607faf467cbfdcd7fa627b1787ec0f14"
BASE_URL= "https://api.themoviedb.org/3"

def get_popular_movies(pages=5):
    all_movies = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}/movie/popular"
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "page": page
        }
        response = requests.get(url, params=params)
        data = response.json()
        results = data.get("results", [])
        
        for movie in results:
            all_movies.append({
                "title": movie.get("title"),
                "overview": movie.get("overview"),
                "poster_path": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}"
            })

    return all_movies

