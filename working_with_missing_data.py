import pandas as pd
import matplotlib.pyplot as plt

"""
https://pandas.pydata.org/pandas-docs/version/0.22.0/missing_data.html

"""

data = r"""date,col_1,unwanted_1,unwanted_2
2018-06-10,0,NaN,NaN
2018-06-11,1,NaN,1
2018-06-12,NaN,a,2
2018-06-13,3,b,NaN
2018-06-14,NaN,x,3
2018-06-15,5,c,5
2018-06-16,6,d,7
2018-06-20,NaN,d,7
"""

df = pd.read_csv(
    pd.compat.StringIO(data),
    usecols=['date', 'col_1'],
    index_col=['date'],
    parse_dates=True,
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)

df.plot(style='-x', color='k', title='original')

# interpolation
df = df.interpolate(method='time')
df.plot(style='-o', color='r', title='interpolated')
plt.show()
