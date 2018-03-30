import os

import pandas as pd
from openpyxl import load_workbook

"""
https://stackoverflow.com/questions/42370977/how-to-save-a-new-sheet-in-an-existing-excel-file-using-pandas
"""

# create an Excel file
str_data = r"""
date, weather
2018-03-30,cloudy
2018-03-31,sunny
2018-04-01,sunny
"""
df = pd.read_csv(pd.compat.StringIO(str_data))

file_name = r"./data/example.xlsx"
file_name = os.path.abspath(file_name)
writer = pd.ExcelWriter(file_name, engine='openpyxl')
df.to_excel(writer, sheet_name='weather', index=False)
writer.save()
writer.close()

# update the existing Excel file
writer = pd.ExcelWriter(file_name, engine='openpyxl')
book = load_workbook(file_name)
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df_update = pd.DataFrame({'location': ['sydney', 'gold coast', 'sunshine coast']})
df_update.to_excel(
    writer,
    sheet_name='weather',
    header=True,
    index=False,
    startrow=0,
    startcol=2
)

writer.save()
writer.close()
