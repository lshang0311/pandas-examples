import pandas as pd
import numpy as np

"""
Ref:
    http://pandas-docs.github.io/pandas-docs-travis/advanced.html
    https://www.datacamp.com/community/tutorials/pandas-split-apply-combine-groupby
"""

# split, apply, combine
df = pd.DataFrame({
    'jim': [0, 0, 1, 1],
    'joe': ['x', 'x', 'z', 'y'],
    'jolie': np.random.rand(4),
    'john': np.random.rand(4),
})
print('df:')
print(df)

df_by_jim = df.groupby(['jim'])
print('group:')
print(list(df_by_jim)[0][1])
print('group:')
print(list(df_by_jim)[1][1])

print('describe:')
print(df_by_jim.describe())

# multiple indexers
s = pd.Series(
    [1, 2, 3, 4, 5, 6],
    index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]])
)
print(s)

groups = list(s.groupby(level=[0]))
print(groups[0][0])
print(groups[0][1])
print(s.groupby(level=[0]).sum())

groups = list(s.groupby(level=[0, 1]))
print(groups[0][0])
print(groups[0][1])

groups = list(s.groupby(level=[1]))
print(s.groupby(level=[1]).sum())

s.index.names = ['foo', 'bar']  # set index names
groups = list(s.groupby(level=['foo']))

groups = list(s.groupby(level=['bar']))

print(s.loc(axis=0)[:, ['c']])  # slicer
print(s.loc(axis=0)[['A'], :])

print("")
