import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import plotly.graph_objects as go
import datetime as dt
import requests
from plotly.subplots import make_subplots


time_series = pd.read_csv('sp-pos-quot-fra-2020-12-11-19h20.csv', header=0, delimiter=";")

#time_series_dates = time_series.groupby('jour').sum()
time_series_h = time_series['P_h'].sum()
time_series_f = time_series['P_f'].sum()

fig13 = go.Figure(data=[go.Pie(labels = ['homme','femme'],values = [time_series_h,time_series_f])])


fig13.update_layout(title='Evolution des nombres quotidiens des cas positifs en France', width=700, height= 400,
                    margin = dict(t=0, l=0, r=0, b=0))
fig13.show()
