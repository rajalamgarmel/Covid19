import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots


time_series = pd.read_csv('sp-pos-quot-fra-2020-12-11-19h20.csv', header=0, delimiter=";")

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


fig13 = go.Figure()
fig13.add_trace(go.Line(x=time_series_09['jour'], y=((100 * time_series_09['P']) / time_series_09['T']), name='0-9'))
fig13.add_trace(go.Line(x=time_series_19['jour'], y=((100 * time_series_19['P']) / time_series_19['T']), name='10-19'))
fig13.add_trace(go.Line(x=time_series_29['jour'], y=((100 * time_series_29['P']) / time_series_29['T']), name='20-29'))
fig13.add_trace(go.Line(x=time_series_39['jour'], y=((100 * time_series_39['P']) / time_series_39['T']), name='30-39'))
fig13.add_trace(go.Line(x=time_series_49['jour'], y=((100 * time_series_49['P']) / time_series_49['T']), name='40-49'))
fig13.add_trace(go.Line(x=time_series_59['jour'], y=((100 * time_series_59['P']) / time_series_59['T']), name='50-59'))
fig13.add_trace(go.Line(x=time_series_69['jour'], y=((100 * time_series_69['P']) / time_series_69['T']), name='60-69'))
fig13.add_trace(go.Line(x=time_series_79['jour'], y=((100 * time_series_79['P']) / time_series_79['T']), name='70-79'))
fig13.add_trace(go.Line(x=time_series_89['jour'], y=((100 * time_series_89['P']) / time_series_89['T']), name='80-89'))
fig13.add_trace(go.Line(x=time_series_90['jour'], y=((100 * time_series_90['P']) / time_series_90['T']), name='90-90'))

# fig13.add_trace(go.Scatter(x=time_series_dates.index, y=timae_series_dates['T'], fill='tozeroy',line_color='grey'))
fig13.update_layout(title='Evolution quotidien de taux de positivité par class d\'ages')
fig13.show()
