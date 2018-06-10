import pandas as pd

"""
https://www.kaggle.com/crawford/python-merge-tutorial/notebook

pd.merge(left_dataframe, right_dataframe, on="some_column", how="left|right|inner|outer")

"""

ratings = r"""userID,placeID,rating,food_rating,service_rating
U1067,1,1,1,1
U1067,2,1,2,2
U1067,3,1,0,1
U1067,4,0,0,0
U1067,5,1,0,0
U1103,6,1,2,1
"""

parking = r"""placeID,parking_lot
1,public
2,none
6,valet parking
7,public
"""

df_ratings = pd.read_csv(pd.compat.StringIO(ratings))
df_parking = pd.read_csv(pd.compat.StringIO(parking))

print("inner:")
df = pd.merge(left=df_ratings, right=df_parking, on="placeID", how="inner")
print(df)

print("left:")
df = pd.merge(left=df_ratings, right=df_parking, on="placeID", how="left")
print(df)

print("right:")
df = pd.merge(left=df_ratings, right=df_parking, on="placeID", how="right")
print(df)

print("outer:")
df = pd.merge(left=df_ratings, right=df_parking, on="placeID", how="outer")
print(df)
