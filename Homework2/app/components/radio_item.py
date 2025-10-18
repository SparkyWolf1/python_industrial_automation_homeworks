import dash


def render(App: dash.Dash) -> dash.html.Div:
    return dash.html.Div(
        children=[
            dash.dcc.RadioItems(["Celá ČR", "Kraj"])
        ]
    )
