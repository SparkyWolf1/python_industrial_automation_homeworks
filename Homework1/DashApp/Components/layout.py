from dash import Dash, html
from pandas import DataFrame
from . import dropdown
from . import chart
from . import chart_line
from . import data_table


def create_layout(app: Dash, Data: DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.H2("Working example with included plotly dataset"),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app),
                    chart.render(app)
                ]
            ),
            html.Hr(),
            html.H2("Not so working for now example with my dataset"),
            html.Div(
                className="real-data-container",
                children=[
                    data_table.render(app, Data),
                    chart_line.render(app, Data)
                ]
            )
        ]
    )
