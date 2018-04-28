import pandas as pd

"""
https://stackoverflow.com/questions/42192323/convert-pandas-dataframe-to-float-with-commas-and-negative-numbers

"""

str_data = r"""
date,sale
2018-01-01,"333,1,234.56"
2018-01-02,"444,2,345.67"
2018-01-03,"555,3,456.78"
2018-01-04,""
"""

df = pd.read_csv(pd.compat.StringIO(str_data), thousands=r',')

print(df)
