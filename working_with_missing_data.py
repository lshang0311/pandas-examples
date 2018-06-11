import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

"""
https://pandas.pydata.org/pandas-docs/version/0.22.0/missing_data.html
https://matplotlib.org/users/gridspec.html
https://matplotlib.org/examples/pylab_examples/legend_demo3.html
https://stackoverflow.com/questions/38152356/matplotlib-dollar-sign-with-thousands-comma-tick-labels

"""

data = r"""date,col_1,unwanted_1,unwanted_2
2018-06-10,0,NaN,NaN
2018-06-11,1,NaN,1
2018-06-12,NaN,a,2
2018-06-13,3,b,NaN
2018-06-14,NaN,x,3
2018-06-15,NaN,c,5
2018-06-16,6,d,7
"""

df = pd.read_csv(
    pd.compat.StringIO(data),
    usecols=['date', 'col_1'],
    index_col=['date'],
    parse_dates=True,
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)

style = 'bmh'
with plt.style.context(style):
    fig = plt.figure(figsize=(7, 6))
    layout = (2, 1)
    ax_1 = plt.subplot2grid(layout, (0, 0))
    ax_2 = plt.subplot2grid(layout, (1, 0), sharex=ax_1)

    df.plot(ax=ax_1, style='-.s', color='k', title='original')

    df = df.interpolate(method='time')
    df.plot(ax=ax_2, style='-o', color='r', title='interpolated')

    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax_1.yaxis.set_major_formatter(tick)
    ax_1.set_ylabel('col 1', rotation=0, fontsize=10, labelpad=20)

    ax_1.legend(['col 1'], shadow=True, fancybox=True, loc='lower right', title='Legend')
    ax_2.legend(['col 2'], shadow=True, fancybox=True, loc='lower right')

    ax_1.get_legend().get_title().set_color("red")

    ax_1.grid(color='y', which='minor')
    ax_2.grid(color='y', which='minor')

    plt.tight_layout()
    plt.show()
