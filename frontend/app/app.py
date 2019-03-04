# coding: utf-8
import os

import pandas as pd

import dash
import plotly.graph_objs as go
from layout import dcc, html, dbc, get_logo #, make_dash_table, print_button
# from layout import overview, dashboard, consumption, production, supplies, connectednetworks, home, graphcomponents
from __init__ import create_flask, create_dash
from dash.dependencies import Input, Output
from flask_cors import CORS

# The Flask instance
# server = create_flask()
#
# # The Dash instance
# app = create_dash(server)


app = dash.Dash(__name__)
server = app.server
CORS(server)

# Custom Script for Heroku
if 'DYNO' in os.environ:
    app.scripts.config.serve_locally = False
    # app.scripts.append_script({
    #     'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    # })

# read data for tables (one df per table)
# df_fund_facts = pd.read_csv('data/df_fund_facts.csv')
# df_price_perf = pd.read_csv('data/df_price_perf.csv')
# df_current_prices = pd.read_csv('data/df_current_prices.csv')
# df_hist_prices = pd.read_csv('data/df_hist_prices.csv')
# df_avg_returns = pd.read_csv('data/df_avg_returns.csv')
# df_after_tax = pd.read_csv('data/df_after_tax.csv')
# df_recent_returns = pd.read_csv('data/df_recent_returns.csv')
# df_equity_char = pd.read_csv('data/df_equity_char.csv')
# df_equity_diver = pd.read_csv('data/df_equity_diver.csv')
# df_expenses = pd.read_csv('data/df_expenses.csv')
# df_minimums = pd.read_csv('data/df_minimums.csv')
# df_dividend = pd.read_csv('data/df_dividend.csv')
# df_realized = pd.read_csv('data/df_realized.csv')
# df_unrealized = pd.read_csv('data/df_unrealized.csv')
# df_graph = pd.read_csv("data/df_graph.csv")
#


noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
mainlayout = html.Div([
    dcc.Location(id='url', refresh=False),
        get_logo(),
    html.Div(id='page-content')
], id='head')


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
        # load the rest of our Dash app
    from layout import overview, dashboard, consumption, production, supplies, connectednetworks, home, graphcomponents
    # configure the Dash instance's layout
    app.layout = mainlayout


    # Update page
    # # # # # # # # #
    # detail in depth what the callback below is doing
    # # # # # # # # #
    @app.callback(dash.dependencies.Output('page-content', 'children'),
                  [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':#'/dash-vanguard-report' or pathname == '/dash-vanguard-report/overview':
            return home.home
        elif pathname == '/Dashboard':#'/dash-vanguard-report' or pathname == '/dash-vanguard-report/overview':
            return dashboard.dashboard
        elif pathname == '/manage/production':
            return production.production
        elif pathname == '/manage/consumption':
            return consumption.consumption
        elif pathname == '/manage/supplies/delivery_order':
            return supplies.delivery_order
        elif pathname == '/manage/supplies/delivery_schedule':
            return supplies.delivery_schedule
        elif pathname == '/manage/supplies/delivery_confirmation':
            return supplies.delivery_confirmation
        elif pathname == '/dash-vanguard-report' or pathname == '/dash-vanguard-report/overview':
            return production.production
        else:
            return noPage


# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #
# external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
#                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
#                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "https://codepen.io/bcd/pen/KQrXdb.css",
#                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
#
# for css in external_css:
#     app.css.append_css({"external_url": css})
#
# external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
#                "https://codepen.io/bcd/pen/YaXojL.js"]
#
# for js in external_js:
#     app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
