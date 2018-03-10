import pandas as pd
from decimal import Decimal

"""
Apply a function to each row of a DataFrame to create a new column

"""


def create_price_label(row):
    price = Decimal(row['price'])
    price = round(price, 2)
    return row['name'].title() + " $" + str(price)


fruit_price = r"""name,price
banana,2.5
grape,5.356
apple,4.99
"""

df = pd.read_csv(pd.compat.StringIO(fruit_price))
df['label'] = df.apply(create_price_label, axis=1)

print(df)
