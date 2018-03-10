import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 10, (5, 2)), columns=list('AB'))

# equal
df_copy = df.copy(deep=True)
assert_frame_equal(df, df_copy)

# not equal - values are different
df_copy['A'][-2:] = 100
assert_frame_equal(df, df_copy)

# not equal - "dtypes" are different
df_copy = df.copy(deep=True)
df_copy['A'] = df_copy['A'].astype('int32')
assert_frame_equal(df, df_copy)
