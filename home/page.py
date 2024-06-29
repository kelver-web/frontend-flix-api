import streamlit as st
import plotly.express as px
from movies.service import MovieService
from annotated_text import annotated_text




def show_home():
    movie_service = MovieService()
    movies_stats = movie_service.get_movies_stats()

    st.title('Estatísticas de Filmes')
    st.write('Bem-vindo à nossa plataforma de gerenciamento de filmes!')
    st.write('Aqui você pode adicionar, editar, excluir e visualizar filmes, atores, gêneros e críticas.')

    st.subheader('Total de Filmes Cadastrados')
    annotated_text(
        ("Total", f"{movies_stats['total_movies']}"), 
    )

    st.subheader('Total de Avaliações Cadastradas')
    annotated_text(
        ("Total", f":green[{movies_stats['total_reveiws']}]"), 
    )

    st.subheader('Média Geral de Estrelas nas Avalições')
    annotated_text(
        ("Total", f":green[{movies_stats['average_stars']}]"), 
    )


   