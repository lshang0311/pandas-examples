import pandas as pd

data = r"""
date,col_1
2018-02-26,1
2018-03-05,1
2018-03-12,1
2018-03-19,1
2018-03-26,1
2018-04-01,1
2018-04-02,1
"""


# datetime format:
#  https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior
df = pd.read_csv(pd.compat.StringIO(data),
                 index_col=['date'],
                 parse_dates=True,
                 date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
                 )

table = df.groupby(pd.Grouper(freq='M')).sum()
print(table)
