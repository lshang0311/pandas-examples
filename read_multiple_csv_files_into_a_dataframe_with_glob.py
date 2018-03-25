import glob
import os

import pandas as pd

"""
https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe

"""

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('../data', "list_of_fruits_*.csv"))))
df.reset_index(inplace=True, drop=True)
print(df)
