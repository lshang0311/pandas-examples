import pandas as pd
import numpy as np

"""
Use lambda to change column names

"""

col_names = ['$A', 'B', '$C']
df = pd.DataFrame(data=np.random.randint(0, 10, (5, 3)),
                  columns=list(col_names))

df.rename(columns=lambda x: x.replace('$', '') if '$' in x else x, inplace=True)
print(df)
