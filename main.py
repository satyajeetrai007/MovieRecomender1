import pandas as pd
import streamlit as st
import pickle

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie_name):
    #colab waala hin fn hai

    movie_index = movies_dataframe[movies_dataframe['title'] == movie_name].index[0]
    # new_df[title] = movie will generate column matrix with 1 only at position
    #  where movie title matches and upon using  new_df[new_df['title']== movie] i can acess the location and taking the 0th index will give
    # the row no. i.e. the INDEX
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    movie_list = []
    for i in movies_list:
        movie_list.append(movies_dataframe.iloc[i[0]].title)
    return movie_list

st.title(':red[Movie Recommender]')
# importing my movie list using pickle
movies_dict = pickle.load(open('movies.pkl','rb'))
movies_dataframe = pd.DataFrame(movies_dict)


option = st.selectbox(
    'Select a Movie',
    (movies_dataframe['title'].values))

st.write('You selected:', option)
# writing a function which recommends movies on selecting any movie



# creating button 'Recommend', if pressed will recommend movie name

if st.button("Recommend", type="primary"):
    recommended = recommend(option)
    for i in recommended:
        st.write(i)