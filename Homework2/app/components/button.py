import dash
from components import ids
import data.shared_data as shared_data
import pandas
import pathlib

CSV_PATH = (pathlib.Path.cwd()
            / "Homework2"
            / "Current_Temperatures.csv"
            )


def render(app: dash.Dash, title: str) -> dash.html.Div:

    @dash.callback(
        dash.Input(ids.csv_button_id, "n_clicks")
    )
    def update_output(n_clicks):
        export_data = pandas.DataFrame(
            shared_data.graphing_data).to_csv(
                CSV_PATH
            )

    return dash.html.Div(
        children=[
            dash.html.Button(
                title,
                id=ids.csv_button_id,
                n_clicks=0
            )
        ]
    )
