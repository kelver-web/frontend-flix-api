import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import time


reviews = [
    {
        "id": 1,
        "stars": 3,
        
    },
    {
        "id": 2,
        "stars": 5,
       
    },
    {
        "id": 3,
        "stars": 5,
       
    },
    {
        "id": 4,
        "stars": 4,
    
    },
]

def show_reviews():
    st.write('Lista de Avaliações:')
    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )

    st.title("Cadastrar nova :blue[Avaliação]")
    stars = st.selectbox("Avaliação", [1, 2, 3, 4, 5])

    if st.button("Cadastrar"):
        st.toast(f':black[Avaliação cadastrada com sucesso]', icon='🎉')
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
