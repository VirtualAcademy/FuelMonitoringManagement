import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from collections import OrderedDict
from layout.components import Header, make_dash_table, print_button, make_row


delivery_order =  html.Div([  # page 1
            Header('Delivery Order'),

    # Row 1
], className="page")

delivery_schedule =  html.Div([  # page 1
            Header('Delivery Schedule'),

    # Row 1
], className="page")

delivery_confirmation =  html.Div([  # page 1
            Header('Delivery Confirmation'),

    # Row 1
], className="page")