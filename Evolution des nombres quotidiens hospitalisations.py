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
time_series_hos = time_series_dates['incid_hosp']
time_series_rea = time_series_dates['incid_rea']
time_series_rad = time_series_dates['incid_rad']


fig13 = go.Figure()
fig13.add_trace(go.Line(x=time_series_dates.index, y=time_series_hos, name='Nouvelles hospitalisations'))
fig13.add_trace(go.Line(x=time_series_dates.index, y=time_series_rea, name='Nouvelles admission en réanimation'))
fig13.add_trace(go.Line(x=time_series_dates.index, y=time_series_rad, name='Nouveaux retour a domicile'))



# fig13.add_trace(go.Scatter(x=time_series_dates.index, y=timae_series_dates['T'], fill='tozeroy',line_color='grey'))
fig13.update_layout(title='Evolution des nombres quotidiens d\'hospitatisations, de réanimation '
                          'et de retour à domicile en France')
fig13.show()
