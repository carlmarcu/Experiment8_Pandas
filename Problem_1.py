import pandas as pd
df=pd.read_csv('cars.csv')
first=df.head()
print(first)
last=df.tail()
print(last)