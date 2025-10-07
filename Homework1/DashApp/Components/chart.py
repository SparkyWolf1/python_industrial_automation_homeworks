import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import ids

TEST_DATA = px.data.medals_long()


def render(App: Dash) -> html.Div:
    @App.callback(
        Output(ids.CHART_ID, "children"),
        Input(ids.DATA_DROPDOWN, "value")
    )
    def update_chart(data: list[str]) -> html.Div:
        filtered_data = TEST_DATA.query("nation in @data")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")
        chart = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(
            dcc.Graph(figure=chart),
            id=ids.CHART_ID
        )
    return html.Div(
        id=ids.CHART_ID
    )
