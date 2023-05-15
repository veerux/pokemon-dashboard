import pandas as pd
from dash import Dash, dcc, html

df = pd.read_csv("pokemondb.csv")
print(df)
    

app = Dash(__name__)

if __name__ == "__main__":
    app.run_server(debug=True)