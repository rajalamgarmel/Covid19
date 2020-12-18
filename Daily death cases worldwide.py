import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots


time_series = pd.read_csv('who_data.csv', header=0, delimiter=",")
#time_series['Date_reported'] = pd.to_datetime(time_series['Date_reported'])

# a. Covid-19 cases worldwide
# Firsty Data
time_series_dates = time_series.groupby('Date_reported').sum()

# Daily death cases
fig14 = go.Figure()
fig14.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['New_deaths'], fill = 'tonexty',
                          line_color = 'red'))
fig14.update_layout(title = 'Evolution des nombres quotidiens des décès dans le monde')
fig14.show()