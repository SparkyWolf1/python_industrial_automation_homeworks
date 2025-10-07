from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids


def render(App: Dash) -> html.Div:
    all_data = ["Canada", "China", "South Korea"]

    @App.callback(
        Output(ids.DATA_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_DATA, "n_clicks"),
    )
    def select_all_data(_: int) -> list[str]:
        return all_data

    return html.Div(
        children=[
            html.H6("Data"),
            dcc.Dropdown(
                id=ids.DATA_DROPDOWN,
                options=[{"label": data, "value": data} for data in all_data],
                value=all_data,
                multi=True
                ),
            html.Button(
                className="dropdown-button",
                children=["Select ALL"],
                id=ids.SELECT_ALL_DATA
            )
        ]
        
    )
