import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from collections import OrderedDict
from layout.components import Header, make_dash_table, print_button, make_row
from layout.graphcomponents import Charts


def make_piechartdata(lxdata=None, ydata=None, lcolor="rgb(53, 83, 255)", line_color="rgb(25, 255, 55)", width=2,
                      name="RIN"):
    return dict(x=lxdata, y=ydata, marker={"color": lcolor, "line": {"color": line_color, "width": width}}, name=name)


g = Charts()

data1 = [['Plant Name','Autonomy Left'],[' MAROUA',59],['Djamboutou',70],['Kousseri',	5]]
columns = ['Plant Name','Autonomy Left']
data2 = [
    ['Plant Name','Autonomy Left'],
    ['Dibamba',46.42],['Limbé',48],['LBB','76'],
    ['Mbalmayo', None],['Ebolowa',None],['Oyo1', None],
    ['Ahala',15],['Bamenda', 18],['Bafoussam',54]]
df1 = pd.DataFrame(data=data1,columns=columns)
df2 = pd.DataFrame(data=data2,columns=columns)
df2.replace(to_replace=[None],value=0,inplace=True)

deliverycolumns = ['No.','Purchase date','Quantity Ordered','ETA(Estimated Arrival Date)']
deliverydata = [['No.','Purchase date','Quantity Ordered(Littres)','ETA(Estimated Arrival Date)'],
                [1,'12-01-2019',2000,'21-01-2019'],
                [1,'12-01-2019',2000,'21-01-2019'],
                [1,'12-01-2019',2000,'21-01-2019'],
                [1,'12-01-2019',2000,'21-01-2019']
                ]
deliverydf = pd.DataFrame(data=deliverydata,columns=deliverycolumns)

mapconver = lambda s:list(map(float,s))

fuelfollowcolumns = ['Date', 'Production', 'Consumption', 'Fuel Stock', 'Deliveries made', 'Pending Deliveries']
fdates = ['2016-11-02', '2016-11-03', '2016-11-04', '2016-11-05', '2016-11-06', '2016-11-07', '2016-11-08', '2016-11-09', '2016-11-10', '2016-11-11', '2016-11-12', '2016-11-13', '2016-11-14', '2016-11-15', '2016-11-16', '2016-11-17', '2016-11-18', '2016-11-19', '2016-11-20', '2016-11-21', '2016-11-22', '2016-11-23', '2016-11-24', '2016-11-25', '2016-11-26', '2016-11-27', '2016-11-28', '2016-11-29', '2016-11-30', '2016-12-01']
prod = mapconver(['160.77', '206.66', '295.42', '203.66', '208.03', '268.38', '217.41', '517.74', '592.45', '535.65', '327.67', '119.72', '158.94', '263.68', '295.46', '233.60', '375.30', '368.00', '396.48', '543.17', '425.52', '635.28', '472.21', '977.57', '1024.61', '382.11', '277.79', '812.51', '705.65', '498.60'])
consum = mapconver(['30.61', '48.15', '53.80', '36.92', '38.62', '38.04', '37.97', '97.82', '115.25', '106.04', '63.67', '20.43', '30.24', '50.66', '52.70', '45.24', '72.94', '72.56', '78.48', '112.02', '87.74', '131.63', '97.22', '201.74', '211.57', '79.30', '57.62', '168.81', '146.42', '103.33'])
fuelstock = mapconver(['768.00', '1804.00', '1462.00', '1362.00', '1298.00', '1273.00', '1206.00', '949.00', '793.00', '591.00', '1426.00', '1363.00', '1329.00', '1237.00', '1180.00', '1056.00', '950.00', '1750.00', '1585.00', '1405.00', '1330.00', '1102.00', '945.00', '614.00', '1305.00', '1140.00', '1017.00', '750.00', '535.00', '412.00'])
Dm=mapconver(['0.00', '1084.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '900.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '1200.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '900.00', '0.00', '0.00', '0.00', '0.00', '0.00'])
Pending=mapconver(['0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'])

fuelfollowdata = OrderedDict([
    ('Date',fdates), ('Production',prod), ('Consumption', consum),('Fuel Stock',fuelstock), ('Deliveries made',Dm), ('Pending Deliveries',Pending)
                ])
fuelstockdf=pd.DataFrame(fuelfollowdata,columns=fuelfollowcolumns)
fuelstockdf['Specific Consumption']=fuelstockdf['Consumption']/fuelstockdf['Production']
# print(pd.DataFrame(fuelstockdf.columns.values))
fuelstockdf =pd.concat([pd.DataFrame([fuelstockdf.columns.values],columns=fuelstockdf.columns.values),fuelstockdf],ignore_index=True)

chartinfo_fuel = [dict(
                x = fuelstockdf['Date'],
                y = fuelstockdf['Specific Consumption'],
                marker = {
                  "color": "rgb(53, 83, 255)",
                  "line": {
                    "color": "rgb(25, 255, 55)",
                    "width": 2
                  }
                },
                name = "Prod and Consumption")]

# fuelstockdf.loc[30]=fuelfollowcolumns
# print(make_piechartdata(lxdata=fuelstockdf['Date'],ydata=fuelstockdf['Specific Consumption']))
chartinfo1 = [dict(
                x = df1['Plant Name'],
                y = df1['Autonomy Left'],
                marker = {
                  "color": "rgb(53, 83, 255)",
                  "line": {
                    "color": "rgb(25, 255, 55)",
                    "width": 2
                  }
                },
                name = "RIN")]

chartinfo2 = [dict(
                x = df2['Plant Name'],
                y = df2['Autonomy Left'],
                marker = {
                  "color": "rgb(53, 83, 255)",
                  "line": {
                    "color": "rgb(25, 255, 55)",
                    "width": 2
                  }
                },
                name = "RIN")]

## Page layouts
autonomyLayout = html.Div([

        html.Div([
            html.Strong(),
        html.Div([
            html.H6(["RIN"],
                    className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df1)),
            html.H6(["RIS"],
                    className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df2)),
        ], className="eleven columns"),
        ], className="six columns"),

        html.Div([
            html.Div([
                g.makebarchart("pie-rin",chartinfo1,'Plants in RIN'),
                g.makebarchart("graph-ris",chartinfo2,'Plant in RIS')
        ], className="twelve columns"),
        ], className="six columns"),

    ], className="row ")


