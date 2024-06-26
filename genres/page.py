import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import time


genres = [
    {
        "id": 1,
        "name": "Ação"
    },
    {
        "id": 2,
        "name": "Aventura"
    },
    {
        "id": 3,
        "name": "Comédia"
    },
    {
        "id": 4,
        "name": "Drama"
    },
]

def show_genres():
    st.write('Lista de Gêneros:')
    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )

    st.title("Cadastrar novo :blue[Gênero]")
    name = st.text_input("Nome do Gênero")
    if st.button("Cadastrar"):
        st.toast(f':black[Gênero "{name}" cadastrado com sucesso]', icon='🎉')
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
            """, unsafe_allow_html=True
        )

        time.sleep(.5)
