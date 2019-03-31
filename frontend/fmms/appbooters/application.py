import flask
import dash

# User management initialization
import yaml
from flask_login import LoginManager
from appbooters.api_requests import User, USERCONFIG


server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.title = "FMMS"
# app._favicon = None
app.config.suppress_callback_exceptions = True

#
# Setup the LoginManager for the server
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

def get_user_info(id):
	return USERCONFIG.get('USERS',str(id))