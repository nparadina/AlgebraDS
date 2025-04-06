import pandas as pd

df=pd.read_csv('C:/Users/nikap/Desktop/demo_temperature_data.csv', engine='pyarrow')
print(df)
df=df[df['Temperature']>60]
print(df.head())
df.sort_values('Year')
print(df)
