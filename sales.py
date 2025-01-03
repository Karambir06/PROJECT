import pandas as pd
df=pd.read_csv('iris.csv')
print(df.head())
print(df.tail())
print(df.head(32))