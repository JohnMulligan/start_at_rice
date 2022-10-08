import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from datetime import date
import numpy as np
import pandas as pd
import json
import re

####### INTITIALIZE THE APP & LOAD THE DATA #######

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
application = app.server
#server = app.server
df=pd.read_csv('Excess_Mortality_Estimates.csv')

####### PRELIM FORMATTING AND FILTERING #######


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

####### Categorical Selectors #######

outcomes=pd.unique(df['Outcome'])
states=pd.unique(df['State'])
states.sort()

####### APP PAGE LAYOUT #######

## We use Dash Bootstrap Components below.
## Documentation: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

## Main app layout
app.layout = dbc.Container(
	[
		dbc.Row(
			[
				dbc.Col(
					html.Div(
						[
						dcc.RadioItems(
							outcomes,
							outcomes[0],
							inline=False,
							id='outcomes_radio',
						)
						]
					)
				),
				dbc.Col(
					html.Div(
						[
						dcc.Dropdown(
							id="state_selector",
							options=states,
							value=states[0]
						)
						]
					)
				)
			]
		),
		dbc.Row(
			html.Div(
				[
					dcc.Graph(id="graph")
				],
			)
		)
	]
)

####### CALLBACKS (Interactivity) #######

@app.callback(
    Output('graph', 'figure'),
	Input('state_selector', 'value'),
	Input('outcomes_radio','value')
)
def line_graph(selected_state,outcome):
	
	## FILTER ON OUTCOME & STATE
	filtered=df[df['Outcome']==outcome]
	filtered=filtered[filtered['State']==selected_state]
	
	filtered['Alarm']=filtered['Exceeds Threshold'].map({True:"X",False:None})
	
	alarmlabels=filtered["Alarm"]
	
	fig=go.Figure()
	fig.add_trace(go.Scatter(
		x=filtered["Week Ending Date"],
		y=filtered["Average Expected Count"],
		name="Average Expected Count",
		mode="lines",
		stackgroup="one",
		line_shape="spline"
	))

	fig.add_trace(go.Scatter(
		x=filtered["Week Ending Date"],
		y=filtered["Excess Estimate"],
		name="Excess Estimate",
		mode="lines+text",
		stackgroup="one",
		line_shape="spline",
		text=alarmlabels,
		textposition="top center"
	))
	
	fig.update_layout(title="Weekly Excess Mortality (%s) in %s" %(outcome,selected_state))
	
	return(fig)

if __name__ == '__main__':
	application.run(debug=True, port=8080)