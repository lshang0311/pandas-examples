import numpy as np
import pandas as pd
from tabulate import tabulate

df = pd.DataFrame(
    data=np.random.randint(0, 10, (5, 3)),
    columns=list(['A', 'B', 'C'])
)

print(df)
print(tabulate(df, headers='keys', tablefmt='psql'))
