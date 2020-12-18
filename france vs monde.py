import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots

time_series = pd.read_csv('who_data.csv', header=0, delimiter=",")
time_series['Date_reported'] = pd.to_datetime(time_series['Date_reported'])

time_series_dates = time_series.groupby('Date_reported').sum()
time_series_dates

# France
time_series_fr = time_series['Country'] == ('France')
time_series_fr = time_series[time_series_fr]

# Spane
time_series_sp = time_series['Country'] == ('Morocco')
time_series_sp = time_series[time_series_sp]

# Italy
time_series_it = time_series['Country'] == ('United States of America')
time_series_it = time_series[time_series_it]

# Germany
time_series_gr = time_series['Country'] == ('Brazil')
time_series_gr = time_series[time_series_gr]

# The United Kingdom
time_series_kg = time_series['Country'] == ('China')
time_series_kg = time_series[time_series_kg]

# Cumulative cases

fig15 = go.Figure()

fig15.add_trace(go.Line(x = time_series_fr['Date_reported'], y = time_series_fr['Cumulative_deaths'], name = 'FRANCE'))
fig15.add_trace(go.Line(x = time_series_sp['Date_reported'], y = time_series_sp['Cumulative_deaths'], name = 'MAROC'))
fig15.add_trace(go.Line(x = time_series_it['Date_reported'], y = time_series_it['Cumulative_deaths'], name = 'ETAT UNIS'))
fig15.add_trace(go.Line(x = time_series_gr['Date_reported'], y = time_series_gr['Cumulative_deaths'], name = 'BRAZIL'))
fig15.add_trace(go.Line(x = time_series_kg['Date_reported'], y = time_series_kg['Cumulative_deaths'], name = 'LA CHINE'))

fig15.update_layout(title = 'Evolution des décès en France et dans le monde')

fig15.show()