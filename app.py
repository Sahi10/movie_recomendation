import pickle

import streamlit as st
import pandas as pd
import numpy as np


st.header("Movie Recommendation System")
movie_df = pd.read_csv('movie_list.csv')
movie_name = st.selectbox("Enter a Movie",movie_df['title'])
similarity = pickle.load(open('similarity.pkl','rb'))
# recommend_b= st.button("Recommend Movie")
def recommend(movie_name):
    movie_index = movie_df[movie_df['title']==movie_name].index[0]
    distance_movies = similarity[movie_index]
    movie_name_sort = sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:21]
    final_movie_name = []
    for i in range(len(movie_name_sort)):
        final_index = movie_name_sort[i][0]
        movie_names = movie_df.iloc[final_index]['title']
        final_movie_name.append(movie_names)
    return final_movie_name

if st.button("Recommend Movie"):

    st.write(recommend(movie_name))