import plotly.express as px
from pandas import DataFrame
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import ids


def render(App: Dash, data: DataFrame) -> html.Div:
    chart = px.line(data, x="Timestamp", y=["Temperature_T0",
                                            "Temperature_J1",
                                            "Temperature_J2",
                                            "Temperature_J3",
                                            "Temperature_J4",
                                            "Temperature_J5"])
    return html.Div(
            dcc.Graph(figure=chart)
        )
