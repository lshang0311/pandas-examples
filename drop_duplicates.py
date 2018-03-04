import pandas as pd

df = pd.DataFrame({
    'A': [1, 1, 2, 3, 3],
    'B': ['apple', 'grape', 'apple', 'banana', 'grape'],
    'C': [1, 2, 3, 4, 5]
})
print(df)

df = df.drop_duplicates(['A'])
print(df)

df = df.drop_duplicates(['B'])
print(df)

df.reset_index(drop=True, inplace=True)
print(df)
