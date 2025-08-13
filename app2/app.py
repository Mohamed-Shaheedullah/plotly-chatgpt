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
    # title
    html.H1("Life Expectancy Dashboard", style={"textAlign": "center"}),

    # Visible Dropdown for selecting country
    dcc.Dropdown(
        id="country-dropdown",
        # list comprehension
        options=[{"label": c, "value": c} for c in countries],
        value="Canada",  # Default value
        clearable=False
    ),

    # Graph
    dcc.Graph(id="lifeexp-chart")
])

# Callback to update the chart based on dropdown selection
@app.callback(
    # identifier and property
    Output("lifeexp-chart", "figure"),
    # identifier and property
    # matches id in layout
    Input("country-dropdown", "value")
)

# number of parameters in function match number of inputs
def update_chart(selected_country):
    # filter for selected country from argument
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
    # number of objects returned matches number of outputs
    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
