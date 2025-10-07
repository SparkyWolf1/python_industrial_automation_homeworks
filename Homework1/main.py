# Dataset UR3 controller data from UC Irvine Machine learning repository
# url: https://archive.ics.uci.edu/dataset/963/ur3+cobotops
# dataset is licensed under a Creative Commons Attribution 4.0 International
# (CC BY 4.0) license

# CSV FILE HEADER COLLUMN NAMES
# [0] Num                       int64
# [1] Timestamp                 Time
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
# [22] Robot protective stop    Bool
# [23] grip lost                Bool

import csv
import pandas
import plotly.express
from dash import Dash, html, dash_table, dcc, callback, Output, Input

DATA_PATH = "DatasetsTesting\\Robot_Data\\dataset_02052023.csv"
USE_COLS = list(range(0, 24))

df = pandas.read_csv(
    filepath_or_buffer=DATA_PATH,
    sep=";",
    decimal=",",
    parse_dates=True,
    date_format='ISO8601',
    usecols=USE_COLS)

df.index = pandas.to_datetime(df['Timestamp'], format='ISO8601')

if __name__ == '__main__':
    print(df.dtypes)
