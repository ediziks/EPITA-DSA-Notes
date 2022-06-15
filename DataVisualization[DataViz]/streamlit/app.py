import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Read the df from csv from Github and drop the unnecessary columns
df = pd.read_csv('https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv')
df = df.drop('Type 2', axis=1) # due to having many null values

# Figures to be plotted
fig = px.bar(df, x="Type 1", y="Total", barmode="group", color="Generation")
fig2 = px.scatter(df, x="Name", y="Total", size="HP", color="Type 1")
fig3 = px.pie(df, values="Total", names="Type 1", labels={'Type 1':'Type 1'})
fig3.update_traces(textposition='inside', textinfo='percent+label')

# HTML Layout for the plots
st.title('Pokemon Spec Plots')
st.subheader('Sample data to observe the columns')
st.dataframe(df.sample(10))
st.subheader('Plot 1: The total specs of Pokemons by their types and colorized by the generation of the each Pokemon')
st.plotly_chart(fig)
st.subheader('Plot 2: Each Pokemons\' Total Specs (sum of all different skill points such as Power, HP, Attack), scatters are sized by the amount of their power, and colorized by their types')
st.plotly_chart(fig2)
st.subheader('Plot 3: Total Skill Points Distrubition by Each Type of Pokemon')
st.plotly_chart(fig3)

st.subheader('Select a Pokemon to see its Specs')
poke = st.selectbox(' ', df['Name'].unique())
fig4 = px.bar_polar(df[df['Name'] == poke], r='Attack', theta='Type 1', color='Total', color_discrete_sequence=px.colors.sequential.Plasma_r, template="plotly_dark")
st.plotly_chart(fig4)
