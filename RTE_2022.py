import csv
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('RTE_2022.csv')
print(df.head())  
print(df.info())
df = df.dropna()  
df['date'] = pd.to_datetime(df['date'])
df['total_production'] = df[['nucleaire', 'renouvelable', 'thermique']].sum(axis=1)
df['part_renouvelable'] = df['renouvelable'] / df['total_production'] * 100
df['part_nucleaire'] = df['nucleaire'] / df['total_production'] * 100
df['mois'] = df['date'].dt.month
consommation_mensuelle = df.groupby('mois')['consommation'].sum()
consommation_mensuelle.plot(kind='bar')
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['part_renouvelable'], label="Part des énergies renouvelables", color='green')
plt.plot(df['date'], df['part_nucleaire'], label="Part du nucléaire", color='blue')
plt.xlabel('Date')
plt.ylabel('Part en %')
plt.title('Part des énergies renouvelables et du nucléaire dans la production d\'électricité')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df_monthly = df.groupby(df['date'].dt.to_period('M')).agg({
    'part_renouvelable': 'mean',
    'part_nucleaire': 'mean'})
plt.figure(figsize=(12, 6))
plt.plot(df_monthly.index.astype(str), df_monthly['part_renouvelable'], label="Part des énergies renouvelables", color='green')
plt.plot(df_monthly.index.astype(str), df_monthly['part_nucleaire'], label="Part du nucléaire", color='blue')
plt.xlabel('Mois')
plt.ylabel('Part en %')
plt.title('Part des énergies renouvelables et du nucléaire dans la production d\'électricité (2022)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()		



		

		
