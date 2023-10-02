import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Dropdown(
        id='drop-1',
        options=[
            {'label': 'Polska', 'value': 'PL'},
            {'label': 'Niemcy', 'value': 'GER'}
        ],
        value='PL'
    ),

    dcc.Graph(
        id='graph-1'
    )
])