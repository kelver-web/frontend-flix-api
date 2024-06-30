import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, ExcelExportMode
from genres.service import GenreService
import time


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros:')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='genres_grid',
        )

    else:
        st.warning('Gênero não encontrados na base de dados')

    st.title("Cadastrar novo :blue[Gênero]")
    name = st.text_input("Nome do Gênero")

    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(
            name=name,
        )

        if new_genre:
            st.toast(f'Gênero {name} cadastrado con sucesso!', icon="✅")
            st.markdown("""
                <style>
                        div[data-testid=stToast] {
                            padding: 15px 25px 15px 10px;
                            width: 20%;
                            background-color: green;
                            color: #ffffff;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                        }
                </style>
                """,
                unsafe_allow_html=True
            )

            time.sleep(2)
            st.rerun()

        else:
            st.toast(f':black[Opa, verifique os campos!]', icon="⚠️")
            st.markdown("""
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
