import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\nikap\Downloads\Data\Data\Filmovi\movie_dataset.csv", delimiter=',')

# print(df.head())
# print(df.columns)

# print(df.genres)
# print(df.info())

# print(df.genres.str.contains('Romance'))
# print(df[df.genres.str.contains('Romance')==True].plot.hist()).show()

df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
#print(df[(df.release_date.dt.year>=1960) & (df.release_date.dt.year<1985)].shape)

print(df[(df.release_date.dt.year>=2010) | (df.release_date.dt.year<1950)])
df['year']=df.release_date.dt.year.astype('Int64')
df['year'].dropna(inplace=True)


# if df['year']>=2000:
#         df['century']='21st century'
#         print(df[['year', 'century']].head(10))

# df['godine_z_score']=(df['year']-df['year'].mean())/df['year'].std()
# print(df[['year', 'godine_z_score']].head(10))

# df['min_max']=(df['year']-df['year'].min())/(df['year'].max()-df['year'])
# print(df[['year', 'godine_z_score']].head(10))


# print(df.describe(include='all').loc['std'].sort_values(ascending=False))
# df.revenue.plot.hist(bins=100, color='blue', alpha=0.5, label='revenue')
# plt.show()

# correlation_matrix = df.corr()['revenue'].drop('revenue').sort_values(ascending=False)
# print(correlation_matrix)

# df.plot.line(x='year', y='revenue', color='blue', alpha=0.5, label='revenue')
# df.plot.line(x='year', y='buvote_count', color='red', alpha=0.5, label='budget')
# plt.show()

df['Drama']=df.genres.str.contains('Drama')
df.dropna(inplace=True)
df.Drama=df.Drama.astype('int')
print(df.Drama)

df2=df.pivot_table(index='year', columns='Drama', values='keywords', aggfunc='count').fillna(0).astype(int)
print(df.columns)
print(df.head(30))
print(df.describe(include='all'))

print(df.describe(include='all').loc['unique'].isna())

df3=pd.pivot_table(df, index='original_language', columns='status', values='revenue', aggfunc='median').dropna()
print(df3)