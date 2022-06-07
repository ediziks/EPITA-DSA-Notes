from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# read the df from csv from github
# and drop the unnecessary columns
df = pd.read_csv('https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv')
df = df.drop('Type 2', axis=1) # due to having many null values

# generate df sample
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# figures to be plotted
fig = px.bar(df, x="Type 1", y="Total", barmode="group", color="Generation")
fig2 = px.scatter(df, x="Name", y="Total", size="HP", color="Type 1")

# HTML Layout
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Pokemon Dashboard'),

        html.H2(children='''
            Dash: Graphs and Tables for Pokemon Data
        '''),

        html.Table([
            html.H4(children='df Sample'),
            generate_table(df)
        ])
    ]),
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ]),
    html.Div([
        dcc.Graph(
            id='example-graph-2',
            figure=fig2
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)