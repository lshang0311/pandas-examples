import pandas as pd
import matplotlib.pyplot as plt

str_data = r"""
date,store_1,store_2
2018-01-01,0,0
2018-01-02,21,22
2018-01-03,31,32
"""
df = pd.read_csv(
    pd.compat.StringIO(str_data),
    parse_dates=True,
    index_col='date',
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
print(df)

ax = df.plot(kind='bar')
lgd = plt.legend()
t0 = 'Sales_' + lgd.get_texts()[0]._text
t1 = 'Sales_' + lgd.get_texts()[1]._text
ax.legend(labels=[t0, t1])
ax.set_xticklabels([x.strftime('%Y-%m-%d') for x in df.index])
plt.xticks(rotation=10)
plt.show()
