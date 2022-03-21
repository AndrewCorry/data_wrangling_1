import pandas as pd
import numpy as np
import matplotlib_inline

df = pd.read_csv('COVID-19_Cases_Over_Time.csv')

print(df.shape)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
print(df.mean)
print(df['New Cases'].max())
print(df['New Cases'].plot())


