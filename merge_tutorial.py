import pandas as pd

"""
https://www.kaggle.com/crawford/python-merge-tutorial/notebook

"""

ratings = r"""
userID,placeID,rating,food_rating,service_rating
U1067,1,1,1,1
U1067,2,1,2,2
U1067,3,1,0,1
U1067,4,0,0,0
U1067,5,1,0,0
U1103,6,1,2,1
"""


parking = r"""
placeID,parking_lot
1,public
2,none
6,valet parking
"""

df_ratings = pd.read_csv(pd.compat.StringIO(ratings))
df_parking = pd.read_csv(pd.compat.StringIO(parking))

df = pd.merge(left=df_ratings, right=df_parking, on="placeID")
print(df)



