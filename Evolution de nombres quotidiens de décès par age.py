import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots


time_series = pd.read_csv('donnees-hospitalieres-classe-age-covid19-2020-12-14-19h03.csv', header=0, delimiter=";")
time_series['jour'] = pd.to_datetime(time_series['jour'])

time_series_09 = time_series['cl_age90'] == 9
time_series_09 = time_series[time_series_09]

time_series_19 = time_series['cl_age90'] == 19
time_series_19 = time_series[time_series_19]

time_series_29 = time_series['cl_age90'] == 29
time_series_29 = time_series[time_series_29]

time_series_39 = time_series['cl_age90'] == 39
time_series_39 = time_series[time_series_39]

time_series_49 = time_series['cl_age90'] == 49
time_series_49 = time_series[time_series_49]

time_series_59 = time_series['cl_age90'] == 59
time_series_59 = time_series[time_series_59]

time_series_69 = time_series['cl_age90'] == 69
time_series_69 = time_series[time_series_69]

time_series_79 = time_series['cl_age90'] == 79
time_series_79 = time_series[time_series_79]

time_series_89 = time_series['cl_age90'] == 89
time_series_89 = time_series[time_series_89]

time_series_90 = time_series['cl_age90'] == 90
time_series_90 = time_series[time_series_90]

time_series_0 = time_series['cl_age90'] == 0
time_series_0 = time_series[time_series_0]


time_series_dates9 = time_series_09.groupby('jour').sum()
time_series_dc9 = time_series_dates9['dc']

time_series_dates19 = time_series_19.groupby('jour').sum()
time_series_dc19 = time_series_dates19['dc']

time_series_dates29 = time_series_29.groupby('jour').sum()
time_series_dc29 = time_series_dates29['dc']

time_series_dates39 = time_series_39.groupby('jour').sum()
time_series_dc39 = time_series_dates39['dc']

time_series_dates49 = time_series_49.groupby('jour').sum()
time_series_dc49 = time_series_dates49['dc']

time_series_dates59 = time_series_59.groupby('jour').sum()
time_series_dc59 = time_series_dates59['dc']

time_series_dates69 = time_series_69.groupby('jour').sum()
time_series_dc69 = time_series_dates69['dc']

time_series_dates79 = time_series_79.groupby('jour').sum()
time_series_dc79 = time_series_dates79['dc']

time_series_dates89 = time_series_89.groupby('jour').sum()
time_series_dc89 = time_series_dates89['dc']

time_series_dates90= time_series_90.groupby('jour').sum()
time_series_dc90 = time_series_dates90['dc']

time_series_dates0 = time_series_0.groupby('jour').sum()
time_series_dc0 = time_series_dates0['dc']


fig13 = go.Figure()
fig13.add_trace(go.Line(x=time_series_dates9.index, y=time_series_dc9, name='0-9'))
fig13.add_trace(go.Line(x=time_series_dates19.index, y=time_series_dc19, name='10-19'))
fig13.add_trace(go.Line(x=time_series_dates29.index, y=time_series_dc29, name='20-29'))
fig13.add_trace(go.Line(x=time_series_dates39.index, y=time_series_dc39, name='30-39'))
fig13.add_trace(go.Line(x=time_series_dates49.index, y=time_series_dc49, name='40-49'))
fig13.add_trace(go.Line(x=time_series_dates59.index, y=time_series_dc59, name='50-59'))
fig13.add_trace(go.Line(x=time_series_dates69.index, y=time_series_dc69, name='60-69'))
fig13.add_trace(go.Line(x=time_series_dates79.index, y=time_series_dc79, name='70-79'))
fig13.add_trace(go.Line(x=time_series_dates89.index, y=time_series_dc89, name='80-89'))
fig13.add_trace(go.Line(x=time_series_dates90.index, y=time_series_dc90, name='+90'))

fig13.update_layout(title='Evolution de nombres cumuler de décès par classe d’âge')
fig13.show()
