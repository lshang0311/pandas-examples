import pandas as pd

str_data = r"""gender,age
female,20
female,nan
male,21
male,22
male,23
female,21
male,nan
female,22
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
print(df)

df['age'].fillna(
    df.groupby(['gender'])['age'].transform('mean'),
    inplace=True
)
print("--------")
print(df)
