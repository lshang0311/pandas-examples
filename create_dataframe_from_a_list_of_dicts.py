import pandas as pd

list_of_dicts = [
    {
        'date': '2018-03-04',
        'weather': 'cloudy'
    },
    {
        'date': '2018-03-05',
        'weather': 'sunny'
    },
    {
        'date': '2018-03-06'
    },
    {
        'date': '2018-03-07',
        'weather': 'rain'
    }
]
df = pd.DataFrame(list_of_dicts)
print(df)
