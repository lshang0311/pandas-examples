import pandas as pd
from sklearn import preprocessing

# data
str_data = r"""date,language,ex_complete,test_complete
2018-06-01,python,0,1
2018-06-02,python,1,2
2018-06-03,python,2,3
2018-06-04,r,3,4
2018-06-05,r,4,5
2018-06-06,r,5,6
2018-06-07,r,6,6
2018-06-08,r,7,6
2018-06-09,python,8,6
2018-06-10,r,9,6
2018-06-11,r,10,6
"""
df = pd.read_csv(pd.compat.StringIO(str_data))
df.set_index(['date', 'language'], inplace=True)
df.sort_index(inplace=True)

# scale
df[df.columns] = df[df.columns].values.astype(float)

scaler = preprocessing.MinMaxScaler()

df[df.columns] = scaler.fit_transform(df[df.columns])
print(df)

# inverse
df_inv = pd.DataFrame(scaler.inverse_transform(df), columns=df.columns, index=df.index)
print(df_inv)
