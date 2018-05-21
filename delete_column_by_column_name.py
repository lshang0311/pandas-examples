import pandas as pd

data = r"""date,col_a,col_b,col_c
2018-05-20,1,2,3
2018-05-21,3,4,6
2018-05-22,5,6,9
"""

df = pd.read_csv(
    pd.compat.StringIO(data),
    index_col=['date'],
    parse_dates=True,
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)

df.drop(['col_a'], axis=1, inplace=True)
print(df)

df.drop(['col_b', 'col_c'], axis=1, inplace=True)
assert df.empty is True, "Expecting an empty data frame"
