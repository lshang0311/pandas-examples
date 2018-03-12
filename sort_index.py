import numpy as np
import pandas as pd

df = pd.DataFrame(
    data=np.random.randint(0, 10, (5, 3)),
    columns=list(['C', 'A', 'B']),
    index=[11, 22, 2, 12, 4]
)

df.reset_index(inplace=True)
print(df)

# sort the rows
df_sorted = df.sort_index(ascending=False)
print(df_sorted)

# sort the columns
df_sorted = df_sorted.sort_index(axis=1)
print(df_sorted)
