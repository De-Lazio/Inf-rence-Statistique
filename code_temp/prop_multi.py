import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Création d'un DataFrame exemple
data = {'Groupe_qualitatif': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'Variable_quantitative': [25, 15, 20, 25, 10, 10, 30]}
df = pd.DataFrame(data)

# Affichage du DataFrame
print("Données d'Exemple :")
print(df)

# Regroupement des données par la variable qualitative et calcul des fréquences
grouped_data = df.groupby('Groupe_qualitatif')['Variable_quantitative'].sum()
print("les données", [[45],[50], [55]])
# Effectuer le test de proportion multinomiale (test du chi-squared)
chi2_stat = chi2_contingency([[45],[50], [55]])

# Affichage des résultats
print("\nRésultats du test de proportion multinomiale :")
print(f"Statistique du test chi-squared : {chi2_stat.statistic}")
print(f"P-valeur : {chi2_stat}")

# Tracer un graphique des fréquences observées
labels = grouped_data.index
values = grouped_data.values

plt.bar(labels, values)
plt.xlabel('Groupe qualitatif')
plt.ylabel('Somme de la variable quantitative')
plt.title('Fréquences observées par groupe qualitatif')
plt.show()
