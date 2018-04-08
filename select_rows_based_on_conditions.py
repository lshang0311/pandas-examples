import pandas as pd

str_data = r"""
date,open,sales,store
2018-01-01,N,23,1
2018-01-02,Y,44,1
2018-01-03,Y,55,1

2018-01-01,N,33,2
2018-01-02,,150,2
2018-01-03,Y,233,2

2018-01-01,N,3,3
2018-01-02,Y,14,3
2018-01-03,Y,125,3
"""
df = pd.read_csv(pd.compat.StringIO(str_data),
                 parse_dates=True,
                 index_col='date',
                 date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
                 )

is_open = df['open'] == 'Y'
store_id = df['store'] == 2
print(df[is_open & store_id])

cond_1 = df['open'].notnull()
cond_2 = df['sales'] > 100
cond = cond_1 & cond_2
print(df[cond])