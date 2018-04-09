import pandas as pd

str_data = r"""
date,weather,city
2018-03-04,sunny,sydney
2018-03-05,nan,melbourne
2018-03-06,rain,perth
"""
df = pd.read_csv(pd.compat.StringIO(str_data))

print(df.isnull().any())
print(df['weather'].isnull().any())

df.iloc[1, 1] = 'cloudy'
assert not (df.isnull().any().any()), "No value should be missing"
