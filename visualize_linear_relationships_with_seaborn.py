import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame()

# x
N = 100
df['x'] = np.random.RandomState(0).uniform(0, 1, size=N)

# y
beta_0 = 1.0
beta_1 = 5.5
epsilon = np.random.RandomState(0).normal(0, 1.0, size=N)
df['y'] = beta_0 + beta_1 * df['x'] + epsilon

sns.lmplot(x='x', y='y', data=df, markers=['x'])
plt.xlim(0.0, 1.0)
plt.show()
