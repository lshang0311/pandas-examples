import pandas as pd

fruit_price = r"""product,unit_price,total_price
apple,"$1.56","$1,234,567"
peach,"$3.33","$2,345,678"
grape,"$2.22","$3,456,789"
"""

df = pd.read_csv(pd.compat.StringIO(fruit_price))

df = df.applymap(lambda x: float((x.replace(',', '').replace('$', ''))) if '$' in x else x)
print(df)
