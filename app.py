import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

data = pd.read_csv("pokemondb.csv")

app = Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1(children="Pokemon analytics"),
        html.P(children=
            "tadaa"
        ),
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)