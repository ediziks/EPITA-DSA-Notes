import plotly.express as px
import streamlit as st
import pandas as pd

st.write("# Ma première appli")   # this is markdown

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

st.write("## Here's our first attempt at using data to create a table:")
df

st.write("## Here's our first attempt at showing a chart:")
fig
