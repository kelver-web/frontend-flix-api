import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import time



actors = [
    {
        "id": 1,
        "name": "Stallone",
        "Birthday": "29-05-1958",
        "Nationality": "USA",
    },
    {
        "id": 2,
        "name": "Chris Rock",
        "Birthday": "29-05-1980",
        "Nationality": "USA",
    },
    {
        "id": 3,
        "name": "Leonardo Di Caprio",
        "Birthday": "29-05-1978",
        "Nationality": "USA",
    },
    {
        "id": 4,
        "name": "Wagner Moura",
        "Birthday": "29-05-1975",
        "Nationality": "BRA",
    },
]

def show_actors():
    st.write('Lista de Atores:')
    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title("Cadastrar novo :blue[Ator/Atriz]")
    name = st.text_input("Nome do Ator/Atriz", placeholder='Nome do ator/atriz')
    birthday = st.date_input("Data de Nascimento", value=None)
    nationality = st.text_input("Nacionalidade", placeholder='Nacionalidade')

    if st.button("Cadastrar"):
        st.toast(f':black[Ator/Atriz "{name}" cadastrado com sucesso]', icon='🎉')
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
