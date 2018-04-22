import pandas as pd

# data
str_data = r"""
date, weather
2017-01-01,rain
2017-01-02,sunny
2017-01-03,rain
2017-12-25,rain

2018-01-01,cloudy
2018-01-02,sunny
2018-01-03,rain
2018-12-25,sunny
"""

df = pd.read_csv(pd.compat.StringIO(str_data))
df['date'] = pd.to_datetime(df['date'])
df = df.set_index(['date'])

# slice
df_sliced = df['2018-01-01':]

df_sliced = df[:'2017-12-25']

df_sliced = df['2018']

df_sliced = df['2018-01']

df_sliced = df['2018-01-01':'2018-01-31']
print(df_sliced)
