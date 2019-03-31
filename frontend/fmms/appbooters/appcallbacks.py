from dash.dependencies import Input, Output, State
from fmms import app

def atab_value(tabtitle):
	return tabtitle.strip().replace(' ','_')

def callbackfunctions(title, returnvalues):
	# tab output render function
	title=title.lower()
	@app.callback(Output('{}-tab-output'.format(title), "children"), [Input("{}-tabs".format(title), "value")])
	def render_content(value):
		return returnvalues[value.lower()]

	# tab modal render function
	@app.callback(Output("{}-tab_modal".format(title), "style"), [Input('{}-tabs-add-btn'.format(title), "n_clicks")])
	def render_con(n_clicks):
		if n_clicks > 0:
			return {"display": "block"}
		return {"display": "none"}

	# tab modal close function
	@app.callback(
	    Output('{}-tabs-add-btn'.format(title), "n_clicks"),
	    [Input("close_{}_modal".format(title), "n_clicks"), Input("submit_new_{}".format(title), "n_clicks")],
	)
	def close_modal_callback(n, n2):
		print('close')
		return 0


# def crud_callback(title, state_values):
	# Add new function
	# @app.callback(
	#     Output("Add_new_{}".format(title), "children"),
	#     [Input("submit_new_{}".format(title), "n_clicks")],
	#     [
	#         State(l_id, 'value')
	#         for l_id in state_values
	#     ],
	# )
	# def add_new_callback(
	#     n_clicks, *values
	#     ):
	# 	value_list = values
	# 	if n_clicks > 0:
	# 		query = {
	#             state_values[i]: value_list[i],
	#             for i in range(len(value_list))
	#         }
	#       print(query)
	# 		# sf_manager.add_case(query)
	#         # df = sf_manager.get_cases()
	#         return #df.to_json(orient="split")
	#
	# 	return current_df