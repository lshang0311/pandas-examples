import pandas as pd

data = r"""store,year,month,day,sales
1,2018,Mon01,D01,100
3,2018,Mon02,D02,200
9,2018,Mon03,D20,300
"""


# use function
def date_parser(date_string):
    return pd.datetime.strptime(date_string, '%Y Mon%m D%d')


df = pd.read_csv(
    pd.compat.StringIO(data),
    parse_dates={'DATE': [1, 2, 3]},
    date_parser=date_parser
)
df.set_index(['DATE'], inplace=True)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)

# use lambda - specify column indices
df = pd.read_csv(
    pd.compat.StringIO(data),
    index_col='date',
    parse_dates={'date': [1, 2, 3]},
    date_parser=lambda x: pd.datetime.strptime(x, '%Y Mon%m D%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)

# use lambda - specify column names
df = pd.read_csv(
    pd.compat.StringIO(data),
    index_col='date',
    parse_dates={'date': ['year', 'month', 'day']},
    date_parser=lambda x: pd.datetime.strptime(x, '%Y Mon%m D%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)
