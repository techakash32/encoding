import pandas as pd
import numpy as np

df=pd.read_csv('covid_toy.csv')
print(df.head(2))

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['gender']=le.fit_transform(df['gender'])
df['cough']=le.fit_transform(df['cough'])
df['city']=le.fit_transform(df['city'])

print(df.head(2))
