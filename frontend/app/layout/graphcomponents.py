import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd

class Charts(object):
	def __init__(self):
		# Create global chart template

		self.layout = dict(
				autosize=True,
				height=340,
				width = 480,
				font=dict(color='orange'),
				titlefont=dict(color='#CCCCCC', size='14'),
				margin=dict(
						l=35,
						r=35,
						b=35,
						t=45
				),
				hovermode="closest",
				plot_bgcolor="white",
				paper_bgcolor="white",
				legend=dict(font=dict(size=10), orientation='h'),
				title='',
		)

	def makebarchart(self,graph_id,chartinfo, charttitle=''):
		self.layout['title']=charttitle
		return dcc.Graph(
				id=graph_id,
				figure={
					'data'  : [
						go.Bar(
								x=kwargs['x'],
								y=kwargs['y'],
								marker=kwargs['marker'],
								name=kwargs['name']
						)
						for kwargs in chartinfo
				],
					'layout': self.layout
				},
				config={
					'displayModeBar': False
				}
		)

	def makebarchart(self,graph_id,chartinfo, charttitle=''):
		self.layout['title']=charttitle
		return dcc.Graph(
				id=graph_id,
				figure={
					'data'  : [
						go.Bar(
								x=kwargs['x'],
								y=kwargs['y'],
								marker=kwargs['marker'],
								name=kwargs['name']
						)
						for kwargs in chartinfo
				],
					'layout': self.layout
				},
				config={
					'displayModeBar': False
				}
		)
