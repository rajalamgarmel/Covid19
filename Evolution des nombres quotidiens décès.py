import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots

time_series = pd.read_csv('donnees-hospitalieres-nouveaux-covid19-2020-12-14-19h03.csv', header=0, delimiter=";")
time_series['jour'] = pd.to_datetime(time_series['jour'])


time_series_dates = time_series.groupby('jour').sum()
time_series_dc = time_series_dates['incid_dc']


fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=time_series_dates.index, y=time_series_dc,
                          line_color = 'black'))

# fig13.add_trace(go.Scatter(x=time_series_dates.index, y=timae_series_dates['T'], fill='tozeroy',line_color='grey'))
fig13.update_layout(title='Evolution des nombres quotidiens des décès en France')
fig13.show()
