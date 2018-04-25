import pandas as pd

"""
    https://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation-how-are-they-different#
    https://pandas.pydata.org/pandas-docs/stable/indexing.html
"""

str_data = r"""
name,age,color,food,height,score,state
Jane,30,blue,Steak,165,4.6,NY
Nick,2,green,Lamb,70,8.3,TX
Aaron,12,red,Mango,120,9.0,FL
Penelope,4,white,Apple,80,3.3,AL
Dean,32,gray,Cheese,180,1.8,AK
Christina,33,black,Melon,172,9.5,TX
Cornelia,69,red,Beans,150,2.2,TX
"""

df = pd.read_csv(pd.compat.StringIO(str_data))
df = df.set_index(['name'])

# .loc - select by labels
s = df.loc['Penelope']
assert isinstance(s, pd.Series)

df_sliced = df.loc[['Cornelia', 'Jane', 'Dean']]
assert isinstance(df_sliced, pd.DataFrame)

df_sliced = df.loc['Aaron':'Dean']
df_sliced = df.loc[lambda x: x['age'] < 10]
df_sliced = df.loc[['Jane', 'Dean'], 'height':]

# .iloc - select by integer location
s = df.iloc[4]
df_sliced = df.iloc[2:]
print(df_sliced)
