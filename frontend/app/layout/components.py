from layout import html, dcc, dbc, menu_list, make_menu, button_item, submenu_item


def Header(htitle='Fuel Monitoring and Management System'):
    return html.Div([
        get_header(htitle),
        html.Br([])
    ])

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


def get_header(headertitle):
    header = html.Div([

        html.Div([
            html.H5(
                headertitle)
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


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

    order = submenu_item(lid='order',ahref="/manage/supplies/delivery_order",name="Delivery Order",lclassName="gradient_menuitem gradient48 first_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_7.png",imgalt="")
    schedule = submenu_item(lid='schedule',ahref="/manage/supplies/delivery_schedule",name="Delivery Schedule",lclassName="gradient_menuitem gradient48",aclassName="with_img_32",imgsrc="mbico_mbmcp_8.png",imgalt="")
    confirmation = submenu_item(lid='confirmation',ahref="/manage/supplies/delivery_confirmation",name="Delivery Confirmation",lclassName="gradient_menuitem gradient48 last_item",aclassName="with_img_32",imgsrc="mbico_mbmcp_9.png",imgalt="")

    supplies_sub = menu_list(uid=None,uclass="gradient_menu gradient138 img_32",list_of_menu=[order,schedule,confirmation])
    supplies = submenu_item(ahref=None,sub_subitem=supplies_sub,lid='supplies',name="Supplies",lclassName="gradient_menuitem gradient40 last_item",aclassName="with_img_24 with_arrow",imgsrc="mbico_mbmcp_6.png" ,imgalt="")

    manage_sub = menu_list(uid=None,uclass="img_24",list_of_menu=[production,consumption,supplies])
    manage_btn = button_item(styling={"width":"146"},div1class="buttonbg gradient_button gradient72",div3class="arrow ",div2class="icon_4 with_img_32",btn_name="Manage",submenu=manage_sub)

    # Help

    manual = submenu_item(lid='manual', ahref="/help/manual", name="Manual", lclassName="gradient_menuitem gradient33 first_item", aclassName="with_img_16", imgsrc="mbico_mbmcp_10.png", imgalt="")

    support = submenu_item(lid='support', ahref="/help/support", name="Support", lclassName="gradient_menuitem gradient33 last_item", aclassName="with_img_16", imgsrc="mbico_mbmcp_11.png", imgalt="")

    help_sub = menu_list(uid=None,uclass="gradient_menu gradient60 img_16",list_of_menu=[manual,support])

    help_btn = button_item(lclass="last_button",styling={"width": "120"}, div1class="buttonbg gradient_button gradient72", div3class="arrow ", div2class="icon_6 with_img_24", btn_name="Help",aclass="button_6", submenu=help_sub)

    menulists = menu_list(uid="mbmcpebul_table", uclass="mbmcpebul_menulist css_menu",list_of_menu=[dashboard_btn,monitor_btn,manage_btn,settings_btn,help_btn])
    menu = make_menu(did="mbmcpebul_wrapper",dstyle={'float':'right'},menus=menulists)

    # menu = html.Div([
    #
    #     dcc.Link('Overview   ', href='/dash-vanguard-report/overview', className="tab first"),
    #
    #     dcc.Link('Price Performance   ', href='/dash-vanguard-report/price-performance', className="tab"),
    #
    #     dcc.Link('Portfolio & Management   ', href='/dash-vanguard-report/portfolio-management', className="tab"),
    #
    #     dcc.Link('Fees & Minimums   ', href='/dash-vanguard-report/fees', className="tab"),
    #
    #     dcc.Link('Distributions   ', href='/dash-vanguard-report/distributions', className="tab"),
    #
    #     dcc.Link('News & Reviews   ', href='/dash-vanguard-report/news-and-reviews', className="tab")
    #
    # ], className="row ")
    return menu

def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

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

def make_form(items=[{'label':{'name':'mylabel','classname':'control-label requiredField'},
                     'input':dict(
                             id="new_opportunity_name",
                             placeholder="Name of the opportunity",
                             type="text",
                             value="",
                             className="form-control",
                             style={"width": "100%"},
                             ),'divclass':dict(className="form-group")}]):
    return [dbc.Form([
        html.Div([
            dbc.Label([
                item['label']['name']
            ], className= item['label']['classname']),
            dcc.Input(
                    id= item['input']['id'],
                    placeholder=item['input']['placeholder'],
                    type=item['input']['type'],
                    value=item['input']['value'],
                    className=item['input']['className'],
                    style=item['input']['style'], )
        ], className=item['divclass'])
    ]) for item in items]