import streamlit as st
from recommender import recommend
from tmdb_api import get_popular_movies

st.set_page_config(page_title="🎬 Film Tavsiye Sistemi")

st.title("🎬 Film Tavsiye Sistemi")
st.markdown("Sevdiğin bir filmi gir, sana benzer filmleri önerelim!")


movies = get_popular_movies()
movie_titles = [m["title"] for m in movies]


with st.expander("📃 Elimizdeki Filmler Listesi"):
    st.write(movie_titles)


user_input = st.text_input("Film ismi gir:", "")


if st.button("Tavsiye Ver"):
    if user_input.strip() == "":
        st.warning("Lütfen bir film ismi gir.")
    else:
        results = recommend(user_input)

        if isinstance(results, str):
            st.error(results)
        else:
            for _, row in results.iterrows():
                st.markdown(f"### 🎥 {row['title']}")
                st.image(row['poster_path'])
                st.write(row['overview'])
