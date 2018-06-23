import pandas as pd
from sklearn import preprocessing

str_data = r"""match,result
1,win
2,win
3,draw
4,draw
5,lose
6,win
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
df_copy = df.copy()
print(df)

print("> Use LabelEncoder:")
le = preprocessing.LabelEncoder()
df['result'] = le.fit_transform(df['result'])
print(df)
print(le.classes_)
df['result'] = le.inverse_transform(df['result'])
print(df)

print("> Use MAP:")
res_map = {
    'win': 3,
    'lose': 0,
    'draw': 1
}

inv_map = {v: k for k, v in res_map.items()}

df_copy['result'] = df_copy['result'].map(res_map).astype(int)
print(df_copy)

df_copy['result'] = df_copy['result'].map(inv_map).astype(str)
print(df_copy)
