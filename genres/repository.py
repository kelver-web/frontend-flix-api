import requests
import streamlit as st

from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = 'https://kelver.pythonanywhere.com/api/v1/'
        self.__genre_url = f'{self.__base_url}genres/'
        self.__header = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json',
        }

    def get_genres(self):
        response = requests.get(
            self.__genre_url,
            headers=self.__header,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
    
    def create_genre(self, genre):
        response = requests.post(
            self.__genre_url,
            headers=self.__header,
            json=genre,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao cadastrar gênero na API. Status Code: {response.status_code}')