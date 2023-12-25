import streamlit as st
import pickle

# Load movie data and similarity matrix from pickled files
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Set up Streamlit app header
st.header("Movie Recommender System")

# Create a dropdown for selecting a movie
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

# Define a function to recommend movies based on similarity
def recommend(movie):
    # Find the index of the selected movie in the dataset
    index = movies[movies['title'] == movie].index[0]
    
    # Sort movies based on similarity and get the top 5 recommendations
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = [movies.iloc[i[0]].title for i in distance[1:6]]
    
    return recommend_movie

# Display recommendations when the "Show Recommend" button is clicked
if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    
    # Display recommended movies in a 5-column layout
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        
    with col2:
        st.text(movie_name[1])
        
    with col3:
        st.text(movie_name[2])
        
    with col4:
        st.text(movie_name[3])
        
    with col5:
        st.text(movie_name[4])
