import matplotlib.pyplot as plt
import pandas as pd

str_data = r"""
a,b,c,d
0,1,5,1
1,2,10,1
2,3,15,0
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
ax = df.plot(kind='scatter', x='a', y='b', color='r', label='a vs. b')
df.plot(kind='scatter', x='a', y='c', color='g', ax=ax, label='a vs. c')
df.plot(kind='scatter', x='b', y='c', color='b', ax=ax, label='b vs. c')

ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()

plt.scatter(df['a'], df['b'], c=df['d'], s=300)
plt.show()
