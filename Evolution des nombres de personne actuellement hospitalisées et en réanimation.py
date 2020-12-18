import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots

time_series = pd.read_csv('donnees-hospitalieres-covid19-2020-12-14-19h03.csv', header=0, delimiter=";")
time_series_0 = time_series['sexe']==0
time_series_0 = time_series[time_series_0]


time_series_dates = time_series_0.groupby('jour').sum()
time_series_hos = time_series_dates['hosp']
time_series_rea = time_series_dates['rea']


fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=time_series_dates.index, y=time_series_hos, name='Hospitalisation'))
fig13.add_trace(go.Scatter(x=time_series_dates.index, y=time_series_rea, name='Réanimation'))

fig13.update_layout(title='Evolution des nombres de personne actuellement hospitalisées et en réanimation en France')
fig13.show()
