import pandas as pd

data = r"""
date,col_1
2000-01-03,1
2000-01-04,3
2000-01-05,5
"""

df = pd.read_csv(pd.compat.StringIO(data),
                 index_col=['date'],
                 parse_dates=True,
                 date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
                 )

assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)
