import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from collections import OrderedDict
from layout.components import Header, make_dash_table, print_button, make_row


# portfolioManagement = html.Div([ # page 3
#
#         print_button(),
#
#         html.Div([
#
#             Header(),
#
#             # Row 1
#
#             html.Div([
#
#                 html.Div([
#                     html.H6(["Portfolio"],
#                             className="gs-header gs-table-header padded")
#                 ], className="twelve columns"),
#
#             ], className="row "),
#
#             # Row 2
#
#             html.Div([
#
#                 html.Div([
#                     html.Strong(["Stock style"]),
#                     dcc.Graph(
#                         id='graph-5',
#                         figure={
#                             'data': [
#                                 go.Scatter(
#                                     x = ["1"],
#                                     y = ["1"],
#                                     hoverinfo = "none",
#                                     marker = {
#                                         "opacity": 0
#                                     },
#                                     mode = "markers",
#                                     name = "B",
#                                 )
#                             ],
#                             'layout': go.Layout(
#                                 title = "",
#                                 annotations = [
#                                 {
#                                   "x": 0.990130093458,
#                                   "y": 1.00181709504,
#                                   "align": "left",
#                                   "font": {
#                                     "family": "Raleway",
#                                     "size": 9
#                                   },
#                                   "showarrow": False,
#                                   "text": "<b>Market<br>Cap</b>",
#                                   "xref": "x",
#                                   "yref": "y"
#                                 },
#                                 {
#                                   "x": 1.00001816013,
#                                   "y": 1.35907755794e-16,
#                                   "font": {
#                                     "family": "Raleway",
#                                     "size": 9
#                                   },
#                                   "showarrow": False,
#                                   "text": "<b>Style</b>",
#                                   "xref": "x",
#                                   "yanchor": "top",
#                                   "yref": "y"
#                                 }
#                               ],
#                               autosize = False,
#                               width = 200,
#                               height = 150,
#                               hovermode = "closest",
#                               margin = {
#                                 "r": 30,
#                                 "t": 20,
#                                 "b": 20,
#                                 "l": 30
#                               },
#                               shapes = [
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0,
#                                   "x1": 0.33,
#                                   "xref": "paper",
#                                   "y0": 0,
#                                   "y1": 0.33,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "dash": "solid",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0.33,
#                                   "x1": 0.66,
#                                   "xref": "paper",
#                                   "y0": 0,
#                                   "y1": 0.33,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0.66,
#                                   "x1": 0.99,
#                                   "xref": "paper",
#                                   "y0": 0,
#                                   "y1": 0.33,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0,
#                                   "x1": 0.33,
#                                   "xref": "paper",
#                                   "y0": 0.33,
#                                   "y1": 0.66,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0.33,
#                                   "x1": 0.66,
#                                   "xref": "paper",
#                                   "y0": 0.33,
#                                   "y1": 0.66,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0.66,
#                                   "x1": 0.99,
#                                   "xref": "paper",
#                                   "y0": 0.33,
#                                   "y1": 0.66,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0,
#                                   "x1": 0.33,
#                                   "xref": "paper",
#                                   "y0": 0.66,
#                                   "y1": 0.99,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(255, 127, 14)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 1
#                                   },
#                                   "opacity": 0.9,
#                                   "type": "rect",
#                                   "x0": 0.33,
#                                   "x1": 0.66,
#                                   "xref": "paper",
#                                   "y0": 0.66,
#                                   "y1": 0.99,
#                                   "yref": "paper"
#                                 },
#                                 {
#                                   "fillcolor": "rgb(127, 127, 127)",
#                                   "line": {
#                                     "color": "rgb(0, 0, 0)",
#                                     "width": 2
#                                   },
#                                   "opacity": 0.3,
#                                   "type": "rect",
#                                   "x0": 0.66,
#                                   "x1": 0.99,
#                                   "xref": "paper",
#                                   "y0": 0.66,
#                                   "y1": 0.99,
#                                   "yref": "paper"
#                                 }
#                               ],
#                               xaxis = {
#                                 "autorange": True,
#                                 "range": [0.989694747864, 1.00064057995],
#                                 "showgrid": False,
#                                 "showline": False,
#                                 "showticklabels": False,
#                                 "title": "<br>",
#                                 "type": "linear",
#                                 "zeroline": False
#                               },
#                               yaxis = {
#                                 "autorange": True,
#                                 "range": [-0.0358637178721, 1.06395696354],
#                                 "showgrid": False,
#                                 "showline": False,
#                                 "showticklabels": False,
#                                 "title": "<br>",
#                                 "type": "linear",
#                                 "zeroline": False
#                               }
#                             )
#                         },
#                         config={
#                             'displayModeBar': False
#                         }
#                     )
#
#                 ], className="four columns"),
#
#                 html.Div([
#                     html.P("Vanguard 500 Index Fund seeks to track the performance of\
#                      a benchmark index that meaures the investment return of large-capitalization stocks."),
#                     html.P("Learn more about this portfolio's investment strategy and policy.")
#                 ], className="eight columns middle-aligned"),
#
#             ], className="row "),
#
#             # Row 3
#
#             html.Br([]),
#
#             html.Div([
#
#                 html.Div([
#                     html.H6(["Equity characteristics as of 01/31/2018"], className="gs-header gs-table-header tiny-header"),
#                     html.Table(make_dash_table(df_equity_char), className="tiny-header")
#                 ], className=" twelve columns"),
#
#             ], className="row "),
#
#             # Row 4
#
#             html.Div([
#
#                 html.Div([
#                     html.H6(["Equity sector diversification"], className="gs-header gs-table-header tiny-header"),
#                     html.Table(make_dash_table(df_equity_diver), className="tiny-header")
#                 ], className=" twelve columns"),
#
#             ], className="row "),
#
#         ], className="subpage")
#
#     ], className="page")
#
# feesMins = html.Div([  # page 4
#
#         print_button(),
#
#         html.Div([
#
#             Header(),
#
#             # Row 1
#
#             html.Div([
#
#                 html.Div([
#                     html.H6(["Expenses"],
#                             className="gs-header gs-table-header padded")
#                 ], className="twelve columns"),
#
#             ], className="row "),
#
#             # Row 2
#
#             html.Div([
#
#                 html.Div([
#                     html.Strong(),
#                     html.Table(make_dash_table(df_expenses)),
#                     html.H6(["Minimums"],
#                             className="gs-header gs-table-header padded"),
#                     html.Table(make_dash_table(df_minimums))
#                 ], className="six columns"),
#
#                 html.Div([
#                     html.Br([]),
#                     html.Strong("Fees on $10,000 invested over 10 years"),
#                     dcc.Graph(
#                         id = 'graph-6',
#                         figure = {
#                             'data': [
#                                 go.Bar(
#                                     x = ["Category Average", "This fund"],
#                                     y = ["2242", "329"],
#                                     marker = {"color": "rgb(53, 83, 255)"},
#                                     name = "A"
#                                 ),
#                                 go.Bar(
#                                     x = ["This fund"],
#                                     y = ["1913"],
#                                     marker = {"color": "#ADAAAA"},
#                                     name = "B"
#                                 )
#                             ],
#                             'layout': go.Layout(
#                                 annotations = [
#                                     {
#                                       "x": -0.0111111111111,
#                                       "y": 2381.92771084,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "$2,242",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     },
#                                     {
#                                       "x": 0.995555555556,
#                                       "y": 509.638554217,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "$329",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     },
#                                     {
#                                       "x": 0.995551020408,
#                                       "y": 1730.32432432,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "You save<br><b>$1,913</b>",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     }
#                                   ],
#                                   autosize = False,
#                                   height = 150,
#                                   width = 340,
#                                   bargap = 0.4,
#                                   barmode = "stack",
#                                   hovermode = "closest",
#                                   margin = {
#                                     "r": 40,
#                                     "t": 20,
#                                     "b": 20,
#                                     "l": 40
#                                   },
#                                   showlegend = False,
#                                   title = "",
#                                   xaxis = {
#                                     "autorange": True,
#                                     "range": [-0.5, 1.5],
#                                     "showline": True,
#                                     "tickfont": {
#                                       "family": "Raleway",
#                                       "size": 10
#                                     },
#                                     "title": "",
#                                     "type": "category",
#                                     "zeroline": False
#                                   },
#                                   yaxis = {
#                                     "autorange": False,
#                                     "mirror": False,
#                                     "nticks": 3,
#                                     "range": [0, 3000],
#                                     "showgrid": True,
#                                     "showline": True,
#                                     "tickfont": {
#                                       "family": "Raleway",
#                                       "size": 10
#                                     },
#                                     "tickprefix": "$",
#                                     "title": "",
#                                     "type": "linear",
#                                     "zeroline": False
#                                   }
#                             )
#                         },
#                         config={
#                             'displayModeBar': False
#                         }
#                     )
#                 ], className="six columns"),
#
#             ], className="row "),
#
#             # Row 3
#
#             html.Div([
#
#                 html.Div([
#                     html.H6(["Fees"],
#                             className="gs-header gs-table-header padded"),
#
#                     html.Br([]),
#
#                     html.Div([
#
#                         html.Div([
#                             html.Strong(["Purchase fee"])
#                         ], className="three columns right-aligned"),
#
#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")
#
#
#                     ], className="row "),
#
#                     html.Div([
#
#                         html.Div([
#                             html.Strong(["Redemption fee"])
#                         ], className="three columns right-aligned"),
#
#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")
#
#                     ], className="row "),
#
#                     html.Div([
#
#                         html.Div([
#                             html.Strong(["12b-1 fee"])
#                         ], className="three columns right-aligned"),
#
#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")
#
#                     ], className="row "),
#
#                     html.Div([
#
#                         html.Div([
#                             html.Strong(["Account service fee"])
#                         ], className="three columns right-aligned"),
#
#                         html.Div([
#                             html.Strong(["Nonretirement accounts, traditional IRAs, Roth IRAs, UGMAs/UTMAs, SEP-IRAs, and education savings accounts (ESAs)"]),
#                             html.P(["We charge a $20 annual account service fee for each Vanguard Brokerage Account, as well as each individual Vanguard mutual fund holding with a balance of less than $10,000 in an account. This fee does not apply if you sign up for account access on vanguard.com and choose electronic delivery of statements, confirmations, and Vanguard fund reports and prospectuses. This fee also does not apply to members of Flagship Select™, Flagship®, Voyager Select®, and Voyager® Services."]),
#                             html.Br([]),
#                             html.Strong(["SIMPLE IRAs"]),
#                             html.P(["We charge participants a $25 annual account service fee for each fund they hold in their Vanguard SIMPLE IRA. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
#                             html.Br([]),
#                             html.Strong(["403(b)(7) plans"]),
#                             html.P(["We charge participants a $15 annual account service fee for each fund they hold in their Vanguard 403(b)(7) account. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
#                             html.Br([]),
#                             html.Strong(["Individual 401(k) plans"]),
#                             html.P(["We charge participants a $20 annual account service fee for each fund they hold in their Vanguard Individual 401(k) account. This fee will be waived for all participants in the plan if at least 1 participant qualifies for Flagship Select, Flagship, Voyager Select, and Voyager Services"]),
#                             html.Br([]),
#                         ], className="nine columns")
#
#                     ], className="row ")
#
#                 ], className="twelve columns")
#
#             ], className="row "),
#
#         ], className="subpage")
#
#     ], className="page")
