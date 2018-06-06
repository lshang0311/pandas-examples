import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, binom

"""
https://en.wikipedia.org/wiki/Quantile

"""

# make data
str_data = r"""date,x,y
2016-12-31,0,2
2017-01-01,1,2
2017-01-02,2,2 
2017-01-03,3,2
2017-01-04,4,2
2017-01-05,5,2
2017-01-06,6,3
2017-01-07,7,3
2017-01-08,8,4
2017-01-09,9,4
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
df.set_index(['date'], inplace=True)

df['x'] = df['x'].astype(float)
df['y'] = df['y'].astype(float)

df_copy = df.copy()

# replace - 1
print(df)
mask = (df['x'] > 0.0) & (df['x'] < 3.0)
df.loc[mask, 'x'] = -1
print(df)

# replace - 2
print(df_copy)
df_copy['x'] = np.where((df_copy['y'] == 3.0) | (df_copy['y'] == 4.0), np.nan, df_copy['x'])
print(df_copy)
