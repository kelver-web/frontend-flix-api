import streamlit as st
from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        new_movie = self.movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movies_stats(self):
        return self.movie_repository.get_movies_stats()
