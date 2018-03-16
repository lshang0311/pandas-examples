import pandas as pd
import numpy as np

# add some columns - 1
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list('ABC'))
df['D'] = df['A'] + df['C']

# add some columns - 2
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list('ABC'))
df['D'] = df[['A', 'C']].sum(axis=1)

# add all the columns
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list('ABC'))
df['D'] = df[list(df.columns)].sum(axis=1)

# use lambda
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list('ABC'))
df['D'] = df.apply(lambda x: x['A'] * 100 + x['B'] / 2, axis=1)
print(df)
