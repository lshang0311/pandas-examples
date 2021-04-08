import pandas as pd
from io import StringIO

str_data = r"""
date, weather
2018-03-04, cloudy
2018-03-05, sunny
2018-03-06, rain
"""

df = pd.read_csv(StringIO(str_data))
print(df)
