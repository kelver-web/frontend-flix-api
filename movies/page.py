import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import time


movies = [
    {
        "id": 1,
        "name": "De volta para o futuro",
        
    },
    {
        "id": 2,
        "name": "Os 8 odiados",
       
    },
    {
        "id": 3,
        "name": "O resgate",
       
    },
    {
        "id": 4,
        "name": "A fronteira",
    
    },
]

def show_movies():
    st.write('Lista de Filmes:')
    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )

    st.title("Cadastrar novo :blue[Filme]")
    name = st.text_input("Nome do Filme", placeholder='Nome do Filme')
    genre_id = st.selectbox("Gênero", [1, 2, 3, 4])

    if st.button("Cadastrar"):
        st.toast(f':black[Filme "{name}" cadastrado com sucesso]', icon='🎉')
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
