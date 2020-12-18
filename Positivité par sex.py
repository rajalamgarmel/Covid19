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


time_series_dates = time_series.groupby('jour').sum()


fig13 = go.Figure()
fig13.add_trace(go.Line(x=time_series_dates.index, y=((100 * time_series_dates['P_h']) / time_series_dates['T_h']), name='Hommes'))
fig13.add_trace(go.Line(x=time_series_dates.index, y=((100 * time_series_dates['P_f']) / time_series_dates['T_f']), name='Femmes'))

# fig13.add_trace(go.Scatter(x=time_series_dates.index, y=timae_series_dates['T'], fill='tozeroy',line_color='grey'))
fig13.update_layout(title='Evolution quotidien du taux de positivité par sexe en France')
fig13.show()
