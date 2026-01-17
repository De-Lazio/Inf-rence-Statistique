# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'twoway.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget, QTabWidget)

from PySide6.QtWebEngineWidgets import QWebEngineView

from pandas.core.series import Series
from DataPackage import data_module as dm
from TestPackage.GestionTest import resultats_gest as rg
from TestPackage.GestionTest import test_fonction as tfonc
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st

class Ui_Test_Two_Way(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        
        self.resize(597, 442)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.cBVarInd_2 = QComboBox(self.centralwidget)
        self.cBVarInd_2.setObjectName(u"cBVarInd_2")
        self.cBVarInd_2.setGeometry(QRect(270, 160, 291, 27))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.cBVarInd_2.setFont(font)
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 321, 16))
        self.label_2.setFont(font)
        
        self.cBHypNull = QComboBox(self.centralwidget)
        self.cBHypNull.setObjectName(u"cBHypNull")
        self.cBHypNull.setGeometry(QRect(270, 260, 291, 27))
        self.cBHypNull.setFont(font)
        
        self.cBVarInd_1 = QComboBox(self.centralwidget)
        self.cBVarInd_1.setObjectName(u"cBVarInd_1")
        self.cBVarInd_1.setGeometry(QRect(270, 110, 291, 27))
        self.cBVarInd_1.setFont(font)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 201, 21))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 170, 191, 16))
        self.label_7.setFont(font1)
        
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(20, 380, 231, 24))
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 270, 171, 21))
        self.label_8.setFont(font1)
        
        self.sBSeuil = QSpinBox(self.centralwidget)
        self.sBSeuil.setObjectName(u"sBSeuil")
        self.sBSeuil.setGeometry(QRect(270, 310, 291, 22))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.sBSeuil.setFont(font2)
        
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(340, 380, 231, 24))
        self.btnValider.setFont(font)
        self.btnValider.clicked.connect(self.onClickValider)
        
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 310, 211, 21))
        self.label_5.setFont(font1)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 211, 21))
        self.label.setFont(font)
        
        self.cBVarDep = QComboBox(self.centralwidget)
        self.cBVarDep.setObjectName(u"cBVarDep")
        self.cBVarDep.setGeometry(QRect(270, 210, 291, 27))
        self.cBVarDep.setFont(font)
        
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 220, 191, 16))
        self.label_9.setFont(font1)
        
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        #Chargement des variables
        self.cBVarInd_1.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if (varType != dm.var_qt ))
        
        self.cBVarInd_2.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if (varType != dm.var_qt))
        
        self.cBVarDep.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        self.cBHypNull.addItems(["moy égale"])
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vararibale Ind\u00e9pendante 1 :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Vararibale Ind\u00e9pendante 2 :", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyppoth\u00e8se null :", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test  Two Way ANOVA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Variable D\u00e9pendante : ", None))
    # retranslateUi

    Slot()
    def onClickBtnAnnuler(self):
        self.close()
        
    Slot()
    def onClickValider(self):
        # Séparer les données en deux groupes
        primaryDataFrame = dm.dictGlobalData[dm.key_main_data_frame]
        secondaryDataFrame = {}
        partieList = ""
        pointList = ""
        
        variableName_1 = self.cBVarInd_1.currentText()
        variableName_2 = self.cBVarInd_2.currentText()
        variableName_3 = self.cBVarDep.currentText()
        if(variableName_1 != variableName_2):
            df = primaryDataFrame[[variableName_1, variableName_2, variableName_3]]
            if variableName_1 != "" and variableName_2 != "" and variableName_3 != "":
                
                # Effectuer le test ANOVA à deux facteurs
                modele_anova = ols(f"{variableName_3} ~ {variableName_1} * {variableName_2}", data=df).fit()

                # Récupérer les résultats ANOVA
                resultats_anova = sm.stats.anova_lm(modele_anova)

                # Afficher la table ANOVA complète
                table_anova = resultats_anova[['df', 'sum_sq', 'mean_sq', 'F', 'PR(>F)']]
                source_col = pd.DataFrame({
                    "Source": [variableName_1, variableName_2, f"{variableName_1}: {variableName_2}", "Résidue"]
                })
                #table_anova.reset_index()//Utiliser comme colonne réelle 
                # Changer les index pour utiliser des nombres de 1 à n
                #table_anova.round(4)
                tfonc.round_df_mixt(table_anova)
                table_anova = table_anova.round(4)
                table_anova['index'] = range(0, len(table_anova))
                table_anova = table_anova.set_index('index')
                
                table_anova = pd.concat([source_col, table_anova], axis=1)
                
                #print("Table ANOVA complète:")
                #print(table_anova)
                
                list_table_anova = [["Source", "DL", "Som des carrés", "Moy des carrés", "F", "Pr(>F)"]]
                for index, ligne in table_anova.iterrows():
                    # Convertir la ligne en liste et l'ajouter à la liste de lignes
                    list_table_anova.append(list(ligne))
                            
                #Tableau du test One Way ANOVA
                interTitle  = f"Tableau du Test Two Way ANOVA sur les variables {variableName_1} et {variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle,list_table_anova)
                self.refCount= self.refCount +1
                
                

                # Afficher le résumé du modèle
                """resume_modele = pd.DataFrame({
                    'Statistiques': ['R-squared', 'Adj. R-squared', 'F-statistic', 'Prob (F-statistic)'],
                    'Valeurs': [modele_anova.rsquared, modele_anova.rsquared_adj, modele_anova.fvalue, modele_anova.f_pvalue]
                })
                print("\nRésumé du modèle:")
                print(resume_modele)"""
                #Resumer du test One Way ANOVA
                interTitle  = f"Résmer du Test Two Way ANOVA sur les variables {variableName_1} et {variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle,[['R-squared', 'Adj. R-squared', 'F-statistic', 'Prob (F-statistic)'], tfonc.round_list([modele_anova.rsquared, modele_anova.rsquared_adj, modele_anova.fvalue, modele_anova.f_pvalue])])
                self.refCount= self.refCount +1
                
                

                # Afficher les coefficients pour chaque niveau des facteurs
                print(modele_anova)
                coefficients = modele_anova.params.reset_index()
                coefficients.columns = ['Facteur', 'Coefficient']
                coefficients['Intervalle'] = [f"[{lower}, {upper}]" for lower, upper in zip(modele_anova.conf_int().iloc[:, 0].round(4), modele_anova.conf_int().iloc[:, 1].round(4))]
                #coefficients.round(4)
                coefficients = coefficients.round(4)
                #print("\nCoefficients pour chaque niveau des facteurs:")
                #print(coefficients)
                #Coefficients pour  du test One Way ANOVA
                interTitle  = "Les coefficients pour chaque niveau des facteurs"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["", "Coéficients", "Intervalles"]] + tfonc.df_to_rlist(coefficients))
                self.refCount= self.refCount +1
                
                

                """
                tableau_rejets = [["Facteur", "p_Value"]]
                # Tester l'hypothèse nulle pour chaque facteur
                alpha = self.sBSeuil.value() / 100
                for facteur in [variableName_1, variableName_2, f"{variableName_1}:{variableName_2}"]:
                    if facteur in resultats_anova.index:
                        p_value = resultats_anova.loc[facteur, 'PR(>F)']
                        tableau_rejets.append([facteur, p_value])
                        if p_value < alpha:
                            print(f"\nRejeter l'hypothèse nulle pour {facteur} : au moins une moyenne est différente.")
                            
                            # Tester chaque niveau du facteur
                            niveaux = df[facteur.split(':')[0]].unique()
                            for niveau in niveaux:
                                comparaison = f"{facteur.split(':')[0]} = {niveau}"
                                contrastes = [f"{facteur.split(':')[0]}[T.{niveau}]"]
                                resultat_contraste = modele_anova.f_test(contrastes)
                                
                                #p_value_contraste = resultat_contraste.pvalue
                                tableau_rejets.append([f"{facteur}:{niveau}", resultat_contraste.pvalue])
                                if p_value_contraste < alpha:
                                    print(f"  - Rejeter l'hypothèse nulle pour {comparaison} : la moyenne est différente.")
                                else:
                                    print(f"  - L'hypothèse nulle pour {comparaison} n'est pas rejetée : les moyennes sont similaires.")
                                
                        else:
                            tableau_rejets.append([facteur, "NON"])

                            #print(f"\nL'hypothèse nulle pour {facteur} n'est pas rejetée : les moyennes sont similaires.")
                    else:
                        pass
                        #tableau_rejets.append([facteur, "NON"])
                        
                        #print(f"\nLe facteur {facteur} n'est pas présent dans les résultats ANOVA.")


                interTitle  = "Tester l'hypothèse nulle pour chaque facteur"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, tfonc.round_list_mixt(tableau_rejets))
                self.refCount= self.refCount +1
                
                """
                
                #Formatage du Test de T_Student
                testTitle = f"Test One Way ANOVA sur les variables {variableName_1} et {variableName_2}"
                rg.leftDiv = rg.leftDiv + rg.formatTestLeft(testTitle, pointList)
                rg.rightDiv = rg.rightDiv + rg.formatTestRight(testTitle, partieList)


                #Chargement des Resultats
                rg.refreshHtmlResult()
                self.tabView.setCurrentIndex(2)
                self.webView.reload()
                self.webView.setUrl(QUrl("{}#ref{}".format(rg.resultPath, str(rg.testCouter))))
                self.webView.reload()
                rg.testCouter = rg.testCouter + 1
                self.refCount = 1
                self.close()
                
    
        else:
            self.statusbar.showMessage("Erreur : Même variable indépendante")