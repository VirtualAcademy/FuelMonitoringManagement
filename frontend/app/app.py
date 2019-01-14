import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from __init__ import create_flask, create_dash

# from .layouts import main_layout_header, main_layout_sidebar


# The Flask instance
server = create_flask()

# The Dash instance
app = create_dash(server)


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    # from . import index

    # configure the Dash instance's layout
    # main_layout_sidebar()
    app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return dbc.Alert('You have selected "{}"'.format(value),className='success')

if __name__ == '__main__':
    app.run_server(debug=True)

