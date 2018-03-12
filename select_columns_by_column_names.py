import numpy as np
import pandas as pd
from tabulate import tabulate

# construct a DataFrame
column_names = ['A', 'B', 'C']
df = pd.DataFrame(
    data=np.random.randint(0, 10, (5, 3)),
    columns=list(column_names)
)
print(tabulate(df, headers='keys', tablefmt='psql'))

# subset by column names
df_2 = df[['A', 'C']]
print(tabulate(df_2, headers='keys', tablefmt='psql'))
