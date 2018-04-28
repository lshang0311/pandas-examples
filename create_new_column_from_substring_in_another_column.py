import pandas as pd

fruit_price = r"""product,price
au-apple-1,2.5
au-apple-2,5.356
au-peach-1,4.99
au-peach-2,3.99
au-grape-2,3.99
"""

df = pd.read_csv(pd.compat.StringIO(fruit_price))
df['Is Apple'] = df['product'].apply(lambda x: 'Y' if 'apple' in x else 'N')

print(df)
