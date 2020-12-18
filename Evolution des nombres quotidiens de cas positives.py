import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots

time_series = pd.read_csv('sp-pos-quot-fra-2020-12-11-19h20.csv', header=0, delimiter=";")
time_series['jour'] = pd.to_datetime(time_series['jour'])


time_series_09 = time_series['cl_age90'] != 0
time_series_09 = time_series[time_series_09]

time_series_dates = time_series_09.groupby('jour').sum()


fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=time_series_dates.index, y=time_series_dates['P'], 
                           line_color='black'))
fig13.update_layout(title='Evolution des nombres quotidiens des cas positifs en France')
fig13.show()
