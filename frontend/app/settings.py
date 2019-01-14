import os

# Variables defined in this file will be passed to the 'config' attribute of the
# Flask instance used by the Dash app. They must be in UPPER CASE in order to
# take effect. For more information see http://flask.pocoo.org/docs/config.

#
# Config for the Dash instance
#

# Your App's title. The value of this parameter will be propagated into
# `app.title`
TITLE = 'FMMS'

# The value of this parameter will be propagated into both
# `app.scripts.config.serve_locally` and `app.css.config.serve_locally`
SERVE_LOCALLY = False

# Prefix for Dash URL routes and client-side requests. Passed into Dash's
# `url_base_pathname` keyword argument. Must begin and end with a '/'.
URL_BASE_PATHNAME = '/'

# Custom CSS files go in here. Passed into Dash's `external_stylesheets`
# keyword argument.  If you want to use Bootstrap from a CDN, Dash Bootstrap
# Components contains links to bootstrapcdn:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.BOOTSTRAP]
#
# or if you want to use a Bootswatch theme:
#
# import dash_bootstrap_components as dbc
# EXTERNAL_STYLESHEETS = [dbc.themes.CYBORG]
EXTERNAL_STYLESHEETS = []

# Custom CSS files go in here. Passed into Dash's `external_scripts` keyword
# argument
EXTERNAL_SCRIPTS = []


#
# Layout config
#

# The ID of the element used to inject each page of the multi-page app into
CONTENT_CONTAINER_ID = 'page-content'

NAVBAR_CONTAINER_ID = 'navbar-items'

# BOOTSTRAP = (
#     "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
# )

# # Grid only
# GRID = "bootstrap/css/bootstrap-grid.min.css"  #
#
# BOOTSWATCH_BASE = "bootswatch/"
#
# THEMES = dict(
#     CERULEAN = BOOTSWATCH_BASE + "cerulean/bootstrap.min.css",
#     COSMO = BOOTSWATCH_BASE + "cosmo/bootstrap.min.css",
#     CYBORG = BOOTSWATCH_BASE + "cyborg/bootstrap.min.css",
#     DARKLY = BOOTSWATCH_BASE + "darkly/bootstrap.min.css",
#     FLATLY = BOOTSWATCH_BASE + "flatly/bootstrap.min.css",
#     JOURNAL = BOOTSWATCH_BASE + "journal/bootstrap.min.css",
#     LITERA = BOOTSWATCH_BASE + "litera/bootstrap.min.css",
#     LUMEN = BOOTSWATCH_BASE + "lumen/bootstrap.min.css",
#     LUX = BOOTSWATCH_BASE + "lux/bootstrap.min.css",
#     MATERIA = BOOTSWATCH_BASE + "materia/bootstrap.min.css",
#     MINTY = BOOTSWATCH_BASE + "minty/bootstrap.min.css",
#     PULSE = BOOTSWATCH_BASE + "pulse/bootstrap.min.css",
#     SANDSTONE = BOOTSWATCH_BASE + "sandstone/bootstrap.min.css",
#     SIMPLEX = BOOTSWATCH_BASE + "simplex/bootstrap.min.css",
#     SKETCHY = BOOTSWATCH_BASE + "sketchy/bootstrap.min.css",
#     SLATE = BOOTSWATCH_BASE + "slate/bootstrap.min.css",
#     SOLAR = BOOTSWATCH_BASE + "solar/bootstrap.min.css",
#     SPACELAB = BOOTSWATCH_BASE + "spacelab/bootstrap.min.css",
#     SUPERHERO = BOOTSWATCH_BASE + "superhero/bootstrap.min.css",
#     UNITED = BOOTSWATCH_BASE + "united/bootstrap.min.css",
#     YETI = BOOTSWATCH_BASE + "yeti/bootstrap.min.css"
# )
