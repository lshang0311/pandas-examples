import pandas as pd

"""
Apply a function to each row of a DataFrame to create a new column

"""


def create_price_label(row):
    return row['name'].title() + " $" + str(row['price'])


fruit_price = r"""name,price
banana,2.55
grape,5.35
apple,4.99
"""

df = pd.read_csv(pd.compat.StringIO(fruit_price))
df['label'] = df.apply(create_price_label, axis=1)

print(df)
