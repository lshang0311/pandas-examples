import pandas as pd

"""
datetime format:
  https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior
"""

str_data = r"""
date,weather
20180304,cloudy
20180305,sunny
20180306,rain
"""

df = pd.read_csv(pd.compat.StringIO(str_data))
print(df)
print(df.dtypes)

# int64 -> datetime64[ns]
df['date'] = pd.to_datetime(df['date'], format="%Y%m%d")
print(df)
print(df.dtypes)
