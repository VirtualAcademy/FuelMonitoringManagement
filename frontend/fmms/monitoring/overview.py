import dash_html_components as html
import dash_core_components as dcc
# from layout.components import Header, make_dash_table, print_button

from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import datetime
import plotly
import numpy as np
import pandas as pd
import psutil
from layout.components import Header, make_dash_table, print_button, make_row
from application import app

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

## Page layouts
overview = html.Div([  # page 1
            Header('Monitoring - Overview'),
    html.Div(children=[
    html.Div([
        html.H4('Generation Forecast'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        html.H4('Fuel Status'),
        html.Div(id='live-update-proc'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000  # in milliseconds
        )
    ])
],
    style={'backgroundColor': colors['background'], 'color': colors['text']}
)
], className="page")

class Context:
    def __init__(self):
        self.t = []
        self.cpu = []
        self.per_cpu = [[] for x in range(psutil.cpu_count())]
        self.mem = []

    @classmethod
    def append_data(cls, d1, d2):
        n = len(d1)
        if n > 100:
            del d1[0:n - 99]
        d1.append(d2)


context = Context()

# The `dcc.Interval` component emits an event called "interval"
# every `interval` number of milliseconds.
# Subscribe to this event with the `events` argument of `app.callback`


@app.callback(Output('live-update-text', 'children'),
              events=[Event('interval-component', 'interval')])
def update_metrics():
    now = datetime.datetime.now()
    hour, minute, second = now.hour, now.minute, now.second
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Usage: {}%'.format(context.cpu[-1]), style=style),
        html.Span('Estimate: {}%'.format(context.mem[-1]), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    # global context
    context.append_data(context.t, datetime.datetime.now())
    context.append_data(context.cpu, psutil.cpu_percent())
    for data, pct in zip(context.per_cpu, psutil.cpu_percent(percpu=True)):
        context.append_data(data, pct)
    context.append_data(context.mem, psutil.virtual_memory().percent)

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2,print_grid=False)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['plot_bgcolor'] = colors['background']
    fig['layout']['paper_bgcolor'] = colors['background']
    fig['layout']['font'] = {'color': colors['text']}
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
    fig['layout']['yaxis1'].update(range=[0, 100])
    fig['layout']['yaxis2'].update(range=[0, 100])

    fig.append_trace({
        'x': context.t,
        'y': context.cpu,
        'name': 'Usage',
        'mode': 'lines',
        'type': 'scatter',
    }, 1, 1)
    for i, y in enumerate(context.per_cpu):
        fig.append_trace({
            'x': context.t,
            'y': y,
            'name': 'Plant {}'.format(i),
            'mode': 'lines',
            'type': 'scatter',
        }, 1, 1)
    fig.append_trace({
        'x': context.t,
        'y': context.mem,
        'name': 'Estimate',
        'mode': 'lines',
        'type': 'scatter',
        'fill': 'tonexty',
    }, 2, 1)

    return fig


def get_proc_df():
    def get_proc(proc):
        try:
            pinfo = proc
        except psutil.NoSuchProcess:
            pass
        return (pinfo.pid, pinfo.name(), pinfo.memory_percent(), pinfo.cpu_percent())

    data = [get_proc(proc) for proc in psutil.process_iter()]
    df = pd.DataFrame(data, columns=['Identification', 'Name', 'Estimate', 'Usage'])
    df['Estimate'] = df['Estimate'].map(lambda x: '{:.2f}%'.format(x))
    df['Usage'] = df['Usage'] / psutil.cpu_count()
    df['Usage'] = df['Usage'].map(lambda x: '{:.2f}%'.format(x))
    return df.sort_values('Usage', ascending=False)


@app.callback(Output('live-update-proc', 'children'),
              events=[Event('interval-component', 'interval')])
def generate_table():
    df = get_proc_df()
    max_rows = 10
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col], style={'width': '8em'}) for col in df.columns
        ]) for i in range(min(len(df), max_rows))]
    )
