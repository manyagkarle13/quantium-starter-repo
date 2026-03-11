import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# load processed data
df = pd.read_csv("processed_sales.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# group sales by date
df = df.groupby("date").sum().reset_index()

# create line chart
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

# create dash app
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Soul Foods Sales Dashboard", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)