fuelDeliveryLayout = html.Div([

        html.Div([
            html.Strong(),
        html.Div([
            html.H6(["Delievery Schedule"],
                    className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(deliverydf)),
        ], className="eleven columns"),
        ], className="six columns"),

        html.Div([
            html.Div([
            html.H6(["Delivery Note"],
                    className="gs-header gs-table-header padded"),
                html.Br([]),
                html.P("\
        As the industry’s first index fund for individual investors, \
        the 500 Index Fund is a low-cost way to gain diversified exposure \
        to the U.S. equity market. The fund offers exposure to 500 of the \
        largest U.S. companies, which span many different industries and \
        account for about three-fourths of the U.S. stock market’s value. \
        The key risk for the fund is the volatility that comes with its full \
        exposure to the stock market. Because the 500 Index Fund is broadly \
        diversified within the large-capitalization market, it may be \
        considered a core equity holding in a portfolio."),
        ], className="twelve columns"),
        ], className="six columns"),

    ], className="row ")


fuelStatusLayout = html.Div([

        html.Div([
        html.Div([
            html.Strong(),

            g.makebarchart("pie-stock", chartinfo_fuel, 'Plants in RIN'),
        ]),
            html.H6(["Stock Variations Table"],
                    className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(fuelstockdf)),
        ], className="twelve columns padded"),

    ], className="row ")

dashboard = html.Div([  # page 1
            Header('Dashboard'),

    # Row 1

    # Row 2
    *make_row("Power Plants Autonomy",autonomyLayout),
    *make_row("Fuel Delivery",fuelDeliveryLayout),
    *make_row("Stock Variations",fuelStatusLayout),

    html.Div([
            # Row 4

            html.Div([

                html.Div([
                    html.H6('Plant Autonomy in Hours',
                            className="gs-header gs-text-header padded"),
	                g.makebarchart("graph-1",chartinfo1,'Plant')
                ], className="six columns"),

                html.Div([
                    html.H6("Hypothetical growth of $10,000",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id="grpah-2",
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                                    y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000", "19000", "20500", "24000"],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "500 Index Fund Inv"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                width = 340,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0277108433735,
                                  "y": -0.142606516291,
                                  "orientation": "h"
                                },
                                margin = {
                                  "r": 20,
                                  "t": 20,
                                  "b": 20,
                                  "l": 50
                                },
                                showlegend = True,
                                xaxis = {
                                  "autorange": True,
                                  "linecolor": "rgb(0, 0, 0)",
                                  "linewidth": 1,
                                  "range": [2008, 2018],
                                  "showgrid": False,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear"
                                },
                                yaxis = {
                                  "autorange": False,
                                  "gridcolor": "rgba(127, 127, 127, 0.2)",
                                  "mirror": False,
                                  "nticks": 4,
                                  "range": [0, 30000],
                                  "showgrid": True,
                                  "showline": True,
                                  "ticklen": 10,
                                  "ticks": "outside",
                                  "title": "$",
                                  "type": "linear",
                                  "zeroline": False,
                                  "zerolinewidth": 4
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6('Price & Performance (%)',
                            className="gs-header gs-table-header padded"),
                    # html.Table(make_dash_table(df_price_perf))
                ], className="six columns"),

                html.Div([
                    html.H6("Risk Potential",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Less risk<br>Less reward</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>More risk<br>More reward</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")

