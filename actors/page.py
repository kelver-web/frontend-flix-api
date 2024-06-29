from datetime import datetime
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import time
from actors.service import ActorService





def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores:')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Ator/Atriz não encontrado na base de dados')

    st.title("Cadastrar novo :blue[Ator/Atriz]")
    name = st.text_input("Nome do Ator/Atriz", placeholder='Nome do ator/atriz')
    birthday = st.date_input(
        "Data de Nascimento",
        value=None,
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ["BRA", "USA"]
    nationality = st.selectbox(
        "Nacionalidade",
        options=nationality_dropdown,
    )

    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )

        if new_actor:
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
