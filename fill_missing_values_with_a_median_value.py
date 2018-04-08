import pandas as pd

str_data = r"""
date,sales
2018-04-01,nan
2018-04-02,40
2018-04-03,nan
2018-04-04,30
2018-04-05,60
2018-04-06,300
"""
df = pd.read_csv(
    pd.compat.StringIO(str_data),
    parse_dates=True,
    index_col='date',
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
print(df)

print("\nmedian = {0:.2f}".format(df.median().values[0]))
print("mean = {0:.2f}\n".format(df.mean().values[0]))

df['sales'].fillna(df['sales'].median(), inplace=True)
print(df)
