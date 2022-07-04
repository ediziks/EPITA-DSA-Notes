import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.write("# Our Final Project: Nike Factory Locations")   # this is markdown

# show all columns when printed
pd.set_option('display.max_columns', None)

# read dataframe from the excel file
df = pd.read_csv('NikeUpdatedCopy.csv')
df2 = pd.read_csv('AdidasVsNike.csv')

# geomap of factories
fig4 = go.Figure(data=go.Scattergeo(
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['City'],
        mode = 'markers'
        ))

fig4.update_layout(
        title = 'Nike Factory Locations all around the World',
        geo_scope='world',
    )

# pie chart for df
fig2 = px.pie(df, values='Total Workers', names='Country', title='Total Worker Distrubution by Country Presented in Pie Chart')
fig2.update_traces(textposition='inside', textinfo='percent')

# pie chart for df2
fig22 = px.pie(df2, values='New Brands', names='Brands', title='Distribution of nmbr of prodcts for each company')
fig22.update_traces(textposition='inside', textinfo='percent')

# bar chart2
fig23 = px.bar(df2, x="Brands", y="Discount", color="Discount",
      title="Discounts by brand in a Sliced Bar Chart"
)
# bar chart
fig1 = px.bar(df, x="Product Type", y="Country", color="Country",
      title="Product Type by Countries in a Sliced Bar Chart"
)

sunburst_df = df.fillna('...')

# sunburst chart to show total worker distrubition through continents and then countries
fig6 = px.sunburst(sunburst_df.loc[sunburst_df['Total Workers'] != 0], path=['Continent', 'Country'],
                  values='Total Workers', color='Total Workers', color_continuous_scale='Magma',
                  color_continuous_midpoint=np.average(df['Total Workers'], weights=df['Total Workers']),
                  title='total worker distrubition through continents and countries over sunburst chart'.title())


# # line plot - workers by continent
# fig7 = px.line(df.groupby('Continent').sum(), x=df.groupby('Continent').sum().index,
#         y=['Total Workers', 'Female Worker Count', 'Migrant Worker Count'],
#         title='Worker Counts per Each Continent on Multiple Line Plot')


# scatter
sub_df = df.groupby(['Continent', 'Product Type']).count()

fig8 = px.scatter(sub_df, x=sub_df.index.get_level_values(0), y=list(sub_df.index.get_level_values(1)), size='Factory Name', color='Factory Name',
        labels={
                     "x": "Continents",
                     "y": "Product Type"
                 },
        title='Factory Count Specified by Continents and Product Type in Scatter Chart', color_continuous_scale='Bluered'
)

# hist chart - continent/total workers | product type
fig9 = px.histogram(df, x="Continent", y="Total Workers", color='Product Type', marginal="rug",
                   hover_data=['Total Workers', 'Female Worker Count', 'Migrant Worker Count'],
                   title='Size of Workers distributed by product type in histogram chart'.title())
# hist chart2
fig24 = px.histogram(df2, x="Sale Price", y="Brands", color='Brands', marginal="rug",
                   hover_data=['Brands', 'Sale Price'],
                   title='Sales distrbution by Brands in histogram chart'.title())



# scatter geo
fig10 = px.scatter_geo(df, lat='Latitude', lon="Longitude", color="Continent",
                     hover_name="Country", size="Total Workers",
                     projection="natural earth",
                     title='Each Nike Factory Pointed Out by Size of Total Workers')

# violin chart
sub_df = df.groupby(['Continent', 'Product Type']).count()

fig11 = px.violin(sub_df, x=sub_df.index.get_level_values(0), y='Total Workers', color=sub_df.index.get_level_values(0), box=True, points="all",
          hover_data=['Factory Name', 'Factory Type'],
          title='Violin Graph of Factory Distribituons Around All Continents including Outliers'
)

# showing the tables:
# st.write("## Here's our 2 datasets table:")
# df
# df2

# showing figures:
fig4

fig1
st.write("#### we can see that Vietnam, China and the US are the main players in all the product types categories")

col1, col2, col3 = st.columns([5,3,3])

with col1:
        fig2
with col3:
        fig10

st.write("#### Asian and far eastern countries have the biggest workers proportion vs the other countries")


fig6

option = st.selectbox('Select Worker Type', ('Total Workers', 'Female Worker Count', 'Migrant Worker Count', ['Total Workers', 'Female Worker Count', 'Migrant Worker Count']))

# line plot - workers by continent
fig7 = px.line(df.groupby('Continent').sum(), x=df.groupby('Continent').sum().index,
        y=option,
        title='Worker Counts per Each Continent on Multiple Line Plot')

fig7

fig8

fig9
st.write("#### Footwear and Apparel are the most focused products in Asia")

fig11

fig22
st.write("##### Adidas roasts Nike in the number of products released")

fig23
st.write("##### Adidas roasts Nike in the number of discounts")

fig24
st.write("##### Adidas has approx twice Nike's profits")
