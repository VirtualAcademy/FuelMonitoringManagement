import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app, server
import plotly.graph_objs as go
import pandas as pd
from collections import OrderedDict
# from forms.form import MyForm
from layout.components import Header, make_dash_table, print_button, make_row
# from api.manager import DashBoardManager
#
# f=DashBoardManager()
# print(f.get_autonomy(''))

app.config['suppress_callback_exceptions']=True

production =  html.Div([  # page 1
            Header('Production'),
    html.Div([
        # dcc.Location(id='sub-url', refresh=False),
        # dbc
        dbc.Tabs([
            dbc.Tab(label='Autonomy   ',id='tab-1',tab_id='autono1'),
            dbc.Tab(label='Power Plannts   ', id='tab-2'),
            dbc.Tab(label='Demand   ', id='tab-3'),
            dbc.Tab(label='Power Availability   ',id='tab-4'),
            dbc.Tab(label='Production Forecast   ', id='tab-5'),
            dbc.Tab()
            # dcc.Tab(label='Power Plannts   ',value=2, id='tab-2')
        ]),

        #
        # dcc.Link('Demand   ', href='/dash-vanguard-report/portfolio-management', className="tab",id='tab-3'),
        #
        # dcc.Link('Power Availability   ', href='/dash-vanguard-report/fees', className="tab",id='tab-4'),
        #
        # dcc.Link('Production Forecast   ', href='/dash-vanguard-report/distributions', className="tab"),

        # dcc.Link('News & Reviews   ', href='/dash-vanguard-report/news-and-reviews', className="tab")
        # html.Div(['This is no page'])
    ], className="row justify-content-center align-items-center", id='submenu'),

    # Row 1

    html.Div(id='production-page-content')
], className="page")

n = html.Div(['This is no page'])
h = html.Div(['This is prodiction'])


# with server.app_context():
@app.callback(dash.dependencies.Output('production-page-content', 'children'),
              [dash.dependencies.Input('autono1', 'n_clicks'),
               dash.dependencies.Input('tab-2', 'n_clicks'),
               dash.dependencies.Input('sub-url', 'n_clicks')])
def display(n):
    # if pathname == '/':  # '/dash-vanguard-report' or pathname == '/dash-vanguard-report/overview':
    #     return home.home
    # elif pathname == '/Dashboard':  # '/dash-vanguard-report' or pathname == '/dash-vanguard-report/overview':
    #     return dashboard.dashboard
    # elif pathname == '/manage/production':
    #     return production.production
    # elif pathname == '/manage/consumption':
    #     return consumption.consumption
    # elif pathname == '/manage/supplies/delivery_order':
    #     return supplies.delivery_order
    # elif pathname == '/manage/supplies/delivery_schedule':
    #     return supplies.delivery_schedule
    if n>0:# == 'Autonomy   ':
        print('True')
        return h
    # elif label == 'Power Plannts   ':
    #     return n
    # else:
    #     return n

