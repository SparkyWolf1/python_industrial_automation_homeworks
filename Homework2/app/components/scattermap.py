"""Scatter map component."""
# import third party modules
import plotly.express
import plotly
import dash
import pandas

# import custom modules
# from . import ids


def render(App: dash.Dash, data) -> dash.html.Div:
    """Renders the scatter map component."""
    print_data = pandas.DataFrame(data)
    map_chart = plotly.express.scatter_map(
        data_frame=print_data,
        lon="longtitude",
        lat="latitude",
        height=500,
        width=700,
        zoom=6,
        hover_name="name",
        size=([2]*len(print_data)),
        hover_data=(
            "temperature",
            "humidity",
            "wind_speed"
        )
    )
    map_chart.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        hoverlabel=dict(
            bgcolor="white",
            font_size=14
        )

    )
    return dash.html.Div(
        dash.dcc.Graph(figure=map_chart),
        # id=ids.scattermap_id
        )
