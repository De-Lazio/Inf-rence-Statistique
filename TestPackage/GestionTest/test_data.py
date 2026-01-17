class Test:
    
    title ="title"
    description = "description"
    groupe_list = "groupe_list"
    
    gp_stat_desc = "Statistique Descriptive"
    gp_t_normalite = "Test de Normalité"
    gp_t_comp_moy = "Comaparaison de Moyenne"
    gp_ass_1v_qt_2v_ql = "Ass 1 var Quant et 2 var Qual"
    gp_ann_variance = "Annalyse de Variance"
    gp_ann_ass_v_nominal = "Annalyse d'Ass de var Nominales"
    gp_ann_tend_v_ordinal = "Annalyse de tendence de var Ordinale"
    gp_ann_acc_meth_observateur = "Annalyse d'accord entre Méthode et observateur"
    gp_corre_regress = "Correlation et regression"
    
    gp_t_parametrique = "Test parametrique"
    gp_t_non_parametrique = "Test non parametrique"

    gp_t_v_qt = "Test de var Quant"
    gp_t_v_ql = "Test de var Qual"
    gp_t_v_ordinal = "Test de var Ordinale"
    
    
    test_gp_list = [gp_stat_desc, gp_t_normalite, gp_ass_1v_qt_2v_ql, gp_ann_variance, gp_ann_ass_v_nominal, gp_ann_tend_v_ordinal, gp_ann_acc_meth_observateur, gp_corre_regress, gp_t_parametrique, gp_t_non_parametrique, gp_t_v_qt, gp_t_v_ql, gp_t_v_ordinal]
        
    test_groupe_dict = {
        
        gp_stat_desc : {
                        title : gp_stat_desc,
                        description: "Statistique Descriptive"
                    },
        
        gp_t_normalite : {
                        title : gp_t_normalite,
                        description: "Test de Normalité"
                    },
        
        gp_t_comp_moy : {
                        title : gp_t_comp_moy,
                        description: "Annalyse Statistique pour la comparaison de deux ou plusieurs moyenne"
                    },
        
        gp_ass_1v_qt_2v_ql : {
                        title : gp_ass_1v_qt_2v_ql,
                        description : "Association d'une varible quantitative ou ordinale de réponse avec deux variables qualitative binaire"
                    },
        
        gp_ann_variance : {
                        title : gp_ann_variance,
                        description : "Test de comparaison de variance"
                    }, 
        
        gp_ann_ass_v_nominal : {
                        title : gp_ann_ass_v_nominal,
                        description : "Annalyse d'association de variable Nominale"
                    },
        
        gp_ann_tend_v_ordinal : {
                        title : gp_ann_tend_v_ordinal,
                        description: "Annalyse de tendence de variable Ordinale"
                    },
        
        gp_ann_acc_meth_observateur : {
                        title : gp_ann_acc_meth_observateur,
                        description : "Annalyse d'accord entre méthode et observateur"
        },
        
        gp_corre_regress : {
                        title : gp_corre_regress,
                        description : "Correlation et Regression"
        },
        #parametrique ou non 
        gp_t_parametrique : {
                        title : gp_t_parametrique,
                        description : "Les tests paramétriques sont des méthodes statistiques qui supposent une distribution spécifique des données, généralement la distribution normale, et font des hypothèses sur les paramètres de cette distribution. Ces tests sont souvent utilisés pour comparer des moyennes, effectuer des analyses de régression, ou évaluer des relations entre variables, mais ils nécessitent des conditions strictes pour garantir la validité des résultats. Les tests t de Student, l'ANOVA, et les régressions linéaires sont des exemples de tests paramétriques couramment utilisés."
        },
        
        gp_t_non_parametrique : {
                        title : gp_t_non_parametrique,
                        description : "Les tests non paramétriques sont des méthodes statistiques qui ne font pas d'hypothèses strictes sur la distribution des données sous-jacentes. Ils sont souvent utilisés lorsque les conditions des tests paramétriques ne sont pas satisfaites, notamment en présence de données non normalement distribuées. Les tests de Mann-Whitney, de Kruskal-Wallis, et de Wilcoxon sont des exemples de tests non paramétriques couramment employés pour comparer des échantillons, évaluer des tendances, ou explorer des relations entre variables sans exiger des prérequis stricts sur la forme des distributions. Ces tests sont plus robustes face à la violation des hypothèses paramétriques, mais peuvent avoir moins de pouvoir statistique dans certaines situations."
        }, 
        
        #Type de variables
        gp_t_v_qt : {
                        title : gp_t_v_qt,
                        description : "Les tests sur les variables quantitatives"
        }, 
        
        gp_t_v_ql : {
                        title : gp_t_v_ql,
                        description : "Les tests sur les variables qualitative"
        }, 
        
        gp_t_v_ordinal : {
                        title : gp_t_v_ordinal,
                        description : "Les tests sur les variables Ordinales"
        }
        
    }
    
    
    
    
    desc_stat = "Statistique descriptive"
    t_T_1v_qt = "Test de T à une var Quant"
    t_T_2v_qt_Ind = "T de Student à deux échantillons indépendantes"
    t_T_2v_qt_App = "T de Student à deux échantillons appariés"
    t_prop_Bi = "Test de proportion Binomiale"
    t_f_std = "Test de Fisher Standard"
    t_oneway = "Test One Way ANOVA"
    t_twoway = "Test Two Way ANOVA"
    t_ksmirnov = "Test de Kolmogorov-Smirnov"
    t_essaie = "Test de mikpor"
    t_prop_multi = "Test de proportion multinomiale"
    
    
    test_list = [desc_stat, t_T_1v_qt]
    test_dict = {
        
        
        
        desc_stat: { 
                    title: desc_stat, 
                    groupe_list: [gp_stat_desc, gp_t_v_ql, gp_t_v_qt, gp_t_v_ordinal], 
                    description: "Annalyse descriptive d'une variable avec des graphiques à l'ppuis. Elle permet de décrire la variable afin de mieux la comprendre " 
                    
        },
        
        
        t_T_1v_qt: { 
                    title: t_T_1v_qt, 
                    groupe_list: [gp_t_parametrique, gp_t_comp_moy, gp_t_v_qt], 
                    description: "Test de T sur une variable quantitative. Il permet de comparer la moyenne de l'échantillon à une moyenne témoin" 
                
        },
        
        t_T_2v_qt_Ind: { 
                    title: t_T_2v_qt_Ind,
                    groupe_list: [gp_t_parametrique, gp_t_comp_moy, gp_t_v_qt], 
                    description: "Test T de Student pour la comparaison des moyennes de deux echantillons indépendantes" 
                
        },
        
        t_T_2v_qt_App: { 
                    title: t_T_2v_qt_App,
                    groupe_list: [gp_t_parametrique, gp_t_comp_moy, gp_t_v_qt], 
                    description: "Test T de Student pour la comparaison des moyennes de deux echantillons appariés" 
                
        },
        
        t_prop_Bi: { 
                    title: t_prop_Bi,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test de proportion binomiale est utilisé pour déterminer si la proportion d'un événement dans un échantillon est significativement différente d'une valeur attendue. " 
                
        },
        
        t_f_std: { 
                    title: t_f_std,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test de F standard est généralement utilisé pour comparer les variances de deux échantillons. La statistique de test F est calculée comme le rapport des variances de deux échantillons." 
                
        },
        
        t_oneway: { 
                    title: t_oneway,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test One-Way ANOVA compare les moyennes de trois groupes ou plus pour déterminer s'il existe des différences significatives entre eux, basé sur la supposition que les échantillons suivent une distribution normale et que les variances sont homogènes." 
                
        },
         
        
        t_twoway: { 
                    title: t_twoway,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test Two-Way ANOVA (Analyse de la Variance à Deux Facteurs) évalue simultanément l'effet de deux variables indépendantes (facteurs) sur une variable dépendante continue, permettant de déterminer s'il existe une interaction significative entre ces facteurs et s'ils ont des effets significatifs individuels. Il est souvent utilisé pour explorer les influences croisées dans les expérimentations où deux facteurs peuvent affecter la variable mesurée." 
                
        },
        
        
        t_ksmirnov: { 
                    title: t_ksmirnov,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test de Kolmogorov-Smirnov vise à déterminer si un échantillon de données suit une distribution de probabilité spécifiée (généralement la distribution normale, mais cela peut être toute autre distribution)." 
                
        },
        
        t_prop_multi: { 
                    title: t_prop_multi,
                    groupe_list: [gp_t_parametrique, gp_t_v_ql], 
                    description: "Descrition à ajouter plus tard. " 
                
        },
        t_essaie: { 
                    title: t_essaie,
                    groupe_list: [gp_t_parametrique, gp_t_v_qt], 
                    description: "Le test de Mikpor vise à déterminer si un échantillon de données suit une distribution de probabilité spécifiée (généralement la distribution normale, mais cela peut être toute autre distribution)." 
        },
        
        
    }

#print(Test.test_gp_list[0])