import pandas as pd
import numpy as np


df = pd.read_csv('COVID-19_Cases_Over_Time.csv')
print(df.info())

print(df.isnull().any())
print(df.isnull().all())

df.drop(columns='Data Loaded At', inplace=True)
print(df)

cases = df['New Cases']
q1 = cases.quantile(.25)
q3 = cases.quantile(.75)
iqr = q3 - q1
pmin = q1 - 1.5 * iqr
pmax = q3 + 1.5 * iqr
nwc = cases.where(cases.between(pmin, pmax))

compare = pd.DataFrame({'before':cases, 'after':nwc})
print(compare.describe())

print(df.duplicated().any())

