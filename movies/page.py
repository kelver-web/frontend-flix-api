from datetime import datetime
import pandas as pd
import streamlit as st
from genres.service import GenreService
from actors.service import ActorService
from movies.service import MovieService
from st_aggrid import AgGrid, ExcelExportMode
import time


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        st.write('Lista de Filmes:')
        AgGrid(
            data=movies_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='movies_grid',
        )
    else:
        st.warning('Filme não encontrado na base de dados')

    st.title("Cadastrar novo :blue[Filme]")

    title = st.text_input("Título", placeholder='Título do Filme')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )


    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area("Sinopse", placeholder='Escreva a sinopse do filme aqui...')


    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )

        if new_movie:
            st.toast(f':black[Filme "{time}" cadastrado com sucesso]', icon='🎉')
            st.markdown(
                """
                    <style>
                            div[data-testid=stToast] {
                                padding: 15px 25px 15px 10px;
                                width: 20%;
                                background-color: #3CB371;
                                color: #ffffff;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                            }
                    </style>
                """,
                unsafe_allow_html=True
            )

            time.sleep(.5)
            st.rerun()
        else:
            st.toast(f':black[Opa, verifique os campos!]', icon="⚠️")
            st.markdown(
                """
                    <style>
                            div[data-testid=stToast] {
                                padding: 15px 25px 15px 10px;
                                width: 20%;
                                background-color: #FF6347;
                                color: #000000;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                            }
                    </style>
                """,
                unsafe_allow_html=True
            )

            time.sleep(.5)
