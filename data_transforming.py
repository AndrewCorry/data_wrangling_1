import pandas as pd
import numpy as np


df = pd.read_csv('COVID-19_Cases_Over_Time.csv')
cases = df['New Cases']


df.pivot('Specimen Collection Date', 'Data As Of', 'New Cases')
print(df)
print(cases.mean())
print(cases - cases.mean())

