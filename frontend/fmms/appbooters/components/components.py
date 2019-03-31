from layout import html, dcc, dbc, menu_list, button_item, submenu_item, make_menu
from .graphcomponents import  table_plot


#############################################
#                                           #
#  Manage Menu items page layout blue print #
#                                           #
#############################################

def manageMenu_page(tabstack, title='',tablist=[]):
    l_title = title.lower()
    return html.Div([  # page
        # Header
        Header('Manage {}'.format(title)),

        # Buttons
        html.Div([
            html.Div(className='Six columns'),
            html.Button('Add',style=dict(padding='1',width=100, background='red'),className='btn btn-info',n_clicks=0,id='{}-tabs-add-btn'.format(l_title)),
            html.Button('Edit',style=dict(padding='5',width=100, background='orange'),className='btn btn-info',n_clicks=0,id='{}-tabs-edit-btn'.format(l_title)),
            html.Button('Delete',style=dict(padding='1',width=100),className='btn btn-info',n_clicks=0,id='{}-tabs-delete-btn'.format(l_title))
        ],style=dict(marginLeft='75%'),className='row'),

        # Hidden Modal
        html.Div(
                [
                    card_compn(l_title)
                ],
                id = "{}-tab_modal".format(title.lower()),
                style={"display": "none"},
                className="modal",),

        # Tabs
        html.Div(
                [
                tabs_compn(l_title,tabstack, tablist)
                ],
                style={'width': '20%', 'float': 'left'}
        ),

        # Tab Output hook
        html.Div(
            html.Div(id='{}-tab-output'.format(l_title)),
            style={'width': '80%', 'float': 'right'}
        )
    ],
            style={
                'fontFamily': 'Sans-Serif',
                'margin-left': 'auto',
                'margin-right': 'auto',
            }
            , className="page")

# End of Manage Menu items page layout blue print #

##################
# Card Component #
##################
def card_compn(title):
    title=title.lower()
    card = dbc.Card(
            [
                dbc.CardHeader([
                                html.Span(
                                    "New Case",
                                    style={
                                        "color": "#506784",
                                        "fontWeight": "bold",
                                        "fontSize": "20",
                                    },
                                ),
                                html.Span(
                                    "×",
                                    id="close_{}_modal".format(title),
                                    n_clicks=0,
                                    style={
                                        "float": "right",
                                        "cursor": "pointer",
                                        "marginTop": "0",
                                        "marginBottom": "17",
                                    },
                                ),
                            ],
                            # className="row",
                            # style={"borderBottom": "1px solid #C8D4E3"},
                        ),
                dbc.CardBody(
                    [
                        dbc.CardTitle("Yanky Dudu"),
                        html.Div([

                            html.P(
                                    "Priority",
                                    style={
                                        "textAlign"   : "left",
                                        "marginBottom": "2",
                                        "marginTop"   : "4",
                                    },
                            ),
                            dcc.Dropdown(
                                    id="new_case_priority",
                                    options=[
                                        {"label": "High", "value": "High"},
                                        {"label": "Medium", "value": "Medium"},
                                        {"label": "Low", "value": "Low"},
                                    ],
                                    value="Medium",
                                    clearable=False,
                            ),
                        ]),
                        html.Div([
                        # submit button
                        html.Span(
                            "Submit",
                            id="submit_new_{}".format(title),
                            n_clicks=0,
                            className="button button-primary add"
                        )],
                            style={"marginTop": "10", "textAlign": "center"})
                    ],className="modal-content",
                    style={"textAlign": "center", "border": "1px solid #C8D4E3"},
                ),
                dbc.CardFooter("Footer"),
            ],
            color="primary",
            outline=True)
    return card

# End of Card Component #

##################
# Tab Component #
##################
def tabs_compn(title, current_tabstack,tablist=[]):
    if not tablist:
        return None
    first = current_tabstack[-1]+'_tab'
    print(first,'this first tab1')
    return dcc.Tabs(
                    children=[
                        dcc.Tab(label=name, value=name.strip().replace(' ','_')+'_tab')
                        for name in tablist
                    ],
                    value=first,
                    id='{}-tabs'.format(title),
                    vertical=True,
                    style={
                        'height'     : '100vh',
                        'borderRight': 'thin lightgrey solid',
                        'textAlign'  : 'left'
                    }
            )

