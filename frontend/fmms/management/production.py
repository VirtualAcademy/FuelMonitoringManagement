from layout import tabStack
from layout import manageMenu_page, get_production_comp
from futils import atab_value, callbackfunctions
# from api.manager import DashBoardManager
#
# f=DashBoardManager()
# print(f.get_autonomy(''))
import plotly.plotly as py


###########################
#  Constants definition   #
###########################

TAB_LIST = ['Autonomy', 'Power Plants', 'Demand', 'Power Availability', 'Production Forecast']
CURRENT_STACK = tabStack([atab_value(TAB_LIST[0].lower())], 1)
PAGE_TITLE = 'Production'
TAB_PDTCOMPONENTS = get_production_comp()
# print(TAB_PDTCOMPONENTS)



# End of Constants definition #

# Production Main Page Layout component
production =  manageMenu_page(tabstack=CURRENT_STACK,title=PAGE_TITLE,tablist=TAB_LIST)


# Call backs
callbackfunctions(title=PAGE_TITLE, returnvalues=TAB_PDTCOMPONENTS)
