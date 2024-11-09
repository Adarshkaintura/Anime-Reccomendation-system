# Anime Recommendation System
## Deployment

You can view and interact with the deployed project by clicking the link below:

[View Deployed Project](https://anime-reccomendation-system-vfnfx7cawrsgdsiuoebrg5.streamlit.app/)
This is a simple Anime Recommendation System built using Streamlit. The system allows users to input the name of an anime they like and the number of recommendations they want. Based on the input, the system will suggest similar anime based on genre similarity.

## Features:
- **User Input**: The user types the name of an anime and the number of recommendations they want.
- **Recommendation**: The system will recommend anime based on the genre similarity using **Euclidean distance**.
- **Output**: Displays the recommended anime list.

## ML Algorithm Used:
The system uses **Euclidean distance** to measure the similarity between the input anime's genre and others in the dataset. While no explicit machine learning algorithm like K-Means clustering is used in this version, the system still makes recommendations based on genre features.

## How It Works:
1. **User Input**: The user inputs an anime name and the number of recommendations they want.
2. **Similarity Calculation**: The system calculates the **Euclidean distance** between the genre features of the given anime and other anime in the dataset.
3. **Recommendation**: The system recommends anime with the smallest Euclidean distance (most similar).

## Technologies Used:
- **Streamlit**: For building the interactive web app.
- **Pandas**: For data manipulation and handling the dataset.
- **NumPy**: For handling numerical operations.
- **SciPy**: For calculating Euclidean distance between anime genre features.

## How to Run:
1. Clone the repository or download the code.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
