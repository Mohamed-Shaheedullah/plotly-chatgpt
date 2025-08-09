import plotly.express as px
import pandas as pd

df = px.data.gapminder()
print(df.info())

fig = px.line(
    df[df['country'] == 'Canada'], 
    x="year", 
    y="lifeExp", 
#    color="continent", 
#    size="pop", 
#    hover_name="country", 
#    log_x=True, 
#    animation_frame="year"
)
fig.show()
