import pandas as pd
df=pd.read_csv('cars.csv')
odd=df.iloc[0:5,1:12:2]
print(odd)
mazda=df.loc[[0],:]
print(mazda)
camaro=df.loc[23,'cyl']
print("The Cylinder of Camaro Z28 is: ", camaro)
carz=df.loc[[1,18,28],['cyl','gear']]
print(carz)