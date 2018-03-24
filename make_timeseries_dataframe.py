import pandas.util.testing as tm
import pandas as pd
from dateutil.relativedelta import relativedelta, FR
import matplotlib.pyplot as plt

# make a df of time series
tm.N = 10
df = tm.makeTimeDataFrame(freq='B')  # 'B': business daily
print(df)

# reindex with new time stamps
df.index = pd.date_range(
    start=pd.Timestamp.now().date() + relativedelta(weekday=FR(-1)),
    periods=df.shape[0],
    freq='B'
)
print(df)

# show
df.plot(figsize=(10, 6), marker='o')
plt.show()
