import pandas as pd
from patsy.highlevel import dmatrix

"""
https://towardsdatascience.com/the-dummys-guide-to-creating-dummy-variables-f21faddb1d40
https://www.youtube.com/watch?v=WRxHfnl-Pcs
"""

url = 'http://data.princeton.edu/wws509/datasets/salary.dat'
df = pd.read_table(url, delim_whitespace=True)
print(df.head())

# use pandas
dummy = pd.get_dummies(df['sx'])
print(dummy.head())

df = pd.concat([df, dummy], axis=1)
print(df.head())

# use patsy
dummy = dmatrix("sx", df, return_type='dataframe')
df = pd.concat([df, dummy], axis=1)
print(df.head())
