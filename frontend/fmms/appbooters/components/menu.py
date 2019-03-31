from layout import html, dcc
import settings

image_url = settings.IMAGE_URL

def submenu_item(lid,lclassName,aclassName,imgsrc,imgalt,name,ahref=None,sub_subitem=None):
	return html.Li([
		html.A([
			html.Img(src=image_url+imgsrc, alt=imgalt),name
		],href=ahref,className=aclassName),
		sub_subitem
	],id=lid,title="",className=lclassName)

def button_item(div1class,div2class,btn_name,aclass=None,styling=None,div3class=None,submenu=None,lclass=None,ahref=None):
	if not submenu:
		btn = html.Div([
			html.Div([
				dcc.Link(btn_name,className=aclass,href=ahref)
			],className=div2class)
		],className=div1class,style=styling)

		return html.Li([btn],className=lclass)
	else:
		btn = html.Div([
			html.Div([
				html.Div([
					dcc.Link(btn_name,className=aclass,href=ahref)
				],className=div3class)
			],className=div2class)
		],className=div1class,style=styling)

		return html.Li([btn,submenu],className=lclass)


def seperator():
	return html.Li(html.Div(),className="separator" )

def menu_list(uid,uclass,list_of_menu):
	return html.Ul(list_of_menu,id=uid,className=uclass)

def make_menu(did,dstyle,menus):
	return html.Div(menus,id=did,style=dstyle)
