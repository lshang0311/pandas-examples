import pandas as pd

"""
    https://pandas.pydata.org/pandas-docs/stable/timeseries.html
"""

# data
str_data = r"""
weather
sunny
rain
rain
"""

df = pd.read_csv(pd.compat.StringIO(str_data))
rng = pd.date_range('2018-04-22', '2018-04-24', freq='D')
df.set_index(rng, inplace=True)

df_truncated = df.truncate(before='2018-04-23', after='2018-04-24')
print(df_truncated)
