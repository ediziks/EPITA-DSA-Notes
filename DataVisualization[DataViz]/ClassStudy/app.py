from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# initialize Dash app
app = Dash(__name__)

# Read the df from csv from Github and drop the unnecessary columns
df = pd.read_csv('https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv')
df = df.drop('Type 2', axis=1) # due to having many null values

# Figures to be plotted
fig = px.bar(df, x="Type 1", y="Total", barmode="group", color="Generation")
fig2 = px.scatter(df, x="Name", y="Total", size="HP", color="Type 1")

# HTML Layout for the plots
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Pokemon Spec Plots'),
        html.P(children='Prepared by @zx for Data Visualization class'),
    ]),
    html.Div([
        html.H3(children='''
            Plot 1: The total specs of Pokemons by their types and 
            colorized by the generation of the each Pokemon
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ]),
    html.Div([
        html.H3(children='''
            Plot 2: Each Pokemons' total specs (sum of all different skill points such as Power, HP, 
            Attack), scatters are sized by the amount of their power, and colorized by their types
        '''),
        dcc.Graph(
            id='example-graph-2',
            figure=fig2
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
