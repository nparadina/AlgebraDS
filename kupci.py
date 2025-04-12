import pandas as pd
import matplotlib.pyplot as plt

kupci_df=pd.read_csv(r"C:\Users\nikap\Downloads\Data\Data\Vjezbe_Primjeri\mall_customers.csv", delimiter=',')
print(kupci_df)

print(kupci_df.describe(include='all'))
kolona_min_3kvantil=kupci_df.describe(include='all').loc['75%'].min()
print(kolona_min_3kvantil)
print(kupci_df.corr().abs())
kupci_df.plot(kind='scatter',x='Age', y='Spending Score (1-100)', color='blue', alpha=0.5, label='Age vs Spending Score')
plt.show()

kupci_df['studenti']=kupci_df[kupci_df['Age'].between(18, 25)==True]
print(kupci_df['studenti'])