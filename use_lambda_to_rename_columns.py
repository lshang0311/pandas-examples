import pandas as pd
import numpy as np

"""
Use lambda to change column names

"""

col_names = ['$A', 'B', '$C']
np.random.seed(0)
df = pd.DataFrame(np.random.randint(0, 10, (5, 3)),
                  columns=list(col_names))
print(df)

df.rename(columns=lambda x: x.replace('$', '') if '$' in x else x, inplace=True)
print(df)
