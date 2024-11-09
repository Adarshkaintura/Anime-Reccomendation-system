import numpy as np
import pandas as pd
import streamlit as st
from scipy.spatial import distance

# Load your dataset
data = pd.read_csv('anime.csv')
data = data[data['genre'] != 'Hentai']  # Filter out unwanted genres

# Prepare the genre list and convert it to a feature matrix
genre = data['genre'].values
lis = []
for i in genre:
    i = str(i)
    for p in i.split(','):
        if p not in lis:
            lis.append(p)

dic = {}
t = []
for i in genre:
    for j in lis:
        dic[j] = 0
    i = str(i)
    for p in i.split(','):
        dic[p] += 1
    t.append(list(dic.values()))

X = np.array(t)

# Streamlit UI
st.title("Anime Recommendation System")

# Auto-suggestion for anime name
anime_names = data['name'].values
suggestions = []

# Text input with auto-suggestions
user_input = st.text_input('Enter the anime you like, and we will find more like those for you:', '')

# Generate suggestions based on the user input
if user_input:
    suggestions = [anime for anime in anime_names if user_input.lower() in anime.lower()]

# Display suggestions live below the text input
if suggestions:
    st.write("Suggestions:")
    for suggestion in suggestions:
        st.write(suggestion)

# Input for number of recommendations
num_recommendations = st.number_input('Please enter the number of recommendations you want:', min_value=1, max_value=10, value=5)

# Check if the user selected a valid anime from suggestions
selected_anime = ''
if user_input and suggestions:
    selected_anime = suggestions[0].lower()  # Just select the first suggestion for simplicity

# Find the anime in the dataset
name = data['name'].values
h = -1
for i in range(len(name)):
    if selected_anime in name[i].lower():
        h = i
        break

imp = []
if h == -1:
    st.write('Sorry, no match found :(')
else:
    for i in range(len(t)):
        if i == h:
            continue
        else:
            if len(imp) < num_recommendations:
                imp.append([distance.euclidean(t[i], t[h]), t[i], i])
            else:
                imp.sort()
                if imp[num_recommendations - 1][0] > distance.euclidean(t[i], t[h]):
                    del imp[num_recommendations - 1]
                    imp.append([distance.euclidean(t[i], t[h]), t[i], i])

    # Display the recommendations
    st.write('The anime recommended for you are:')
    count = 0
    for i in imp:
        count += 1
        recommended_anime = name[i[2]]
        st.write(f"Recommendation {count}: {recommended_anime}")
