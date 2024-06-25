import streamlit as st


def main():
    st.title("Flix App")

    menu_options = st.sidebar.selectbox(
        "Selecione uma opção",
        ["Início", "Generos", "Atores/Atrizes", "Filmes", "Avaliações"]
    )

    if menu_options == "Início":
        st.write("Início")

    if menu_options == "Generos":
        st.write("Generos")
    
    if menu_options == "Atores/Atrizes":
        st.write("Atores/Atrizes")

    if menu_options == "Filmes":
        st.write("Filmes")
    
    if menu_options == "Avaliações":
        st.write("Avaliações")



if __name__ == "__main__":
    main()
