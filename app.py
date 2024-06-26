import streamlit as st

from actors.page import show_actors
from genres.page import show_genres
from movies.page import show_movies


def main():
    st.title("Flix App")

    menu_options = st.sidebar.selectbox(
        "Selecione uma opção",
        ["Início", "Generos", "Atores/Atrizes", "Filmes", "Avaliações"]
    )

    if menu_options == "Início":
        st.write("Início")

    if menu_options == "Generos":
        show_genres()
    
    if menu_options == "Atores/Atrizes":
        show_actors()

    if menu_options == "Filmes":
        show_movies()
    
    if menu_options == "Avaliações":
        st.write("Avaliações")



if __name__ == "__main__":
    main()
