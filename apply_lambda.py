import pandas as pd

city = r"""city,state
sydney,nsw
brisbane,qld
perth,sa
"""

df = pd.read_csv(pd.compat.StringIO(city))

df['state'] = df['state'].apply(lambda x: x.upper())
df['city'] = df['city'].apply(lambda x: x.title())
print(df)
