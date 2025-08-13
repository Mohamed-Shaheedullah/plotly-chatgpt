import plotly.express as px
import pandas as pd

# Load data
df = px.data.gapminder()

# Create a list of countries to include in dropdown
countries = ["Canada", "United States", "Mexico", "France", "Japan"]

# Create an initial figure for the first country
fig = px.line(
    df[df["country"] == countries[0]],
    x="year",
    y="lifeExp",
    markers=True,
    title=f"Life Expectancy in {countries[0]} (1952–2007)",
    labels={"year": "Year", "lifeExp": "Life Expectancy (Years)"},
    template="plotly_white"
)

# Add dropdown menu to switch countries
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label=country,
                    method="update",
                    args=[
                        {
                            "x": [df[df["country"] == country]["year"]],
                            "y": [df[df["country"] == country]["lifeExp"]],
                        },
                        {"title": f"Life Expectancy in {country} (1952–2007)"}
                    ],
                )
                for country in countries
            ],
            direction="down",
            showactive=True
        )
    ]
)

fig.show()

