import pandas as pd

"""
Ref:
    https://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe
"""

str_data = r"""date,language,example_complete
2017-01-01,python,1
2017-01-02,python,3
2017-01-03,python,5

2017-01-01,r,2
2017-01-02,r,4
2017-01-03,r,6
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
df.set_index(['date'], inplace=True)
df.sort_index(inplace=True)

# insert None
df.iloc[0, 0] = None
print(df)
assert isinstance(df['language'].iloc[0], type(None))

# filter
mask = df['language'].str.contains('r', na=False)
print(df[mask])
