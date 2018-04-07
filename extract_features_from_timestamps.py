import pandas as pd

str_data = r"""
date,weather
2018-01-01,cloudy
2018-01-02,sunny
2018-01-03,sunny
2018-01-04,sunny
2018-01-05,sunny
2018-01-06,sunny
2018-01-07,sunny
2018-01-08,sunny
"""
df = pd.read_csv(pd.compat.StringIO(str_data),
                 parse_dates=True,
                 index_col='date',
                 date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
                 )

df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['weekofyear'] = df.index.weekofyear
df['weekday'] = df.index.weekday
df['weekday_name'] = df.index.weekday_name
df['hour'] = df.index.hour
df['date'] = df.index.date
df['time'] = df.index.time
