import pandas as pd
from sklearn.model_selection import train_test_split

# data
data = r"""date,x
2018-03-01,0
2018-03-02,1
2018-03-03,2
2018-03-04,3
2018-03-05,4
2018-03-06,5
2018-03-07,6
2018-03-08,7
2018-03-09,8
2018-03-10,9
"""
df = pd.read_csv(pd.compat.StringIO(data))

# use pandas sample
train_and_validate = df.sample(frac=0.8, random_state=0)
test = df.drop(train_and_validate.index)

train = train_and_validate.sample(frac=0.8, random_state=0)
validate = train_and_validate.drop(train.index)

print(train.sort_index())
print(validate.sort_index())
print(test.sort_index())

# use sklearn
train, test = train_test_split(df, test_size=0.2, random_state=1)
train, validate = train_test_split(train, test_size=0.2, random_state=1)
print("train:")
print(train.sort_index())

print("validate:")
print(validate.sort_index())

print("test:")
print(test.sort_index())
