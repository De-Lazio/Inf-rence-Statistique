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

# Création d'une table de contingence
contingency_table = pd.crosstab(df['Groupe_qualitatif'], df['Variable_quantitative'])

# Effectuer le test de proportion multinomiale (test du chi-squared)
chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)

# Affichage des résultats
print("\nRésultats du test de proportion multinomiale :")
print(f"Statistique du test chi-squared : {chi2_stat}")
print(f"P-valeur : {p_val}")
print(f"Degrés de liberté : {dof}")
print("Tableau des valeurs attendues :")
print(expected)

# Tracer un graphique des fréquences observées
labels = contingency_table.index
values = contingency_table.values

plt.bar(labels, values.flatten())
plt.xlabel('Groupe qualitatif')
plt.ylabel('Somme de la variable quantitative')
plt.title('Fréquences observées par groupe qualitatif')
plt.show()