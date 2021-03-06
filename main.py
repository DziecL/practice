import pandas as pd
import plotly.express as px
from datetime import datetime

url = 'http://api.open-notify.org/iss-now.json'

df = pd.read_json(url)

df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']

df.reset_index(inplace=True)

df = df.drop(['index','message'], axis = 1)

fig = px.scatter_geo(df, lat = 'latitude', lon = 'longitude')

now = datetime.now()
date = str(now.strftime("%d-%m-%Y %H-%M-%S"))

fig.write_html('C:/Users/User/PycharmProjects/ISS/arch/first_figure ' + date + '.html', auto_open=True)
