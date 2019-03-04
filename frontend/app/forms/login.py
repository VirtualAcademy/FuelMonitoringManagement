import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from layout import make_form

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
                                dcc.Input(
                                        id="submit_btn",
                                        placeholder="Name of the opportunity",
                                        type="submit",
                                        value="submit",
                                        className="form-control btn btn-info btn-md",style={'color':"white"})
                            ], className="form-group")
                        ], className="loginform")
                ], className="float"),
            ], className="loginbox")
        ], id="login-column" , className="col-md-6")
    ],id="login-row", className="row justify-content-center align-items-center")
], className="container")


