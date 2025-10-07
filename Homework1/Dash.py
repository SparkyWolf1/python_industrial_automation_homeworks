# Dataset UR3 controller data from UC Irvine Machine learning repository
# url: https://archive.ics.uci.edu/dataset/963/ur3+cobotops
# dataset is licensed under a Creative Commons Attribution 4.0 International
# (CC BY 4.0) license

# CSV FILE HEADER COLLUMN NAMES
# [0] Num                       int64
# [1] Timestamp                 datetime64
# [2] Current J0                float64
# [3] Temperature J0            float64
# [4] Current J1                float64
# [5] Temperature J1            float64
# [6] Current J2                float64
# [7] Temperature J2            float64
# [8] Current J3                float64
# [9] Temperature J3            float64
# [10] Current J4               float64
# [11] Temperature J4           float64
# [12] Current J5               float64
# [13] Temperature J5           float64
# [14] Speed J0                 float64
# [15] Speed J1                 float64
# [16] Speed J2                 float64
# [17] Speed J3                 float64
# [18] Speed J4                 float64
# [19] Speed J5                 float64
# [20] Tool current             float64
# [21] Cycle                    int64
# [22] Robot protective stop    bool
# [23] grip lost                bool

import pandas
import plotly.express
from dash import Dash, html, dcc, callback, Output, Input

# Create program constants
DATA_PATH = "DatasetsTesting\\Robot_Data\\dataset_02052023.csv"
USE_COLS = list(range(0, 22))
COLUMN_NAMES = ['Number', 'Timepstamp', 'Current J0',
                'Temperature J0', 'Current J1', 'Temperature J1',
                'Current J2', 'Temperature J2', 'Current J3',
                'Temperature J3', 'Current J4', 'Temperature J4',
                'Current J5', 'Temperature J5', 'Speed J1',
                'Speed J2', 'Speed J3', 'Speed J4',
                'Speed J5', 'Tool current', 'Cycle',
                'Robot protective stop', 'Grip lost']
DATE_FORMAT = 'ISO8601'


# specifiy data types
header_data = dict.fromkeys(COLUMN_NAMES, 'float64')
header_data.update({'Number': 'int64'})
header_data.update({'Cycle': 'int64'})
# header_data.update({'Timestamp': 'datetime64'})
header_data.update({'Grip lost': 'bool'})
header_data.update({'Robot protective stop': 'bool'})

# specify parsing dates
parse_dates = True

# read out csv file
df = pandas.read_csv(
    filepath_or_buffer=DATA_PATH,
    sep=";",
    decimal=",",
    parse_dates=parse_dates,
    date_format=DATE_FORMAT,
    usecols=USE_COLS,
    dtype=header_data)
df.index = pandas.to_datetime(df['Timestamp'], format='ISO8601')

plot_frame = df[['Timestamp', 'Temperature_T0', 'Temperature_J1']].copy()

# plot parameters
plot_title = 'Joint temperatures in time'
x_label = 'Timestamp'
y_label = 'Joint temperatures [°C]'

# create plot
fig = plotly.express.line(data_frame=plot_frame,
                          title=plot_title,
                          animation_frame='Temperature_T0',
                          labels={'x': x_label,
                                  'y': y_label})

# create dash app
app = Dash()
app.layout = [
    html.Div(
        dcc.Graph(figure=fig)
    )
]

if __name__ == '__main__':
    app.run()
