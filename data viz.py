import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache
def load_data():
    return pd.read_csv("Netflix TV Shows and Movies.csv")

df = load_data()

# Main title
st.title("Netflix TV Shows and Movies Analysis Dashboard")

# Perform data analysis and visualization
df2 = df.tail(5)
fig = px.bar(df2, x='title', y='imdb_score', title='Movies and their IMDb ratings')

# Display visualization
st.plotly_chart(fig)
