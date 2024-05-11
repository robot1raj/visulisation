import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title='Data Visualization')

st.markdown(
    """
    <h1 style='text-align: center; padding: 20px; background: linear-gradient(to right, #FFD700, #FF8C00, #FF4500); color: black; font-family: Arial, sans-serif; font-size: 36px; font-weight: bold; border-radius: 10px;'>SELECTED TOPICS IN INFORMATION PROCESSING - II </h1>
    """,
    unsafe_allow_html=True
)
st.header("IPL Dataset", divider='rainbow')
df = pd.read_csv('datasets/data.csv')
st.write(df)

st.title("STEPS")
st.write("""Import libraries""")
st.write('EDA(exploratory data analysis)')
st.write('DATA cleaning ')
st.write('Generate Visualizations')


st.header("Pie chart showing highest scoring teams from 2008 to 2022", divider='rainbow')
st.image('datasets/img.png', width=700)

st.header("Bar chart showing highest scoring batsman till 2022", divider='rainbow')
st.image('datasets/a7.jpeg', width=700)

st.header("Bar graph showing best fielders in IPL till 2022", divider='rainbow')
st.image('datasets/a6.jpeg', width=700)

st.header("Bar chart showing highest wicket taking bowlers", divider='rainbow')
st.image('datasets/a10.jpeg', width=700)

st.header("This shows the Sankey Diagram of runs flow between teams ", divider='rainbow')
st.image('datasets/a8.jpeg', width=700)

st.header("Bar chart showing distribution of wickets", divider='rainbow')
st.image('datasets/a9.jpeg', width=700)

st.header("Distribution of Wicket", divider='rainbow')
st.image('datasets/a1.jpeg', width=700)

st.header("Feature Importance", divider='rainbow')
st.image('datasets/a2.jpeg', width=700)

st.header("Statistical Analysis", divider='rainbow')
st.image('datasets/a4.jpeg', width=700)

st.header("Toss Impact on match", divider='rainbow')
st.image('datasets/p.png', width=700)

st.header("Random Forest based prediction for a best team", divider='rainbow')
st.image('datasets/a15.png', width=700)

