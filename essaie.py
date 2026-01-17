import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Exemple de création d'un DataFrame (remplace cela par tes propres données)
data = {
    'facteur1': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'facteur2': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'],
    'variable_dependante': [23, 32, 19, 25, 28, 30, 18, 20, 22]
}
df = pd.DataFrame(data)

# Effectuer le test ANOVA à deux facteurs
modele_anova = ols('variable_dependante ~ facteur1 * facteur2', data=df).fit()

# Récupérer les résultats ANOVA
resultats_anova = sm.stats.anova_lm(modele_anova)

# Afficher la table ANOVA complète
table_anova = resultats_anova[['index', 'df', 'sum_sq', 'mean_sq', 'F', 'PR(>F)']]
print("Table ANOVA complète:")
print(table_anova)
print(type(table_anova))

# Afficher le résumé du modèle
resume_modele = pd.DataFrame({
    'Statistiques': ['R-squared', 'Adj. R-squared', 'F-statistic', 'Prob (F-statistic)'],
    'Valeurs': [modele_anova.rsquared, modele_anova.rsquared_adj, modele_anova.fvalue, modele_anova.f_pvalue]
})
print("\nRésumé du modèle:")
print(resume_modele)

# Afficher les coefficients pour chaque niveau des facteurs
coefficients = modele_anova.params.reset_index()
coefficients.columns = ['Facteur', 'Coefficient']
coefficients['Intervalle'] = [f"[{lower}, {upper}]" for lower, upper in zip(modele_anova.conf_int().iloc[:, 0], modele_anova.conf_int().iloc[:, 1])]
print("\nCoefficients pour chaque niveau des facteurs:")
print(coefficients)

# Tester l'hypothèse nulle pour chaque facteur
alpha = 0.05
for facteur in ['facteur1', 'facteur2', 'facteur1:facteur2']:
    if facteur in resultats_anova.index:
        p_value = resultats_anova.loc[facteur, 'PR(>F)']
        if p_value < alpha:
            print(f"\nRejeter l'hypothèse nulle pour {facteur} : au moins une moyenne est différente.")
            
            # Tester chaque niveau du facteur
            niveaux = df[facteur.split(':')[0]].unique()
            for niveau in niveaux:
                comparaison = f"{facteur.split(':')[0]} = {niveau}"
                contrastes = [f"{facteur.split(':')[0]}[T.{niveau}]"]
                resultat_contraste = modele_anova.f_test(contrastes)
                
                p_value_contraste = resultat_contraste.pvalue
                if p_value_contraste < alpha:
                    print(f"  - Rejeter l'hypothèse nulle pour {comparaison} : la moyenne est différente.")
                else:
                    print(f"  - L'hypothèse nulle pour {comparaison} n'est pas rejetée : les moyennes sont similaires.")
        else:
            print(f"\nL'hypothèse nulle pour {facteur} n'est pas rejetée : les moyennes sont similaires.")
    else:
        print(f"\nLe facteur {facteur} n'est pas présent dans les résultats ANOVA.")
