import dash


def render(App: dash.Dash, selection: list[str]) -> dash.html.Div:
    return dash.html.Div(
        children=[
            dash.dcc.Dropdown(selection)
        ]
    )
