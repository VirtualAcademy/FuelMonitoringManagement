from layout import tabStack
from layout import manageMenu_page, get_supply_comp
from futils import atab_value, callbackfunctions
from application import app


###########################
#  Constants definition   #
###########################

TAB_LIST = ['Delivery Schedule', 'Delivery Order', 'Delivery Confirmation']
CURRENT_STACK = tabStack([atab_value(TAB_LIST[0].lower())], 1)
PAGE_TITLE = 'Supply'
TAB_SCOMPONENTS = get_supply_comp()



# End of Constants definition #

# Main Page Layout component
supply =  manageMenu_page(tabstack=CURRENT_STACK,title=PAGE_TITLE,tablist=TAB_LIST)


# Call backs
callbackfunctions(title=PAGE_TITLE, returnvalues=TAB_SCOMPONENTS)