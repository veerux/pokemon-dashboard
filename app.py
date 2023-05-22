import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Load the data from the CSV file

df = pd.read_csv("pokemondb.csv")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Pokemon Scatter Plot"),
    html.Div([
        html.Label("Type 1:"),
        dcc.Dropdown(
            id='type1-dropdown',
            options=[{'label': t, 'value': t} for t in df['Type 1'].unique()],
            value='Grass'
        )
    ]),
    dcc.Graph(id='scatter-plot')
])

# Define the callback function to update the scatter plot based on the dropdown selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('type1-dropdown', 'value')]
)
def update_scatter_plot(type1):
    filtered_df = df[df['Type 1'] == type1]
    fig = px.scatter(filtered_df, x='Type 1', y='Total', color='Legendary', title=f"Scatter Plot for {type1}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
