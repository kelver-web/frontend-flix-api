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

    if len(movies_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movies_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados')
    annotated_text(
        ("Total", f"{movies_stats['total_movies']}"), 
    )

    st.subheader('Quantidade de Filmes por Gênero')
    for genre in movies_stats['movies_by_genre']:
        st.write(
            f"{genre['genre__name']}: -- :red[{genre['count']}]"
        )

    st.subheader('Total de Avaliações Cadastradas')
    annotated_text(
        ("Total", f":green[{movies_stats['total_reveiws']}]"), 
    )

    st.subheader('Média Geral de Estrelas nas Avalições')
    annotated_text(
        ("Total", f":blue[{movies_stats['average_stars']}]"), 
    )


   