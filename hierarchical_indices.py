import pandas as pd

"""
Ref:
    https://www.datacamp.com/community/tutorials/pandas-multi-index#comments
"""

str_data = r"""date,language,ex_complete
2017-01-01,python,6
2017-01-02,python,5
2017-01-03,python,10
2017-01-01,r,8
2017-01-02,r,8
2017-01-03,r,8
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
df.set_index(['date', 'language'], inplace=True)
df.sort_index(inplace=True)

print(df.index)

# slice
s = df.loc['2017-01-02']
print(s)

s = df.loc[('2017-01-02', 'r')]
print(s)
