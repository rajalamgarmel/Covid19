import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots

time_series = pd.read_csv('donnees-hospitalieres-covid19-2020-12-14-19h03.csv', header=0, delimiter=";")
time_series['jour'] = pd.to_datetime(time_series['jour'])


time_series_dates = time_series.groupby('jour').sum()


fig13 = go.Figure()
fig13.add_trace(go.Line(x=time_series_dates.index, y=((100 * time_series_dates['P']) / time_series_dates['T']), name='Taux de positivité'))
fig13.add_trace(go.Scatter(x=time_series_dates.index, y=time_series_dates['T'], fill='tozeroy'))
fig13.update_layout(title='Evolution de taux de positivité quotidien en France')
fig13.show()