#html.Div([  # page 1

    #     html.Div([
    #         Header('Overview'),
    #
    #         # Row 3
    #         html.Div([
    #
    #             html.Div([
    #                 html.H6('Product Summary',
    #                         className="gs-header gs-text-header padded"),
    #
    #                 html.Br([]),
    #
    #                 html.P("\
    #                         As the industry’s first index fund for individual investors, \
    #                         the 500 Index Fund is a low-cost way to gain diversified exposure \
    #                         to the U.S. equity market. The fund offers exposure to 500 of the \
    #                         largest U.S. companies, which span many different industries and \
    #                         account for about three-fourths of the U.S. stock market’s value. \
    #                         The key risk for the fund is the volatility that comes with its full \
    #                         exposure to the stock market. Because the 500 Index Fund is broadly \
    #                         diversified within the large-capitalization market, it may be \
    #                         considered a core equity holding in a portfolio."),
    #
    #             ], className="six columns"),
    #
    #             html.Div([
    #                 html.H6(["Fund Facts"],
    #                         className="gs-header gs-table-header padded"),
    #                 # html.Table(make_dash_table(df_fund_facts))
    #             ], className="six columns"),
    #
    #         ], className="row "),
    #
    #         # Row 4
    #
    #         html.Div([
    #
    #             html.Div([
    #                 html.H6('Average annual performance',
    #                         className="gs-header gs-text-header padded"),
    #                 # dcc.Graph(
    #                 #     id = "graph-1",
    #                 #     figure={
    #                 #         'data': [
    #                 #             go.Bar(
    #                 #                 x = ["1 Year", "3 Year", "5 Year", "10 Year", "41 Year"],
    #                 #                 y = ["21.67", "11.26", "15.62", "8.37", "11.11"],
    #                 #                 marker = {
    #                 #                   "color": "rgb(53, 83, 255)",
    #                 #                   "line": {
    #                 #                     "color": "rgb(255, 255, 255)",
    #                 #                     "width": 2
    #                 #                   }
    #                 #                 },
    #                 #                 name = "500 Index Fund"
    #                 #             ),
    #                 #             go.Bar(
    #                 #                 x = ["1 Year", "3 Year", "5 Year", "10 Year", "41 Year"],
    #                 #                 y = ["21.83", "11.41", "15.79", "8.50"],
    #                 #                 marker = {
    #                 #                   "color": "rgb(255, 225, 53)",
    #                 #                   "line": {
    #                 #                     "color": "rgb(255, 255, 255)",
    #                 #                     "width": 2
    #                 #                     }
    #                 #                 },
    #                 #                 name = "S&P 500 Index"
    #                 #             ),
    #                 #         ],
    #                 #         'layout': go.Layout(
    #                 #             autosize = False,
    #                 #             bargap = 0.35,
    #                 #             font = {
    #                 #               "family": "Raleway",
    #                 #               "size": 10
    #                 #             },
    #                 #             height = 200,
    #                 #             hovermode = "closest",
    #                 #             legend = {
    #                 #               "x": -0.0228945952895,
    #                 #               "y": -0.189563896463,
    #                 #               "orientation": "h",
    #                 #               "yanchor": "top"
    #                 #             },
    #                 #             margin = {
    #                 #               "r": 0,
    #                 #               "t": 20,
    #                 #               "b": 10,
    #                 #               "l": 10
    #                 #             },
    #                 #             showlegend = True,
    #                 #             title = "",
    #                 #             width = 340,
    #                 #             xaxis = {
    #                 #               "autorange": True,
    #                 #               "range": [-0.5, 4.5],
    #                 #               "showline": True,
    #                 #               "title": "",
    #                 #               "type": "category"
    #                 #             },
    #                 #             yaxis = {
    #                 #               "autorange": True,
    #                 #               "range": [0, 22.9789473684],
    #                 #               "showgrid": True,
    #                 #               "showline": True,
    #                 #               "title": "",
    #                 #               "type": "linear",
    #                 #               "zeroline": False
    #                 #             }
    #                 #         )
    #                 #     },
    #                 #     config={
    #                 #         'displayModeBar': False
    #                 #     }
    #                 # )
    #             ], className="six columns"),
    #
    #             html.Div([
    #                 html.H6("Hypothetical growth of $10,000",
    #                         className="gs-header gs-table-header padded"),
    #                 # dcc.Graph(
    #                 #     id="grpah-2",
    #                 #     figure={
    #                 #         'data': [
    #                 #             go.Scatter(
    #                 #                 x = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"],
    #                 #                 y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000", "19000", "20500", "24000"],
    #                 #                 line = {"color": "rgb(53, 83, 255)"},
    #                 #                 mode = "lines",
    #                 #                 name = "500 Index Fund Inv"
    #                 #             )
    #                 #         ],
    #                 #         'layout': go.Layout(
    #                 #             autosize = False,
    #                 #             title = "",
    #                 #             font = {
    #                 #               "family": "Raleway",
    #                 #               "size": 10
    #                 #             },
    #                 #             height = 200,
    #                 #             width = 340,
    #                 #             hovermode = "closest",
    #                 #             legend = {
    #                 #               "x": -0.0277108433735,
    #                 #               "y": -0.142606516291,
    #                 #               "orientation": "h"
    #                 #             },
    #                 #             margin = {
    #                 #               "r": 20,
    #                 #               "t": 20,
    #                 #               "b": 20,
    #                 #               "l": 50
    #                 #             },
    #                 #             showlegend = True,
    #                 #             xaxis = {
    #                 #               "autorange": True,
    #                 #               "linecolor": "rgb(0, 0, 0)",
    #                 #               "linewidth": 1,
    #                 #               "range": [2008, 2018],
    #                 #               "showgrid": False,
    #                 #               "showline": True,
    #                 #               "title": "",
    #                 #               "type": "linear"
    #                 #             },
    #                 #             yaxis = {
    #                 #               "autorange": False,
    #                 #               "gridcolor": "rgba(127, 127, 127, 0.2)",
    #                 #               "mirror": False,
    #                 #               "nticks": 4,
    #                 #               "range": [0, 30000],
    #                 #               "showgrid": True,
    #                 #               "showline": True,
    #                 #               "ticklen": 10,
    #                 #               "ticks": "outside",
    #                 #               "title": "$",
    #                 #               "type": "linear",
    #                 #               "zeroline": False,
    #                 #               "zerolinewidth": 4
    #                 #             }
    #                 #         )
    #                 #     },
    #                 #     config={
    #                 #         'displayModeBar': False
    #                 #     }
    #                 # )
    #             ], className="six columns"),
    #
    #         ], className="row "),
    #
    #         # Row 5
    #
    #         html.Div([
    #
    #             html.Div([
    #                 html.H6('Price & Performance (%)',
    #                         className="gs-header gs-table-header padded"),
    #                 # html.Table(make_dash_table(df_price_perf))
    #             ], className="six columns"),
    #
    #             html.Div([
    #                 html.H6("Risk Potential",
    #                         className="gs-header gs-table-header padded"),
    #                 # dcc.Graph(
    #                 #     id='graph-3',
    #                 #     figure = {
    #                 #         'data': [
    #                 #             go.Scatter(
    #                 #                 x = ["0", "0.18", "0.18", "0"],
    #                 #                 y = ["0.2", "0.2", "0.4", "0.2"],
    #                 #                 fill = "tozerox",
    #                 #                 fillcolor = "rgba(31, 119, 180, 0.2)",
    #                 #                 hoverinfo = "none",
    #                 #                 line = {"width": 0},
    #                 #                 mode = "lines",
    #                 #                 name = "B",
    #                 #                 showlegend = False
    #                 #             ),
    #                 #             go.Scatter(
    #                 #                 x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
    #                 #                 y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
    #                 #                 fill = "tozerox",
    #                 #                 fillcolor = "rgba(31, 119, 180, 0.4)",
    #                 #                 hoverinfo = "none",
    #                 #                 line = {"width": 0},
    #                 #                 mode = "lines",
    #                 #                 name = "D",
    #                 #                 showlegend = False
    #                 #             ),
    #                 #             go.Scatter(
    #                 #                 x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
    #                 #                 y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
    #                 #                 fill = "tozerox",
    #                 #                 fillcolor = "rgba(31, 119, 180, 0.6)",
    #                 #                 hoverinfo = "none",
    #                 #                 line = {"width": 0},
    #                 #                 mode = "lines",
    #                 #                 name = "F",
    #                 #                 showlegend = False
    #                 #             ),
    #                 #             go.Scatter(
    #                 #                 x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
    #                 #                 y = ["0.2", "0.2", "1", "0.8", "0.2"],
    #                 #                 fill = "tozerox",
    #                 #                 fillcolor = "rgb(31, 119, 180)",
    #                 #                 hoverinfo = "none",
    #                 #                 line = {"width": 0},
    #                 #                 mode = "lines",
    #                 #                 name = "H",
    #                 #                 showlegend = False
    #                 #             ),
    #                 #             go.Scatter(
    #                 #                 x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
    #                 #                 y = ["0.2", "0.2", "1.2", "1", "0.2"],
    #                 #                 fill = "tozerox",
    #                 #                 fillcolor = "rgba(31, 119, 180, 0.8)",
    #                 #                 hoverinfo = "none",
    #                 #                 line = {"width": 0},
    #                 #                 mode = "lines",
    #                 #                 name = "J",
    #                 #                 showlegend = False
    #                 #             ),
    #                 #         ],
    #                 #         'layout': go.Layout(
    #                 #             title = "",
    #                 #             annotations = [
    #                 #                 {
    #                 #                   "x": 0.69,
    #                 #                   "y": 0.6,
    #                 #                   "font": {
    #                 #                     "color": "rgb(31, 119, 180)",
    #                 #                     "family": "Raleway",
    #                 #                     "size": 30
    #                 #                   },
    #                 #                   "showarrow": False,
    #                 #                   "text": "<b>4</b>",
    #                 #                   "xref": "x",
    #                 #                   "yref": "y"
    #                 #                 },
    #                 #                 {
    #                 #                   "x": 0.0631034482759,
    #                 #                   "y": -0.04,
    #                 #                   "align": "left",
    #                 #                   "font": {
    #                 #                     "color": "rgb(44, 160, 44)",
    #                 #                     "family": "Raleway",
    #                 #                     "size": 10
    #                 #                   },
    #                 #                   "showarrow": False,
    #                 #                   "text": "<b>Less risk<br>Less reward</b>",
    #                 #                   "xref": "x",
    #                 #                   "yref": "y"
    #                 #                 },
    #                 #                 {
    #                 #                   "x": 0.92125,
    #                 #                   "y": -0.04,
    #                 #                   "align": "right",
    #                 #                   "font": {
    #                 #                     "color": "rgb(214, 39, 40)",
    #                 #                     "family": "Raleway",
    #                 #                     "size": 10
    #                 #                   },
    #                 #                   "showarrow": False,
    #                 #                   "text": "<b>More risk<br>More reward</b>",
    #                 #                   "xref": "x",
    #                 #                   "yref": "y"
    #                 #                 }
    #                 #               ],
    #                 #               autosize = False,
    #                 #               height = 200,
    #                 #               width = 340,
    #                 #               hovermode = "closest",
    #                 #               margin = {
    #                 #                 "r": 10,
    #                 #                 "t": 20,
    #                 #                 "b": 80,
    #                 #                 "l": 10
    #                 #               },
    #                 #               shapes = [
    #                 #                 {
    #                 #                   "fillcolor": "rgb(255, 255, 255)",
    #                 #                   "line": {
    #                 #                     "color": "rgb(31, 119, 180)",
    #                 #                     "width": 4
    #                 #                   },
    #                 #                   "opacity": 1,
    #                 #                   "type": "circle",
    #                 #                   "x0": 0.621,
    #                 #                   "x1": 0.764,
    #                 #                   "xref": "x",
    #                 #                   "y0": 0.135238095238,
    #                 #                   "y1": 0.98619047619,
    #                 #                   "yref": "y"
    #                 #                 }
    #                 #               ],
    #                 #               showlegend = True,
    #                 #               xaxis = {
    #                 #                 "autorange": False,
    #                 #                 "fixedrange": True,
    #                 #                 "range": [-0.05, 1.05],
    #                 #                 "showgrid": False,
    #                 #                 "showticklabels": False,
    #                 #                 "title": "<br>",
    #                 #                 "type": "linear",
    #                 #                 "zeroline": False
    #                 #               },
    #                 #               yaxis = {
    #                 #                 "autorange": False,
    #                 #                 "fixedrange": True,
    #                 #                 "range": [-0.3, 1.6],
    #                 #                 "showgrid": False,
    #                 #                 "showticklabels": False,
    #                 #                 "title": "<br>",
    #                 #                 "type": "linear",
    #                 #                 "zeroline": False
    #                 #             }
    #                 #         )
    #                 #     },
    #                 #     config={
    #                 #         'displayModeBar': False
    #                 #     }
    #                 # )
    #             ], className="six columns"),
    #
    #         ], className="row ")
    #
    #     ], className="subpage")
    #
    # ], className="page")
    #
