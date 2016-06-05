#!/usr/bin/env python
"""
	postToPlotly.py

	updates the plots and data for pagecount, wordcount etc in plotly

----------

	-jbsilva
"""

import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd;

datapd = pd.read_csv('ProgressMetrics/pageData.csv')
datapd.index.names = ['Id'];

x0 = datapd.dayOfYear
y0 = datapd.PagesCompleted

trace0 = Scatter(
    x=x0,
    y=y0,
    mode='markers'
)

data = Data([trace0])

layout = Layout(
    title='Thesis Pages Completed',
    xaxis=XAxis(
        title='Day Of Year',
        titlefont=Font(
            color='black'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=Font(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='All'
    ),
    yaxis=YAxis(
        title='Pages Completed',
        titlefont=Font(
            color='black'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=Font(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='All'
    )
)

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='thesis_pages', auto_open=False)
