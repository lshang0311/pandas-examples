import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame()

# x
N = 5000
df['x1'] = np.random.RandomState(0).uniform(0, 1, size=N)
df['x2'] = np.random.RandomState(0).normal(0, 0.15, size=N)

# y
beta_0 = 1.0
beta_1 = 3.5
beta_2 = 0.5
epsilon = np.random.RandomState(0).normal(0, 0.01, size=N)
df['y'] = beta_0 + beta_1 * df['x1'] + beta_2 * df['x2'] + epsilon

sns.lmplot(x='x1', y='y', data=df, markers=['x'])
sns.lmplot(x='x2', y='y', data=df, markers=['x'])

style = 'bmh'
with plt.style.context(style):
    fig = plt.figure(figsize=(7, 7))

    color = 'blue'

    layout = (2, 2)
    ax1 = plt.subplot2grid(layout, (0, 0), rowspan=1, colspan=2)
    sns.distplot(df['y'], color=color, ax=ax1)

    ax2 = plt.subplot2grid(layout, (1, 0))
    sns.distplot(df['x1'], color=color, ax=ax2)

    ax3 = plt.subplot2grid(layout, (1, 1))
    sns.distplot(df['x2'], color='red', ax=ax3)

    fig.tight_layout(pad=0.5, w_pad=5.0, h_pad=5.0)

plt.show()
