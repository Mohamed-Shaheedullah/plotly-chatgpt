# dash one selectable country

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = px.data.gapminder()

# List of countries
countries = ["Canada", "United States", "Mexico", "France", "Japan"]

# Create Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Life Expectancy Dashboard", style={"textAlign": "center"}),

    # Dropdown for selecting country
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada",  # Default value
        clearable=False
    ),

    # Graph
    dcc.Graph(id="lifeexp-chart")
])

# Callback to update the chart based on dropdown selection
@app.callback(
    Output("lifeexp-chart", "figure"),
    Input("country-dropdown", "value")
)
def update_chart(selected_country):
    filtered_df = df[df["country"] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        markers=True,
        title=f"Life Expectancy in {selected_country} (1952–2007)",
        labels={"year": "Year", "lifeExp": "Life Expectancy (Years)"},
        template="plotly_white"
    )
    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
