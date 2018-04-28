import pandas as pd

"""
https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict

"""

fruit_price = r"""product,number,store
apple,100,1
peach,300,1
apple,200,2
grape,33,2
peach,10,1
"""

df = pd.read_csv(pd.compat.StringIO(fruit_price))
print(df)

dict_product_code = {
    'apple': 'A',
    'peach': 'P',
    'grape': 'G'
}
df.replace({'product': dict_product_code}, inplace=True)
print(df)
