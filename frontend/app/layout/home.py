import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from forms import login
from layout.components import Header, make_dash_table, print_button

## Page layouts
home = html.Div([  # page 1

        html.Div([
            Header('HOME - Login'),
            login.loginForm
        #     # Row 3
        #     html.Div([
        #
        #         html.Div([
        #             html.H6('Product Summary',
        #                     className="gs-header gs-text-header padded"),
        #
        #             html.Br([]),
        #
        #             html.P("\
        #                     As the industry’s first index fund for individual investors, \
        #                     the 500 Index Fund is a low-cost way to gain diversified exposure \
        #                     to the U.S. equity market. The fund offers exposure to 500 of the \
        #                     largest U.S. companies, which span many different industries and \
        #                     account for about three-fourths of the U.S. stock market’s value. \
        #                     The key risk for the fund is the volatility that comes with its full \
        #                     exposure to the stock market. Because the 500 Index Fund is broadly \
        #                     diversified within the large-capitalization market, it may be \
        #                     considered a core equity holding in a portfolio."),
        #
        #         ], className="six columns"),
        #
        #         html.Div([
        #             html.H6(["Fund Facts"],
        #                     className="gs-header gs-table-header padded"),
        #             # html.Table(make_dash_table(df_fund_facts))
        #         ], className="six columns"),
        #
        #     ], className="row "),
        #
        #     # Row 4
        #
        #     html.Div([
        #
        #         html.Div([
        #             html.H6('Plant Autonomy in Hours',
        #                     className="gs-header gs-text-header padded"),
        #             # dcc.Graph()
        #         ], className="six columns"),
        #
        #     ], className="row ")
        #
        ], className="subpage")

    ], className="page")

