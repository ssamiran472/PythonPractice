# import pandas as pd
import pandas as pd
import numpy as np

data = pd.read_csv('nba.csv', index_col=1)
first = data["Name"]
print('Unique values are ', first.unique())
print('Unique values are ', first.nunique())
print('Unique values count ', first.value_counts())

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, np.nan, 80, 98]}

df = pd.DataFrame(dict)
df.fillna(0)
print(df.fillna(0))
print(df)
print(df.isnull())
print('-----::::::======', df.dropna())