# End of Tab Component #

###################
# Modal Component #
###################
# def modal_compn():
#
#     # contacts["Name"] = (
#     #     contacts["Salutation"]
#     #     + " "
#     #     + contacts["FirstName"]
#     #     + " "
#     #     + contacts["LastName"]
#     # )
#     return html.Div(
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         # modal header
#                         html.Div(
#                             [
#                                 html.Span(
#                                     "New Case",
#                                     style={
#                                         "color": "#506784",
#                                         "fontWeight": "bold",
#                                         "fontSize": "20",
#                                     },
#                                 ),
#                                 html.Span(
#                                     "×",
#                                     id="cases_modal_close",
#                                     n_clicks=0,
#                                     style={
#                                         "float": "right",
#                                         "cursor": "pointer",
#                                         "marginTop": "0",
#                                         "marginBottom": "17",
#                                     },
#                                 ),
#                             ],
#                             className="row",
#                             style={"borderBottom": "1px solid #C8D4E3"},
#                         ),
#
#                         # modal form
#                         html.Div(
#                             [
#
#                                 # left Div
#                                 html.Div(
#                                     [
#                                         # html.P(
#                                         #     "Account name",
#                                         #     style={
#                                         #         "textAlign": "left",
#                                         #         "marginBottom": "2",
#                                         #         "marginTop": "4",
#                                         #     },
#                                         # ),
#                                         # html.Div(
#                                         #     dcc.Dropdown(
#                                         #         id="new_case_account",
#                                         #         options=[
#                                         #             {
#                                         #                 "label": row["Name"],
#                                         #                 "value": row["Id"],
#                                         #             }
#                                         #             for index, row in accounts.iterrows()
#                                         #         ],
#                                         #         clearable=False,
#                                         #         value=accounts.iloc[0].Id,
#                                         #     )
#                                         # ),
#                                         html.P(
#                                             "Priority",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Dropdown(
#                                             id="new_case_priority",
#                                             options=[
#                                                 {"label": "High", "value": "High"},
#                                                 {"label": "Medium", "value": "Medium"},
#                                                 {"label": "Low", "value": "Low"},
#                                             ],
#                                             value="Medium",
#                                             clearable=False,
#                                         ),
#                                         html.P(
#                                             "Origin",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Dropdown(
#                                             id="new_case_origin",
#                                             options=[
#                                                 {"label": "Phone", "value": "Phone"},
#                                                 {"label": "Web", "value": "Web"},
#                                                 {"label": "Email", "value": "Email"},
#                                             ],
#                                             value="Phone",
#                                             clearable=False,
#                                         ),
#                                         html.P(
#                                             "Reason",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Dropdown(
#                                             id="new_case_reason",
#                                             options=[
#                                                 {
#                                                     "label": "Installation",
#                                                     "value": "Installation",
#                                                 },
#                                                 {
#                                                     "label": "Equipment Complexity",
#                                                     "value": "Equipment Complexity",
#                                                 },
#                                                 {
#                                                     "label": "Performance",
#                                                     "value": "Performance",
#                                                 },
#                                                 {
#                                                     "label": "Breakdown",
#                                                     "value": "Breakdown",
#                                                 },
#                                                 {
#                                                     "label": "Equipment Design",
#                                                     "value": "Equipment Design",
#                                                 },
#                                                 {
#                                                     "label": "Feedback",
#                                                     "value": "Feedback",
#                                                 },
#                                                 {"label": "Other", "value": "Other"},
#                                             ],
#                                             value="Installation",
#                                             clearable=False,
#                                         ),
#                                         html.P(
#                                             "Subject",
#                                             style={
#                                                 "float": "left",
#                                                 "marginTop": "4",
#                                                 "marginBottom": "2",
#                                             },
#                                             className="row",
#                                         ),
#                                         dcc.Input(
#                                             id="new_case_subject",
#                                             placeholder="The Subject of the case",
#                                             type="text",
#                                             value="",
#                                             style={"width": "100%"},
#                                         ),
#                                     ],
#                                     className="six columns",
#                                     style={"paddingRight": "15"},
#                                 ),
#
#
#                                 # right Div
#                                 html.Div(
#                                     [
#                                         # html.P(
#                                         #     "Contact name",
#                                         #     style={
#                                         #         "textAlign": "left",
#                                         #         "marginBottom": "2",
#                                         #         "marginTop": "4",
#                                         #     },
#                                         # ),
#                                         # html.Div(
#                                         #     dcc.Dropdown(
#                                         #         id="new_case_contact",
#                                         #         options=[
#                                         #             {
#                                         #                 "label": row["Name"],
#                                         #                 "value": row["Id"],
#                                         #             }
#                                         #             for index, row in contacts.iterrows()
#                                         #         ],
#                                         #         clearable=False,
#                                         #         value=contacts.iloc[0].Id,
#                                         #     )
#                                         # ),
#                                         html.P(
#                                             "Type",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Dropdown(
#                                             id="new_case_type",
#                                             options=[
#                                                 {
#                                                     "label": "Electrical",
#                                                     "value": "Electrical",
#                                                 },
#                                                 {
#                                                     "label": "Mechanical",
#                                                     "value": "Mechanical",
#                                                 },
#                                                 {
#                                                     "label": "Electronic",
#                                                     "value": "Electronic",
#                                                 },
#                                                 {
#                                                     "label": "Structural",
#                                                     "value": "Structural",
#                                                 },
#                                                 {"label": "Other", "value": "Other"},
#                                             ],
#                                             value="Electrical",
#                                         ),
#                                         html.P(
#                                             "Status",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Dropdown(
#                                             id="new_case_status",
#                                             options=[
#                                                 {"label": "New", "value": "New"},
#                                                 {
#                                                     "label": "Working",
#                                                     "value": "Working",
#                                                 },
#                                                 {
#                                                     "label": "Escalated",
#                                                     "value": "Escalated",
#                                                 },
#                                                 {"label": "Closed", "value": "Closed"},
#                                             ],
#                                             value="New",
#                                         ),
#                                         html.P(
#                                             "Supplied Email",
#                                             style={
#                                                 "textAlign": "left",
#                                                 "marginBottom": "2",
#                                                 "marginTop": "4",
#                                             },
#                                         ),
#                                         dcc.Input(
#                                             id="new_case_email",
#                                             placeholder="email",
#                                             type="email",
#                                             value="",
#                                             style={"width": "100%"},
#                                         ),
#                                         html.P(
#                                             "Description",
#                                             style={
#                                                 "float": "left",
#                                                 "marginTop": "4",
#                                                 "marginBottom": "2",
#                                             },
#                                             className="row",
#                                         ),
#                                         dcc.Textarea(
#                                             id="new_case_description",
#                                             placeholder="Description of the case",
#                                             value="",
#                                             style={"width": "100%"},
#                                         ),
#                                     ],
#                                     className="six columns",
#                                     style={"paddingLeft": "15"},
#                                 ),
#                             ],
#                             style={"marginTop": "10", "textAlign": "center"},
#                             className="row",
#                         ),
#
#                         # submit button
#                         html.Span(
#                             "Submit",
#                             id="submit_new_case",
#                             n_clicks=0,
#                             className="button button--primary add"
#                         ),
#
#                     ],
#                     className="modal-content",
#                     style={"textAlign": "center", "border": "1px solid #C8D4E3"},
#                 )
#             ],
#             className="modal",
#         ),
#         id="tab_modal",
#         style={"display": "none"},
#     )
#
#     return

