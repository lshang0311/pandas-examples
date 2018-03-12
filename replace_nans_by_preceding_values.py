import pandas as pd

"""
    https://stackoverflow.com/questions/27905295/how-to-replace-nans-by-preceding-values-in-pandas-dataframe
"""

df = pd.DataFrame(
    data=[[1, 2, 3], [4, None, None], [None, None, 9]],
    columns=list(['A', 'B', 'C'])
)
print(df)

df['A'].fillna(method='ffill', inplace=True)
print(df)

df.fillna(method='ffill', inplace=True)
print(df)
