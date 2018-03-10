import pandas as pd
import numpy as np

"""
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html

"""

s = pd.Series(np.random.randn(50))
print(s.head())

np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 10, (20, 3)), columns=list('ABC'))
df_sampled = df.sample(frac=0.7, replace=True, random_state=3)
print(df_sampled)
