import pandas as pd
data = r"""
date,col_str,col_int
2018-03-05,sunny,10
2018-10-04,cloudy,0
2018-03-06,rain,2
"""

df = pd.read_csv(pd.compat.StringIO(data))

df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df_sorted = df.sort_values(by='date')

df_sorted = df.sort_values(by='col_int', ascending=False)

print(df_sorted)
