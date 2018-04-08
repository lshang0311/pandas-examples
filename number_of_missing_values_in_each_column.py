import pandas as pd

str_data = r"""
date,open,sales,store
2018-01-01,N,23,1
2018-01-02,,44,1
2018-01-03,Y,,1

2018-01-01,N,33,2
2018-01-02,,150,2
2018-01-03,Y,233,2

2018-01-01,N,3,3
2018-01-02,Y,14,3
2018-01-03,Y,125,3
"""
df = pd.read_csv(
    pd.compat.StringIO(str_data),
    parse_dates=True,
    index_col='date',
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)

print(df.isnull())
print(df.isnull().sum())
