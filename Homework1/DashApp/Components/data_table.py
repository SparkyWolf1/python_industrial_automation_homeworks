from dash import Dash, html, dash_table
from pandas import DataFrame


def render(App: Dash, Data: DataFrame) -> html.Div:
    return html.Div(
        children=[
            dash_table.DataTable(
                data=Data.to_dict("records"),
                columns=[{"name": i, "id": i} for i in Data.columns],
                page_size=20)
        ]
    )
