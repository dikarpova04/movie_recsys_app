import os

import streamlit as st
# from streamlit_extras.no_default_selectbox import selectbox
from dotenv import load_dotenv

from api.omdb import OMDBApi
from api.tmdb import TMDBApi
from recsys import ContentBaseRecSys

TOP_K = 5
# load_dotenv()
#
# API_KEY = os.getenv("API_KEY")
# API_KEY_TMDB = os.getenv("API_KEY_TMDB")
# MOVIES = os.getenv("MOVIES")
# DISTANCE = os.getenv("DISTANCE")

API_KEY = st.secrets['API_KEY']
API_KEY_TMDB = st.secrets['API_KEY_TMDB']
MOVIES = 'assets/movies.csv'
DISTANCE = 'assets/distance.csv'


omdbapi = OMDBApi(API_KEY)
tmdbapi = TMDBApi(API_KEY_TMDB)

st.set_page_config(
    page_title="Movie recommendation App",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': f"# This is a simple movie recommendation application for studying purposes."
    })

recsys = ContentBaseRecSys(
    movies_dataset_filepath=MOVIES,
    distance_filepath=DISTANCE,
)

# st.markdown(
#     "<h1 style='text-align: center; color: black;'>Movie Recommender Service</h1>",
#     unsafe_allow_html=True
# )

st.title("Welcome to movie recommendation app.")

st.sidebar.title("Choose the necessary parameters for personal recommendation.")
st.sidebar.image('images/movie_time.jpg', use_column_width=True)

selected_movie = st.sidebar.selectbox(
    "Type or select the movie you like :",
    recsys.get_title()
)

selected_genre = st.sidebar.selectbox(
    "Type or select the movie genre you like :",
    recsys.get_genres()
)

selected_actor = st.sidebar.selectbox(
    "Type or select the actor you like :",
    [None] + [i for i in recsys.get_actors()]
)

if st.sidebar.button('Show Recommendation'):
    st.subheader("What to watch:")
    filtered_movies = recsys.filter_movies(selected_genre, selected_actor)
    if len(filtered_movies) > 0:
        TOP_K = min(len(filtered_movies), 5)
        recommended_movie_names = list(recsys.recommendation(filtered_movies, selected_movie, top_k=TOP_K)['title'])
        recommended_movie_names_id = list(recsys.recommendation(filtered_movies, selected_movie, top_k=TOP_K).index)
        recommended_movie_posters = omdbapi.get_posters(recommended_movie_names)
        movies_col = st.columns(TOP_K)

        for index, col in enumerate(movies_col):
            video = tmdbapi.get_video_data(recommended_movie_names_id[index])

            with col:
                if recommended_movie_posters[index] != 'Poster not available':
                    st.image(recommended_movie_posters[index], use_column_width=True)
                else:
                    st.write("Poster not available.")
                # st.image(recommended_movie_posters[index])
                st.subheader(recommended_movie_names[index])
                if video:
                    video_url = f"https://www.youtube.com/watch?v={video[0]['key']}"
                    st.video(video_url)
                else:
                    st.write("Video not available.")
                st.write("------------------------------")
    else:
        st.subheader('There is no movies on these paramet