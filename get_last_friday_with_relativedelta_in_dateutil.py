import pandas as pd
from dateutil.relativedelta import relativedelta, FR

list_of_dicts = [
    {
        'date': '2018-03-01',
        'weather': 'cloudy'
    },
    {
        'date': '2018-03-02',
        'weather': 'sunny'
    },
    {
        'date': '2018-03-03'
    },
    {
        'date': '2018-03-04',
        'weather': 'rain'
    }
]
df = pd.DataFrame(list_of_dicts)

df['date'] = pd.to_datetime(df['date'])
df['last_friday'] = df['date'].apply(lambda x: x + relativedelta(weekday=FR(-1)))
print(df)
