import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

str_data = r"""
date,open,sales,store
2018-01-01,N,0,1
2018-01-02,Y,21,1
2018-01-03,Y,31,1

2018-01-01,N,0,2
2018-01-02,Y,22,2
2018-01-03,Y,32,2
"""
df = pd.read_csv(
    pd.compat.StringIO(str_data),
    parse_dates=True,
    index_col='date',
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)

ax = sns.barplot(x=df.index, y="sales", hue="store", data=df)
ax.set_xticklabels([x.strftime('%Y-%m-%d') for x in df.index])
plt.show()
