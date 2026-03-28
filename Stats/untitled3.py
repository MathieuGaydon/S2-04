import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Tenrac.csv", skiprows=1)
df['dignite'] = df['dignite'].fillna('Sans Dignité')

groupby2merde = df.groupby(['titre', 'dignite']).size().unstack(fill_value=0)
groupby2merde.plot(kind='bar', stacked=False, figsize=(12, 6), width=0.8)

plt.title('Dignités par catégorie de Titre')
plt.xlabel('Titres des Tenracs')
plt.ylabel('Nombre de membres')
plt.legend(title='Dignités disponibles')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()