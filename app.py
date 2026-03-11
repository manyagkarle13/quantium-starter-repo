import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset
df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign":"center",
            "color":"#2c3e50",
            "marginBottom":"30px"
        }
    ),

    html.Div([

        html.Div([
            html.Label("Select Region"),
            dcc.Dropdown(
                id="region-filter",
                options=[
                    {"label":"All Regions","value":"all"},
                    {"label":"North","value":"north"},
                    {"label":"South","value":"south"},
                    {"label":"East","value":"east"},
                    {"label":"West","value":"west"}
                ],
                value="all",
                clearable=False
            )
        ], style={"width":"30%","display":"inline-block"}),

        html.Div([
            html.Label("Select Date Range"),
            dcc.DatePickerRange(
                id="date-filter",
                start_date=df["date"].min(),
                end_date=df["date"].max()
            )
        ], style={"width":"40%","display":"inline-block","marginLeft":"50px"})

    ], style={"marginBottom":"30px"}),

    dcc.Graph(id="sales-line-chart"),

    dcc.Graph(id="region-bar-chart")

],
style={
    "width":"80%",
    "margin":"auto",
    "fontFamily":"Arial"
})


@app.callback(
    Output("sales-line-chart","figure"),
    Output("region-bar-chart","figure"),
    Input("region-filter","value"),
    Input("date-filter","start_date"),
    Input("date-filter","end_date")
)

def update_dashboard(region,start_date,end_date):

    filtered_df = df[
        (df["date"] >= start_date) &
        (df["date"] <= end_date)
    ]

    if region != "all":
        filtered_df = filtered_df[filtered_df["region"] == region]

    sales_by_date = filtered_df.groupby("date")["sales"].sum().reset_index()

    line_chart = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title="Sales Trend Over Time"
    )

    region_sales = filtered_df.groupby("region")["sales"].sum().reset_index()

    bar_chart = px.bar(
        region_sales,
        x="region",
        y="sales",
        title="Sales by Region",
        color="region"
    )

    return line_chart, bar_chart


if __name__ == "__main__":
    app.run(debug=True)