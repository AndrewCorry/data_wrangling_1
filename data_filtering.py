import pandas as pd
import numpy as np

df = pd.read_csv('COVID-19_Cases_Over_Time.csv').head()

print(df.head())
print(df['New Cases'])
print(df['New Cases'][1])
dft = df.T
print(dft)
print(dft.columns)
print(dft[2])

print(df[['New Cases', 'Cumulative Cases']])
print(df[2:4][['New Cases', 'Cumulative Cases']])

print(df.loc[1,'New Cases']) # loc is better than chain indexing(the line above this one) because it only requires 1 operation compared to 2. Loc only indexes by label, not postion. iloc uses integers.

print(df[[False, True, True, False, False]])
print(df['New Cases']>5)

df.sort_index(inplace=True, ascending=False)
df.sort_values(by='New Cases')
print(df['New Cases'])