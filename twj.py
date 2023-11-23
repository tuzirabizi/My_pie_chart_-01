from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_excel('SAS22.xlsx', sheet_name='Sheet1')



app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Main crops Gross Value Added in current prices (Value RWF per ha)', style={'textAlign':'center'}),
    dcc.Dropdown(df.columns[1:].unique(), 2016, id='dropdown-selection', style={"width": "300px"},),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    return px.pie(df, names=df.columns[0], values=value)


if __name__ == '__main__':
    app.run(debug=True)
