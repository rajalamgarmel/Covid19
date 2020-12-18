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

time_series_sexe1 = time_series['sexe'] == 1
time_series_sexe1 = time_series[time_series_sexe1]

time_series_sexe2 = time_series['sexe'] == 2
time_series_sexe2 = time_series[time_series_sexe2]


time_series_dates1 = time_series_sexe1.groupby('jour').sum()
time_series_hos1 = time_series_dates1['hosp'].sum()
time_series_rea1 = time_series_dates1['rea'].sum()

time_series_dates2 = time_series_sexe2.groupby('jour').sum()
time_series_hos2 = time_series_dates2['hosp'].sum()
time_series_rea2 = time_series_dates2['rea'].sum()


fig13 = go.Figure(data=[go.Pie(labels = ['Hommes','Femmes'],
                               values = [time_series_rea1,time_series_rea2])])

# fig13.add_trace(go.Scatter(x=time_series_dates.index, y=timae_series_dates['T'], fill='tozeroy',line_color='grey'))
fig13.update_layout(title='Evolution des hospitalisation en France', width=300, height= 200,
                    margin = dict(t=0, l=0, r=0, b=0))

fig13.show()
