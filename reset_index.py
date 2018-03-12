import numpy as np
import pandas as pd

df = pd.DataFrame(
    data=np.random.randint(0, 10, (5, 3)),
    columns=list(['C', 'A', 'B']),
    index=[11, 22, 2, 12, 4]
)
print(df)

df.reset_index(inplace=True, drop=True)
print(df)
