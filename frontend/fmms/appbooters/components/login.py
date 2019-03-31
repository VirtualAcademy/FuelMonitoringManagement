import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask_login import login_user
from api import User
import flask
#from layout import make_form
from application import app
import requests



loginForm = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div(className="shape1"),
                html.Div(className="shape2"),
                html.Div(className="shape3"),
                html.Div(className="shape4"),
                html.Div(className="shape5"),
                html.Div(className="shape6"),
                html.Div(className="shape7"),
                html.Div([
                    dbc.Form([
                            html.Div([
                                dbc.Label(["Username"],className="control-label text-white  requiredField"),
                                # html.Br(),
                                dcc.Input(
                                        id="username",
                                        placeholder="Enter email or username",
                                        type="text",
                                        value="",
                                        className="form-control",)
                            ], className="form-group"),
                            html.Div([
                                dbc.Label(["Password"],className="control-label text-white requiredField"),
                                # html.Br(),
                                dcc.Input(
                                        id="password",
                                        placeholder="Name of the opportunity",
                                        type="password",
                                        value="",
                                        className="form-control",)
                            ], className="form-group"),
                            html.Div([
                                html.Button(
                                        id="submit_btn",
                                        children='Submit',
                                        className="form-control btn btn-info btn-md",style={'color':"white"})
                            ], className="form-group")
                        ], className="loginform")
                ], className="float"),
            ], className="loginbox")
        ], id="login-column" , className="col-md-6")
    ],id="login-row", className="row justify-content-center align-items-center")
], className="container")


@app.callback(Output('url2', 'children'),
              [Input('submit_btn','n_clicks')],
              [State('username','value'),
               State('password','value')])
def loginfxn(n_clicks, username,password):

    api_user = User(username,password)
    # u=api_user_auth.auth_url
    # print('clicked',username,password, api_user.authenticate_user())
    user = api_user.authenticate_user()
    print(user,user.is_authenticated,flask.redirect('/Dashboard',code=200))
    if user.is_authenticated:
        print('before')
        # login_user(user)
        print('/success')
        return dcc.Location(id='url',pathname='/Dashboard',refresh=False)
        # return '/Dashboard'
    else:
        print('Not authenticated')
        pass

    # value_list = v
    # # if n_clicks > 0:
    # query = [value_list[i]
    #     for i in range(len(value_list))
    # ]
    # print(query)
    # login_url = 'http://127.0.0.1:8000/rest-auth/login/'
    # params = dict(username=username,password=password)
    # usercred = requests.post(url=login_url,data=params)
    # print(usercred.json())
    # print('user '+str(username),'pass '+str(password))
    # if usercred.status_code==200:
    #     print('clicked')
    #     print(usercred.json())
    #     user = usercred.json()["user"]["username"]
    #     msg = 'You are logged in as {}'.format(user)
    #     print('clicked '+msg)
    #     return html.P('msg')
    # else:
    #     print('error')
    #     return html.P('error')