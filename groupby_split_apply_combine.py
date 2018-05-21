import numpy as np
import pandas as pd

"""
https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html
"""

rng = np.random.RandomState(0)
df = pd.DataFrame(
    {
        'key': ['A', 'B', 'C', 'A', 'B', 'C'],
        'data1': range(6),
        'data2': rng.randint(0, 10, 6)
    },
    columns=['key', 'data1', 'data2']
)
print(df)


def f_norm(x):
    print("group:")
    print(x)
    return x / x.sum()


def f_sum(x):
    return x.sum()


def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x


# transformation
print(df.groupby('key').transform(lambda x: x - x.mean()))
print(df.groupby('key').transform(f_norm))
df[['data1_group_sum', 'data2_group_sum']] = df.groupby('key').transform(f_sum)
print(df)

# apply()
print(df.groupby('key').apply(norm_by_data2))

# specifying the split key
L = [0, 0, 1, 1, 1, 1]
print(df.groupby(L).sum())

# a dictionary mapping index to group
df2 = df.set_index(['key'])

mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print(df2.groupby(mapping).sum())
