from typing import List, Set

import pandas as pd
from .utils import parse
import streamlit as st

@st.cache_data  # cash for loading data
def _load_base(path: str, index_col: str = 'id') -> pd.DataFrame:
    """Load CSV file to pandas.DataFrame"""
    return pd.read_csv(path, index_col=index_col)

class ContentBaseRecSys:

    def __init__(self, movies_dataset_filepath: str, distance_filepath: str):
        self.distance = _load_base(distance_filepath, index_col='movie_id')
        self.distance.index = self.distance.index.astype(int)
        self.distance.columns = self.distance.columns.astype(int)
        self._init_movies(movies_dataset_filepath)

    def _init_movies(self, movies_dataset_filepath) -> None:
        self.movies = _load_base(movies_dataset_filepath, index_col='id')
        self.movies.index = self.movies.index.astype(int)
        self.movies['genres'] = self.movies['genres'].apply(parse)

    def get_title(self) -> List[str]:
        return self.movies['title'].values

    def get_genres(self) -> Set[str]:
        genres = [item for sublist in self.movies['genres'].values.tolist() for item in sublist]
        return set(genres)

    def get_actors(self) -> Set[str]:
        self.movies['cast'] = self.movies['cast'].apply(parse)
        actors = [item for sublist in self.movies['cast'].values.tolist() for item in sublist]
        return set(actors)


    def filter_movies(self,
                      genre: str | None = None,
                      actor: str | None = None) -> List[int]:
        if genre and actor:
            genre_index = set(self.movies[self.movies['genres'].apply(lambda x: genre in x)].index)
            actor_index = set(self.movies[self.movies['cast'].apply(lambda x: actor in x)].index)
            filtered_movies_index = list(genre_index.intersection(actor_index))
        elif genre:
            filtered_movies_index = list(self.movies[self.movies['genres'].apply(lambda x: genre in x)].index)
        return filtered_movies_index

    def recommendation(self, index: List[int], title: str, top_k: int = 5, ) -> pd.DataFrame:
        """
        Returns the names of the top_k most similar movies with the movie "title"
        """
        index_movie = self.movies[self.movies['title'] == title].index[0]  # find index of title
        sim_scores = self.distance[index_movie]  # find Series with distances to each movie
        sorted_sim_scores = sim_scores.sort_values(ascending=False)  # sort series on desc of distances
        # sorted_sim_scores = list(sorted_sim_scores.keys())  # list with indices of matching movies
        # top_k_indices = [item for item in sorted_sim_scores if item in index][:top_k]
        # movie_titles = self.movies[self.movies['movie_id'].isin(top_k_indices)]['title']
        top_movies = self.movies.loc[sorted_sim_scores.index.intersection(index)]
        if title in list(top_movies['title']):
            top_movies = top_movies[top_movies['title'] != title]
            top_k_movies = top_movies.head(top_k)
        else:
            top_k_movies = top_movies.head(top_k)

        return top_k_movies

        # top_k_indices = list(sorted_sim_scores[1:top_k+1].keys())  # list with indices of top_k movies
        # move_titles = self.movies[self.movies['movie_id'].isin(top_k_indices)]['title']
        # return list(move_titles.values)




