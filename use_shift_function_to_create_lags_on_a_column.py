import pandas as pd
import matplotlib.pyplot as plt

data = r"""
date,col_num
2018-03-01,1
2018-03-02,2
2018-03-03,3
2018-03-04,4
2018-03-05,5
2018-03-06,6
2018-03-07,7
"""

df = pd.read_csv(pd.compat.StringIO(data),
                 index_col=['date'],
                 parse_dates=True,
                 date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
                 )

df['lag_1'] = df['col_num'].shift(1)
df['lag_2'] = df['col_num'].shift(2)
df['lag_-1'] = df['col_num'].shift(-1)
print(df)

# show
df.plot(figsize=(10, 6), marker='o')
plt.show()
