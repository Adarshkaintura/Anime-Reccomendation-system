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

# Input for anime user likes and number of recommendations
user_input = st.text_input('Enter the anime you like, and we will find more like those for you:')
num_recommendations = st.number_input('Please enter the number of recommendations you want:', min_value=1, max_value=10, value=5)

# Convert user input to lowercase for comparison
user_input = user_input.lower()

# Find the anime in the dataset
name = data['name'].values
h = -1
for i in range(len(name)):
    if user_input in name[i].lower():
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
