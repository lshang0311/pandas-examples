import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

N = 1000
df['rand_col_1'] = np.random.RandomState(0).uniform(0, 1, size=N)
df['rand_col_2'] = np.random.RandomState(0).normal(0, 1, size=N)
df['rand_col_3'] = np.random.RandomState(0).binomial(10, 0.5, size=N)
df['rand_col_4'] = np.random.RandomState(1).poisson(3, size=N)

df.hist(bins=10)
plt.show()
