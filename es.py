import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from tabulate import tabulate  # Assure-toi d'installer cette bibliothèque avec pip install tabulate

# Exemple de DataFrame avec deux facteurs
df = pd.DataFrame({
    'Facteur_1': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'Facteur_2': ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'X'],
    'Variable_Dépendante': [23, 32, 19, 25, 28, 30, 18, 20, 22]
})

# Modèle avec interaction entre les deux facteurs
modele_anova = ols('Variable_Dépendante ~ Facteur_1 * Facteur_2', data=df).fit()

# Tableau des coefficients
coefficients = pd.DataFrame(modele_anova.params, columns=['Coefficient'])

# Résultats ANOVA
resultats_anova = anova_lm(modele_anova)

# Afficher les résultats sous forme de tableau
tableau_resultats = tabulate(resultats_anova, headers='keys', tablefmt='pretty', showindex=True)
print("\nRésultats de l'ANOVA :")
print(tableau_resultats)

# Tester l'hypothèse nulle pour chaque facteur
alpha = 1
tableau_rejets = []

for facteur in ['facteur1', 'facteur2', "facteur1:facteur2"]:
    if facteur in resultats_anova.index:
        p_value = resultats_anova.loc[facteur, 'PR(>F)']
        rejet_hypothese = p_value < alpha

        # Ajouter l'information au tableau des rejets d'hypothèse
        tableau_rejets.append({
            'Facteur': facteur,
            'P-value': p_value,
            'Rejet hypothèse nulle': rejet_hypothese
        })

        if rejet_hypothese:
            # Tester chaque niveau du facteur
            niveaux = df[facteur.split(':')[0]].unique()
            for niveau in niveaux:
                comparaison = f"{facteur.split(':')[0]} = {niveau}"
                contrastes = [f"{facteur.split(':')[0]}[T.{niveau}]"]
                resultat_contraste = modele_anova.f_test(contrastes)

                p_value_contraste = resultat_contraste.pvalue
                rejet_hypothese_contraste = p_value_contraste < alpha

                # Ajouter l'information au tableau des rejets d'hypothèse
                tableau_rejets.append({
                    'Facteur': comparaison,
                    'P-value': p_value_contraste,
                    'Rejet hypothèse nulle': rejet_hypothese_contraste
                })

# Afficher le tableau des rejets d'hypothèse
print("\nTableau des rejets d'hypothèse :")
tableau_rejets_df = pd.DataFrame(tableau_rejets)
print(tabulate(tableau_rejets_df, headers='keys', tablefmt='pretty', showindex=False))
