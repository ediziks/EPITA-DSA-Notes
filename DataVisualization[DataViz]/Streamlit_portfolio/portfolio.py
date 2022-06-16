import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

import yfinance as yf
import datetime as dt

st.write("# Fake crypto portfolio")
st.write("Computed from local *portfolio.xlsx* file")

df = pd.read_excel("portfolio.xlsx", None); # reads all sheets
xls = pd.ExcelFile('portfolio.xlsx')


maindf = pd.DataFrame(columns=['CoinName', 'count', 'totalInvest','currentValue'])
start = dt.datetime.now() #-(1000*60*60)

for k in df.keys():
    tdf = xls.parse(k,parse_cols = 3, skiprows = 0, nrows = 1, header = None)
    val = yf.download(k, start, start)
    current_value = tdf.iloc[0,5]
    row = { 'CoinName': tdf.at[0,1],'count':tdf.at[0,3],'totalInvest':tdf.at[0,5], 'currentValue': current_value}
    maindf= maindf.append(row, ignore_index=True)


st.dataframe(tdf)
st.dataframe( maindf )

pieByCount = go.Figure(
    go.Pie(
        labels = maindf['CoinName'],
        values = maindf['count'],
        hoverinfo = "label+percent+value",
        textinfo = "label+value"
    ))
st.write("## Unit Count per coin")
pieByCount


pieByVolume = go.Figure(
    go.Pie(
        labels = maindf['CoinName'],
        values = maindf['totalInvest'],
        hoverinfo = "label+percent+value",
        textinfo = "label+value"
    ))

st.write("## Investment per coin")
pieByVolume

## Treemap
st.write("## Your treasure repartition")
treemap = px.treemap(maindf, path=[px.Constant("all"), 'CoinName'], values='totalInvest', labels='CoinName',hover_name="CoinName")
treemap.update_traces(root_color="lightgreen")
treemap.update_layout(margin = dict(t=50, l=25, r=25, b=25))
st.write("## Treemap ")
st.plotly_chart(treemap, use_container_width=True)

# show comparison of total investment and current value in a Sankey chart
sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=15,
        line = dict(color = "yellow", width = 0.5),
        label=["Total Investment", "Current Value"],
        color=["lightblue", "lightgreen"]
    ),
    link=dict(
        source=[0, 0, 1, 1],
        target=[1, 2, 2, 2],
        value=[maindf['totalInvest'].sum(), maindf['currentValue'].sum()]
    )
)])

sankey.update_layout(title_text="Investment vs Current Value")
st.write("## Investment vs Current Value")
st.plotly_chart(sankey, use_container_width=True)


# 1/ horizontal bar chart : total invest + current value
hbar = go.Figure(data=[go.Bar(
    x=maindf['totalInvest'],
    y=maindf['currentValue'],
    marker_color='lightblue',
    name='Total Investment + Current Value'
)])
hbar.update_layout(title_text="Total Investment + Current Value")
st.write("## Total Investment + Current Value")
st.plotly_chart(hbar, use_container_width=True)


# 2/ double donut: inner=invest , outer = value
pie = px.pie(maindf, values='currentValue', names='CoinName', title='Total Investment')
# ddonut = px.sunburst(maindf, path=['totalInvest', 'currentValue'], values='currentValue')
# ddonut.update_traces(textposition='inside')
# st.write("## Investment vs Current Value")
st.plotly_chart(pie, use_container_width=True)

# 3/ vertical bar chart w/ 2 columns per coin
bar = go.Figure(data=[go.Bar(
    x=maindf['CoinName'],
    y=maindf['totalInvest'],
    marker_color='lightblue',
    name='Total Investment'
)])

bar.update_layout(title_text="Total Investment")
st.write("## Total Investment")
st.plotly_chart(bar, use_container_width=True)

# component showing a balance