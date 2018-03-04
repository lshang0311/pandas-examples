import pandas as pd

str_data = r"""
date, weather
2018-03-04, cloudy
2018-03-05, sunny
2018-03-06, rain
"""

df = pd.read_csv(pd.compat.StringIO(str_data))
print(df)

df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.weekday_name
df['weekday_short'] = df['date'].dt.strftime("%a")
print(df)
