from layout import tabStack
from futils import atab_value, callbackfunctions
from layout import tabStack,manageMenu_page, get_consumption_comp
from layout.components import Header, make_dash_table, print_button, make_row,manageMenu_page
from application import app


###########################
#  Constants definition   #
###########################

TAB_LIST = ['Delivery Schedule', 'Delivery Order', 'Delivery Confirmation']
CURRENT_STACK = tabStack([atab_value(TAB_LIST[0].lower())], 1)
PAGE_TITLE = 'Consumption'
TAB_CONCOMPONENTS = get_consumption_comp()


# End of Constants definition #

consumption = manageMenu_page(tabstack=CURRENT_STACK,title=PAGE_TITLE,tablist=TAB_CONCOMPONENTS)