# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oneway.ui'
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
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st

class Ui_Test_One_Way(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        
        self.resize(627, 391)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(350, 330, 231, 24))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.btnValider.setFont(font)
        self.btnValider.clicked.connect(self.onClickValider)
        
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 220, 171, 21))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.label_8.setFont(font1)
        
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(30, 330, 231, 24))
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 170, 191, 16))
        self.label_7.setFont(font1)
        
        self.cBHypNull = QComboBox(self.centralwidget)
        self.cBHypNull.setObjectName(u"cBHypNull")
        self.cBHypNull.setGeometry(QRect(280, 210, 291, 27))
        self.cBHypNull.setFont(font)
        
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(280, 260, 291, 22))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.spinBox.setFont(font2)
        
        self.cBVarDep = QComboBox(self.centralwidget)
        self.cBVarDep.setObjectName(u"cBVarDep")
        self.cBVarDep.setGeometry(QRect(280, 160, 291, 27))
        self.cBVarDep.setFont(font)
        
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 260, 211, 21))
        self.label_5.setFont(font1)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 20, 211, 21))
        self.label.setFont(font)
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 321, 16))
        self.label_2.setFont(font)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 120, 201, 21))
        self.label_3.setFont(font1)
        
        self.cBVarInd = QComboBox(self.centralwidget)
        self.cBVarInd.setObjectName(u"cBVarInd")
        self.cBVarInd.setGeometry(QRect(280, 110, 291, 27))
        self.cBVarInd.setFont(font)
        
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        #Chargement des variables
        self.cBVarInd.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if (varType != dm.var_qt and dm.dictGlobalData[dm.key_main_data_frame][varName].nunique() > 2))
        
        self.cBVarDep.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        self.cBHypNull.addItems(["moy égale"])
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"One Way ANOVA", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyppoth\u00e8se null :", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Variable D\u00e9pendante : ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test  One Way ANOVA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vararibale Ind\u00e9pendante :", None))
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
        
        variableName_1 = self.cBVarInd.currentText()
        variableName_2 = self.cBVarDep.currentText()
    
        secondaryDataFrame = primaryDataFrame[[variableName_1, variableName_2]]
        if variableName_1 != "" and variableName_2 != "":
            resultats_anova = stats.f_oneway(*[group[variableName_2] for name, group in secondaryDataFrame.groupby(variableName_1)])

            # Calculer les sommes des carrés à partir des données brutes
            groupes = secondaryDataFrame.groupby(variableName_1)[variableName_2]
            moyenne_globale = secondaryDataFrame[variableName_2].mean()
            SS_total = sum((x - moyenne_globale) ** 2 for x in secondaryDataFrame[variableName_2])
            SS_between = sum(len(group) * (group.mean() - moyenne_globale) ** 2 for name, group in groupes)
            SS_within = SS_total - SS_between

            # Calculer les degrés de liberté
            nbrGroups = secondaryDataFrame[variableName_1].nunique()
            df_between = nbrGroups - 1
            df_within = len(secondaryDataFrame[variableName_1]) - nbrGroups
            df_total = len(secondaryDataFrame[variableName_1]) -1

            # Calculer les moyennes des carrés
            MS_between = SS_between / df_between
            MS_within = SS_within / df_within

            # Statistique de test F
            statistique_F = MS_between / MS_within

            # P-value
            p_value = resultats_anova.pvalue
            
            
            
            #Les mesures de dispersion des deux Ration
            """interTitle  = "Mesures de dispersion de {} suivant les modalitées de  {}".format(variableName_2, variableName_1)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [[variableName_1, "N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [groupes_uniques[0],  int(len(variable_1)), rg.formatFloat(np.mean(variable_1)), rg.formatFloat(np.std(variable_1, ddof=1)), rg.formatFloat(stats.sem(variable_1, ddof= 1)), rg.formatFloat(variable_1.min()), rg.formatFloat(variable_1.max())], [groupes_uniques[1], int(len(variable_2)), rg.formatFloat(np.mean(variable_2)), rg.formatFloat(np.std(variable_2, ddof=1)), rg.formatFloat(stats.sem(variable_2, ddof= 1)), rg.formatFloat(variable_2.min()), rg.formatFloat(variable_2.max())]])
            self.refCount= self.refCount +1"""
                
            #Tableau du test One Way ANOVA
            interTitle  = f"Tableau du Test One Way ANOVA sur les variables {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Source", "Somme des carrés (SC)", " DL ", "Variance"], ["Entre Gps", SS_between, df_between, MS_between], ["Interieur Gps", SS_within, df_within, MS_within], ["Total", SS_total,  df_total, " "]])
            self.refCount= self.refCount +1
            
            #Tableau du test de T Student
            interTitle  = f"Tableau 2 du Test One Way ANOVA sur les variables {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["F", "p_value"], [statistique_F, p_value]])
            self.refCount= self.refCount +1
            
            
            # Tests post hoc (si le test ANOVA est significatif)
            seuil = self.spinBox.value()/100
            
            if p_value < seuil:
                # Utilisation du test de Tukey
                posthoc = pairwise_tukeyhsd(secondaryDataFrame[variableName_2], secondaryDataFrame[variableName_1])
                comparisons = posthoc.groupsunique
                p_values_corrected = posthoc.pvalues

                #print("\nTests post hoc (p-valeur corrigée) :")
                post_hoc_list = [["Tests post hoc", "p-valeur corrigée"],]
                for i, comparison in enumerate(comparisons):
                    post_hoc_list.append([f"Comparaison {i + 1} : {comparison}", f"{p_values_corrected[i]}"])
                    #print(f"Comparaison {i + 1} : {comparison}       {p_values_corrected[i]}")
                  
                print(post_hoc_list)
                prod = [['Tests post hoc', 'p-valeur corrigée'], ['Comparaison 1 : 2ER', '0.0004994882587784355'], ['Comparaison 2 : AGE', '0.2890007805793726'], ['Comparaison 3 : IRA', '0.024013283820620512']]
                #Tableau du test de T Student
                interTitle  = f"Tableau du Test de Tukey {variableName_1} et {variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, post_hoc_list)
                self.refCount= self.refCount +1
            
             
            
            #Formatage du Test de T_Student
            testTitle = f"Test One Way ANOVA sur les variables {variableName_1} et {variableName_2}"
            rg.leftDiv = rg.leftDiv + rg.formatTestLeft(testTitle, pointList)
            rg.rightDiv = rg.rightDiv + rg.formatTestRight(testTitle, partieList)

            # Afficher les résultats
            """
            print("Statistique de test F :", statistique_F)
            print("Valeur p :", p_value)
            print("\nTableau ANOVA :")
            print(f"{'Source de variation':<20}{'Degrés de liberté':<20}{'Somme des carrés':<20}{'Moyenne des carrés':<20}")
            print(f"{'Between Groups':<20}{df_between:<20}{SS_between:<20}{MS_between:<20}")
            print(f"{'Within Groups':<20}{df_within:<20}{SS_within:<20}{MS_within:<20}")
            print(f"{'Total':<20}{len(secondaryDataFrame[variableName_2]) - 1:<20}{SS_total:<20}")
            """
            
        #Chargement des Resultats
        rg.refreshHtmlResult()
        self.tabView.setCurrentIndex(2)
        self.webView.reload()
        self.webView.setUrl(QUrl("{}#ref{}".format(rg.resultPath, str(rg.testCouter))))
        self.webView.reload()
        rg.testCouter = rg.testCouter + 1
        self.refCount = 1
        self.close()