import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

np.random.seed(0)
df['rand_col_1'] = np.random.uniform(0, 1, size=1000)
df['rand_col_2'] = np.random.uniform(0, 1, size=1000)

df.hist(bins=5)
plt.show()