# End of Modal Component #

####################
# Header Component #
####################
def Header(htitle='Fuel Monitoring and Management System'):
    return html.Div([
        get_header(htitle),
        html.Br([])
    ])

# End of Header Component #

###########################
# logo Component function #
###########################
def get_logo():
    logo = html.Div([

        html.Div([
            html.Div([
                html.A([html.Img(id='a2',src='/assets/images/fmmslogo.png', height='60', width='60')],
                       href='/'),
                # html.Br(),
                html.A([html.Img(id='a1',src='/assets/images/logo.png', height='50', width='160')],href='/'),
            ]),
        ], className="three columns padded",style={'marginBottom':'5%','height':100,'width':80}),

        html.Div([
            get_menu()
        ], className="nine columns padded"),


    ],id='da1', className="row gs-header")
    return logo

# End of logo Component #

###########################
# header Component function #
###########################
def get_header(headertitle):
    header = html.Div([

        html.Div([
            html.H5(
                headertitle)
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header

# End of header Component function #

###########################
# menu Component function #
###########################
def get_menu():

    # home_btn = button_item(styling={"width": "59"},lclass="first_button", ahref="/",div1class="buttonbg gradient_button gradient72", div2class="icon_1 with_img_16", aclass="button_1",btn_name='Home')

    dashboard_btn = button_item(ahref="/Dashboard",div1class="buttonbg gradient_button gradient72", styling={"width": "130"},div2class="icon_2 with_img_16",aclass="button_2", btn_name="Dashboard")

    settings_btn = button_item(styling={"width": "125"}, ahref="/Settings",div1class="buttonbg gradient_button gradient72", div2class="icon_5 with_img_24", aclass="button_5",btn_name='Settings')

    # Monitor button

    overview = submenu_item(lid='overview',ahref="/Monitoring",name="Overview",lclassName="gradient_menuitem gradient48 first_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_1.png",imgalt="")
    rin = submenu_item(lid='rin',ahref="/monitor/rin",name="RIN",lclassName="gradient_menuitem gradient48",aclassName="with_img_32",imgsrc="mbico_mbmcp_2.png",imgalt="")
    ris = submenu_item(lid='ris',ahref="/monitor/ris",name="RIS",lclassName="gradient_menuitem gradient48 last_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_3.png",imgalt="")
    monitor_sub = menu_list(uid=None,uclass="gradient_menu gradient153 img_32",list_of_menu=[overview,rin,ris,])

    monitor_btn = button_item(div1class="buttonbg gradient_button gradient72",styling={"width": "145"},div3class="arrow ",div2class="icon_3 with_img_32",btn_name="Monitor",submenu=monitor_sub)

    # Manage button

    consumption = submenu_item(lid='consumption',ahref="/manage/consumption",name="Consumption",lclassName="gradient_menuitem gradient40 first_item",aclassName="with_img_24",imgsrc="mbico_mbmcp_4.png",imgalt="")
    production = submenu_item(lid='production',ahref="/manage/production",name="Production",lclassName="gradient_menuitem gradient40",aclassName="with_img_24",imgsrc="mbico_mbmcp_5.png",imgalt="")

    # supplies

    # order = submenu_item(lid='order',ahref="/manage/supplies/delivery_order",name="Delivery Order",lclassName="gradient_menuitem gradient48 first_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_7.png",imgalt="")
    # schedule = submenu_item(lid='schedule',ahref="/manage/supplies/delivery_schedule",name="Delivery Schedule",lclassName="gradient_menuitem gradient48",aclassName="with_img_32",imgsrc="mbico_mbmcp_8.png",imgalt="")
    # confirmation = submenu_item(lid='confirmation',ahref="/manage/supplies/delivery_confirmation",name="Delivery Confirmation",lclassName="gradient_menuitem gradient48 last_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_9.png",imgalt="")

    # supplies_sub = menu_list(uid=None,uclass="gradient_menu gradient138 img_32",list_of_menu=[order,schedule,confirmation])
    supplies = submenu_item(ahref="/manage/supplies",lid='supplies',name="Supplies",lclassName="gradient_menuitem gradient40 last_item",aclassName="with_img_24 with_arrow",imgsrc="mbico_mbmcp_6.png" ,imgalt="")

    manage_sub = menu_list(uid=None,uclass="img_24",list_of_menu=[production,consumption,supplies])
    manage_btn = button_item(styling={"width":"146"},div1class="buttonbg gradient_button gradient72",div3class="arrow ",div2class="icon_4 with_img_32",btn_name="Manage",submenu=manage_sub)

    # Help

    manual = submenu_item(lid='manual', ahref="/help/manual", name="Manual", lclassName="gradient_menuitem gradient33 first_item", aclassName="with_img_16", imgsrc="mbico_mbmcp_10.png", imgalt="")

    support = submenu_item(lid='support', ahref="/help/support", name="Support", lclassName="gradient_menuitem gradient33 last_item", aclassName="with_img_16", imgsrc="mbico_mbmcp_11.png", imgalt="")

    help_sub = menu_list(uid=None,uclass="gradient_menu gradient60 img_16",list_of_menu=[manual,support])

    help_btn = button_item(lclass="last_button",styling={"width": "120"}, div1class="buttonbg gradient_button gradient72", div3class="arrow ", div2class="icon_6 with_img_24", btn_name="Help",aclass="button_6", submenu=help_sub)

    menulists = menu_list(uid="mbmcpebul_table", uclass="mbmcpebul_menulist css_menu",list_of_menu=[dashboard_btn,monitor_btn,manage_btn,settings_btn,help_btn])
    menu = make_menu(did="mbmcpebul_wrapper",dstyle={'float':'right'},menus=menulists)

    return menu

# End of menu Component function #

###########################
# dash table Component function #
###########################
def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

# End of dash table Component function #

############################
# other Component function #
############################
def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

def make_row(headertitle,layoutview):
    return [html.Div([

        html.Div([
            html.H6([headertitle],
                    className="gs-header gs-table-header padded")
        ], className="twelve columns"),

    ], className="row "),layoutview]

# def make_form(items=[{'label':{'name':'mylabel','classname':'control-label requiredField'},
#                      'input':dict(
#                              id="new_opportunity_name",
#                              placeholder="Name of the opportunity",
#                              type="text",
#                              value="",
#                              className="form-control",
#                              style={"width": "100%"},
#                              ),'divclass':dict(className="form-group")}]):
#     return [dbc.Form([
#         html.Div([
#             dbc.Label([
#                 item['label']['name']
#             ], className= item['label']['classname']),
#             dcc.Input(
#                     id= item['input']['id'],
#                     placeholder=item['input']['placeholder'],
#                     type=item['input']['type'],
#                     value=item['input']['value'],
#                     className=item['input']['className'],
#                     style=item['input']['style'], )
#         ], className=item['divclass'])
#     ]) for item in items]


"""
#########################################################
#####                                               #####
    ####                                         ####
        #  Page Layout Components definition    #
    ####                                         ####
#####                                               #####
#########################W###############################
"""

"""
#**************************************************#
 #****  Delivery Page Layout Components definition ********#
#**************************************************#
"""
# Tab content components
def get_delivery_comp():
    return dict(
    # Delivery order tab component
    delivery_order_tab =  html.Div([  # page 1
              #  Header('Delivery Order'),

        # Row 1
    ], className=""),

    # Delivery schedule tab component
    delivery_schedule_tab =  html.Div([  # page 1
               # Header('Delivery Schedule'),

        # Row 1
    ], className=""),

    # Delivery confirmation tab component
    delivery_confirmation_tab =  html.Div([  # page 1
               # Header('Delivery Confirmation'),

        # Row 1
    ], className="")
    )


"""
#**************************************************#
 #****  Production Page Layout Components definition ********#
#**************************************************#
"""
# Tab content components
def get_production_comp():
    return dict(
        autonomy_tab=html.Div([
    html.H4('Plant Autonomy'),
    table_plot(),
        ]),
    # Delivery order tab component
    demand_tab=html.Div("this demand"),

    # Delivery schedule tab component
    power_plants_tab=html.Div('Power Plant'),

    # Delivery confirmation tab component
    power_availability_tab=html.Div("this is Power avail"),

    # Delivery confirmation tab component
    production_forecast_tab=html.Div("this is Production forecast")
    )


"""
#**************************************************#
 #****  Supply Page Layout Components definition ********#
#**************************************************#
"""
# Tab content components
def get_supply_comp():
    return dict(
    # Delivery order tab component
    delivery_order_tab =  html.Div([  # page 1
                Header('Delivery Order'),

        # Row 1
    ], className="eleven columns"),

    # Delivery schedule tab component
    delivery_schedule_tab =  html.Div([  # page 1
                Header('Delivery Schedule'),

        # Row 1
    ], className="eleven columns"),

    # Delivery confirmation tab component
    delivery_confirmation_tab =  html.Div([  # page 1
                Header('Delivery Confirmation'),

        # Row 1
    ], className="eleven columns")
    )

def get_consumption_comp():
    pass