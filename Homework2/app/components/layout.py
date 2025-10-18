# import third party modules
import dash

# import custom moduels
from components import (
    dropdown,
    radio_item,
    scattermap,
)
import data.shared_data as shared_data
# from . import ids


def create_layout(App: dash.Dash, data: dict | None) -> dash.html.Div:
    return dash.html.Div(
        className="app-div",
        children=[
            dash.html.Div(
                className="head-bar",
                children=[
                    dash.html.Img(src='/assets/Images/WeatherLogo.svg'),
                    dash.html.H1(App.title),
                ]
            ),
            dash.html.Div(
                className="main-container",
                children=[
                    dash.html.Div(
                        className="left-panel",
                        children=[
                            dash.html.P("Zobrazení teplot:"),
                            radio_item.render(App),
                            dropdown.render(App, list(shared_data.regions))
                        ]
                    ),
                    scattermap.render(App, shared_data.graphing_data)
                ]
            )
        ]
    )
