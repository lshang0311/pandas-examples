import pandas as pd
import os

"""
https://docs.python.org/3.5/library/os.path.html

"""

path = r"./data"
path = os.path.abspath(path)

file_name = 'list_of_fruits_1.csv'
full_file_name = os.path.join(path, file_name)

df = pd.read_csv(full_file_name)
print(df)
