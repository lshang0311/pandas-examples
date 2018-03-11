import pandas as pd
import numpy as np

"""
Use list comprehension to change column names

"""

col_names = ['$A', 'B', '$C']
df = pd.DataFrame(
    data=np.random.randint(0, 10, (5, 3)),
    columns=list(col_names)
)

# remove '$' in the column names
df.columns = [col.strip('$') for col in df.columns]
print(df)
