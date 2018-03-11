import pandas as pd

# rename all the column names
fruit_price = r"""A,B,C
banana,$2.5,1.2
grape,$5.356,2.3
apple,$4.99,4.5
"""
df = pd.read_csv(pd.compat.StringIO(fruit_price))
df.columns = ['fruit', 'price', 'weight']
print(df)

# rename a specific column
fruit_price = r"""A,B,C
banana,$2.5,1.2
grape,$5.356,2.3
apple,$4.99,4.5
"""
df = pd.read_csv(pd.compat.StringIO(fruit_price))
df.rename(columns={'A': 'fruit'}, inplace=True)
print(df)

# rename a subset of the columns
fruit_price = r"""A,B,C
banana,$2.5,1.2
grape,$5.356,2.3
apple,$4.99,4.5
"""
df = pd.read_csv(pd.compat.StringIO(fruit_price))
df.rename(columns={
    'A': 'fruit',
    'B': 'price'
}, inplace=True)
print(df)


