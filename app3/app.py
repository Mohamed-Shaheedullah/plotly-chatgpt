import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = px.data.gapminder()

# List of countries for dropdown
countries = df["country"].unique()

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Life Expectancy Dashboard", style={"textAlign": "center"}),

    # Multi-select country dropdown
    dcc.Dropdown(
        id="country-dropdown",  # see line 44
        options=[{"label": c, "value": c} for c in countries],
        value=["Canada", "United States"],  # Default
        multi=True,
        clearable=False
    ),

    # Year range slider
    dcc.RangeSlider(
        id="year-slider", # see line 45
        min=df["year"].min(),
        max=df["year"].max(),
        step=5,  # Gapminder dataset has 5-year intervals
        marks={str(year): str(year) for year in sorted(df["year"].unique())},
        value=[df["year"].min(), df["year"].max()]  # Default full range
    ),

    # Chart  see line 43
    dcc.Graph(id="lifeexp-chart")
])

# Callback for updating chart based on both inputs
@app.callback(
    Output("lifeexp-chart", "figure"),  # corresponds to chart 
    [Input("country-dropdown", "value"),  # two inputs correspond to input forms, 1. dropdown
     Input("year-slider", "value")]       # 2. corresponds to year range slider
)
def update_chart(selected_countries, selected_years):  # two parameters correspond to input forms lines 44, 45
    start_year, end_year = selected_years
    filtered_df = df[
        (df["country"].isin(selected_countries)) &
        (df["year"] >= start_year) &
        (df["year"] <= end_year)
    ]
    fig = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        color="country",
        markers=True,
        title="Life Expectancy by Country",
        labels={"year": "Year", "lifeExp": "Life Expectancy (Years)"},
        template="plotly_white"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
