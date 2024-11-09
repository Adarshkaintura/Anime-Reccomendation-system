import streamlit as st
import numpy as np
import pandas as pd
from scipy.spatial import distance
import pyttsx3
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('anime.csv')

# Clean the data by removing 'Hentai' genre
data = data[data['genre'] != 'Hentai']

# Generate genre list
genre = data['genre'].values
lis = []
for i in genre:
    i = str(i)
    for p in i.split(','):
        if p not in lis:
            lis.append(p)

# Initialize dictionary for genre count
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

# Streamlit interface
st.title("Anime Recommendation System")

# User input for anime preference and number of recommendations
s = st.text_input('Enter the anime you like:')
num = st.number_input('Please enter the number of recommendations you want:', min_value=1, max_value=10, value=5)

# Text-to-Speech initialization
engine = pyttsx3.init()

# Recommendations logic
if s:
    s = s.lower()
    name = data['name'].values
    h = -1
    for i in range(len(name)):
        name[i] = name[i].lower()
        if s in name[i]:
            h = i
            break

    imp = []
    if h == -1:
        st.write('Sorry, no match found :(')
        engine.say("Sorry, no match found")
        engine.runAndWait()
    else:
        for i in range(len(t)):
            if i == h:
                continue
            else:
                if len(imp) < num:
                    imp.append([distance.euclidean(t[i], t[h]), t[i], i])
                else:
                    imp.sort()
                    if imp[num - 1][0] > distance.euclidean(t[i], t[h]):
                        del imp[num - 1]
                        imp.append([distance.euclidean(t[i], t[h]), t[i], i])

        st.write('The anime recommended for you are:')
        count = 0
        for i in imp:
            count += 1
            recommended_anime = name[i[2]]
            st.write(f"{count}. {recommended_anime}")

            # Text-to-Speech for the recommendations
            engine.say(f"Recommendation {count}: {recommended_anime}")
            engine.runAndWait()

