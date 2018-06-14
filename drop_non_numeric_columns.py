import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

data = r"""date,numeric_col_1,non-numeric_col,numeric_col_2
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
    index_col=['date'],
    parse_dates=True,
    date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)

df_copy = df.copy()

# use private method
df = df._get_numeric_data()
print(df)

# use select_dtypes
df_copy = df_copy.select_dtypes([np.number])
print(df_copy)

assert_frame_equal(df, df_copy)
