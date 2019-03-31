import plotly.graph_objs as go
import pandas as pd
from layout import dcc, html


def table_plot():
    max_rows = 10
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    # trace0 = go.Table(
    #   header = dict(
    dalues = ['DAY',
                      'MONDAY',
                      'TUESDAY',
                      'WEDNESDAY',
                      'THURSDAY']
      #   line = dict(color = '#506784'),
      #   fill = dict(color = headerColor),
      #   align = ['left','center'],
      #   font = dict(color = 'white', size = 12)
      # ),
      # cells = dict(
    dv_values = [
          ['LPP(Hrs)', 'Logbaba(Hrs)', 'Oyomabang(Hrs)', 'Ahala(Hrs)', 'TOTAL(Hrs)'],
          [1200, 20, 80, 2, 1302],
          [1300, 20, 70, 2, 1392],
          [1300, 20, 120, 2, 1442],
          [1400, 20, 90, 2, 1512]]
        # line = dict(color = '#506784'),
        # fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        # align = ['left', 'center'],
        # font = dict(color = '#506784', size = 11)
        #))

    df = pd.DataFrame(dv_values).transpose()
    dfs = pd.DataFrame(df,columns=dalues)


    # print(df,len(df))
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dfs.columns])] +

        # Body
        [html.Tr([
            html.Td(df.iloc[i][col], style={'width': '8em'}) for col in df.columns
        ]) for i in range(len(df))]
    )


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
