import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, ExcelExportMode
import time
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações:')
        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='reviews_grid',
        )
    else:
        st.warning('Avaliações não encontradas na base de dados')

    st.title("Cadastrar nova :blue[Avaliação]")

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}

    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )
    comments = st.text_area(label='Comentário', max_chars=500)

    if st.button("Cadastrar"):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comments=comments,
        )

        if new_review:
            st.toast(f':black[Review cadastrado com sucesso]', icon='🎉')
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
