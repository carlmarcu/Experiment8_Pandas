import pandas as pd
df=pd.read_csv('cars.csv')
odd=df.iloc[0:5,0:9:2]
mazda=df.loc[[0],:]
cylinder=df.loc[[23],['cyl']]
cylindergear=df.loc[[1,18,28],['cyl','gear']]