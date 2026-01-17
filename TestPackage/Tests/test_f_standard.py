# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_f_standard.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget, QTabWidget)

from PySide6.QtWebEngineWidgets import QWebEngineView

from pandas.core.series import Series
from DataPackage import data_module as dm
from TestPackage.GestionTest import resultats_gest as rg
from scipy.stats import f
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st

class Ui_Test_F_STD(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        
        self.setObjectName(u"MainWindow")
        self.resize(704, 563)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gBGraph = QGroupBox(self.centralwidget)
        self.gBGraph.setObjectName(u"gBGraph")
        self.gBGraph.setGeometry(QRect(140, 340, 331, 161))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(12)
        self.gBGraph.setFont(font)
        
        self.graphHisto_3 = QCheckBox(self.gBGraph)
        self.graphHisto_3.setObjectName(u"graphHisto_3")
        self.graphHisto_3.setGeometry(QRect(30, 40, 181, 20))
        self.graphHisto_3.setFont(font)
        
        self.graphBoite_3 = QCheckBox(self.gBGraph)
        self.graphBoite_3.setObjectName(u"graphBoite_3")
        self.graphBoite_3.setGeometry(QRect(30, 70, 221, 20))
        self.graphBoite_3.setFont(font)
        
        self.graphQQplot_3 = QCheckBox(self.gBGraph)
        self.graphQQplot_3.setObjectName(u"graphQQplot_3")
        self.graphQQplot_3.setGeometry(QRect(30, 100, 241, 20))
        self.graphQQplot_3.setFont(font)
        
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 200, 91, 16))
        self.label_7.setFont(font)
        
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(420, 510, 231, 24))
        self.btnValider.clicked.connect(self.onClickValider)
        
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(14)
        self.btnValider.setFont(font1)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(290, 300, 291, 22))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.spinBox.setFont(font2)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 20, 191, 21))
        self.label.setFont(font1)
        
        self.cBHypNull = QComboBox(self.centralwidget)
        self.cBHypNull.setObjectName(u"cBHypNull")
        self.cBHypNull.setGeometry(QRect(290, 250, 291, 27))
        self.cBHypNull.setFont(font1)
        
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 300, 211, 21))
        self.label_5.setFont(font)
        
        self.cBVarQual = QComboBox(self.centralwidget)
        self.cBVarQual.setObjectName(u"cBVarQual")
        self.cBVarQual.setGeometry(QRect(130, 140, 221, 27))
        self.cBVarQual.setFont(font1)
        
        self.cBVarQt = QComboBox(self.centralwidget)
        self.cBVarQt.setObjectName(u"cBVarQt")
        self.cBVarQt.setGeometry(QRect(130, 190, 221, 27))
        self.cBVarQt.setFont(font1)
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 321, 16))
        self.label_2.setFont(font1)
        
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(40, 510, 231, 24))
        self.btnAnnuler.setFont(font1)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 150, 111, 21))
        self.label_3.setFont(font)
        
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 260, 171, 21))
        self.label_8.setFont(font)
        
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(370, 200, 91, 16))
        self.label_9.setFont(font)
        
        self.cBVar_2 = QComboBox(self.centralwidget)
        self.cBVar_2.setObjectName(u"cBVar_2")
        self.cBVar_2.setGeometry(QRect(470, 190, 221, 27))
        self.cBVar_2.setFont(font1)
        
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 150, 91, 16))
        self.label_4.setFont(font)
        
        self.cBVar_1 = QComboBox(self.centralwidget)
        self.cBVar_1.setObjectName(u"cBVar_1")
        self.cBVar_1.setGeometry(QRect(470, 140, 221, 27))
        self.cBVar_1.setFont(font1)
        
        
        self.rbNonApparie = QRadioButton(self.centralwidget)
        self.rbNonApparie.setObjectName(u"rbNonApparie")
        self.rbNonApparie.setGeometry(QRect(20, 110, 141, 20))
        self.rbNonApparie.setFont(font)
        self.rbNonApparie.setChecked(True)
        self.rbNonApparie.toggled.connect(self.checkNonApparie)
        
        self.rbApparie = QRadioButton(self.centralwidget)
        self.rbApparie.setObjectName(u"rbApparie")
        self.rbApparie.setGeometry(QRect(370, 110, 141, 20))
        self.rbApparie.setFont(font)
        self.rbApparie.toggled.connect(self.checkApparie)
        
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        
        self.checkNonApparie()

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        #Chargement des variables
        self.cBVar_1.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        self.cBVar_2.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        
        #Chargement des variables
        self.cBVarQual.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_binaire)
        
        self.cBVarQt.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        self.cBHypNull.addItems(["moy_R1 = moy_R2"])
        
    # setupUi

    def retranslateUi(self ):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test de F Standard", None))
        self.gBGraph.setTitle(QCoreApplication.translate("MainWindow", u"Choix des graph \u00e0 tracer : ", None))
        self.graphHisto_3.setText(QCoreApplication.translate("MainWindow", u"Histogramme ", None))
        self.graphBoite_3.setText(QCoreApplication.translate("MainWindow", u"Bo\u00eete de moustache", None))
        self.graphQQplot_3.setText(QCoreApplication.translate("MainWindow", u"Q_Q Plot", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Var qt :", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test  de F Standard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Var qual Bin :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyppoth\u00e8se null :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Variable 2 :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Variable 1 :", None))
        self.rbNonApparie.setText(QCoreApplication.translate("MainWindow", u"Non appari\u00e9", None))
        self.rbApparie.setText(QCoreApplication.translate("MainWindow", u"Appari\u00e9", None))
    # retranslateUi

    Slot()
    def checkApparie(self):
        self.cBVar_1.setDisabled(False)
        self.cBVar_2.setDisabled(False)
        self.cBVarQt.setDisabled(True)
        self.cBVarQual.setDisabled(True)
        
    Slot()
    def checkNonApparie(self):
        self.cBVar_1.setDisabled(True)
        self.cBVar_2.setDisabled(True)
        self.cBVarQt.setDisabled(False)
        self.cBVarQual.setDisabled(False)
        
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
        
        if(self.rbNonApparie.isChecked()):
            
            variableName_1 = self.cBVarQual.currentText()
            variableName_2 = self.cBVarQt.currentText()
        
            groupes_uniques = primaryDataFrame[variableName_1].unique()

            # Parcourez les groupes uniques et stockez les données dans le dictionnaire
            
            for groupe in groupes_uniques:
                secondaryDataFrame[groupe] = primaryDataFrame[primaryDataFrame[variableName_1] == groupe][variableName_2]
     
            if variableName_1 != "" and variableName_2 != "":
            
                variable_1 :(Series) = secondaryDataFrame[groupes_uniques[0]].dropna()
                variable_2 :(Series) = secondaryDataFrame[groupes_uniques[1]].dropna()
                data = pd.DataFrame({
                    groupes_uniques[0]: variable_1, 
                    groupes_uniques[1]: variable_2
                })
            
            
        else : 
            variableName_1 = self.cBVar_1.currentText()
            variableName_2 = self.cBVar_2.currentText()
           
            if variableName_1 != "" and variableName_2 != "":
            
                variable_1 :(Series) = primaryDataFrame[variableName_1].dropna()
                variable_2 :(Series) = primaryDataFrame[variableName_2].dropna()
                data = pd.DataFrame({
                    variableName_1: variable_1, 
                    variableName_2: variable_2
                })
            
                
                
        # Calculer les variances
        variance_A = np.var(variable_1, ddof=1)
        variance_B = np.var(variable_2, ddof=1)

        # Calculer la statistique de test F
        statistique_F = variance_A / variance_B

        # Déterminer les degrés de liberté
        ddl_num = len(variable_1) - 1
        ddl_denom = len(variable_2) - 1

        # Calculer la valeur p
        p_value = 1 - f.cdf(statistique_F, ddl_num, ddl_denom)
        
        
        if(self.rbNonApparie.isChecked()):
            
            if self.graphHisto_3.isChecked():
                histoFileName = "hist{}.jpg".format(rg.defRefTestPartie(self.refCount))
                #sns.histplot(variable_1, variable_2, bins=20, kde= True)
                plt.figure()
                plt.title(f"Distribution de {variableName_2}")
                
                plt.subplot(2, 1, 1)  # Deux lignes, une colonne, premier sous-graphique
                sns.histplot(variable_1, alpha= 0.5, label= f"{variableName_1}: {groupes_uniques[0]}", bins=20, kde= True)
                plt.legend(loc="upper right")
                plt.ylabel("Fréquence")
                
                plt.subplot(2, 1, 2)  # Deux lignes, une colonne, deuxième sous-graphique
                sns.histplot(variable_2, alpha= 0.5, label= f"{variableName_2}: {groupes_uniques[1]}", bins=20, kde= True)
                plt.legend(loc="upper right")
                
                plt.xlabel("Valeurs")
                plt.ylabel("Fréquence")
                plt.savefig("{}{}".format(rg.grahFolder, histoFileName))
                plt.close()
                
                interTitle  = "Histogramme de {} suivant les modalitées de  {}".format(variableName_2, variableName_1)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=histoFileName)
                self.refCount= self.refCount +1
            
            if self.graphQQplot_3.isChecked():
                qqplotFileName = "qqplot{}.jpg".format(rg.defRefTestPartie(self.refCount))
                plt.figure(figsize=(10, 5))
                plt.subplot(1,2,1)
                sm.qqplot(variable_1, xlabel ="Quantiles Théoriques", ylabel= "Quantiles de {}".format(f"{variableName_2}: {groupes_uniques[0]}"), line="q")
                plt.title("QQ Plot de {}".format(variableName_1))
                
                plt.subplot(1,2,2)
                sm.qqplot(variable_2, xlabel ="Quantiles Théoriques", ylabel= "Quantiles de {}".format(f"{variableName_2}: {groupes_uniques[1]}"), line="q")
                plt.title("QQ Plot de {}".format(variableName_1))
                
                plt.tight_layout()
                plt.savefig("{}{}".format(rg.grahFolder, qqplotFileName))
                plt.close()
                
                interTitle  = "QQ Plot sur de {} suivant les modalitées de  {}".format(variableName_2, variableName_1)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=qqplotFileName)
                self.refCount= self.refCount +1
            
            if self.graphBoite_3.isChecked():
                boiteFileName = "boite{}.jpg".format(rg.defRefTestPartie(self.refCount))
                
                plt.figure(figsize=(8,6))
                plt.grid(True, linestyle='-', alpha=0.6)
                sns.boxplot(data, width=0.2)
                #primaryDataFrame.boxplot(column = [variableName_1, variableName_2], grid= False)
                plt.title("Boîte à moustache des deux échantillons")
                plt.ylabel(variableName_1)
                plt.xlabel(variableName_2)
                plt.savefig("{}{}".format(rg.grahFolder, boiteFileName))
                plt.close()
                
                interTitle  = "Boite à moustache de {} suivant les modalitées de  {}".format(variableName_2, variableName_1)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=boiteFileName)
                self.refCount= self.refCount +1
                
            #Les mesures de dispersion des deux Ration
            interTitle  = "Mesures de dispersion de {} suivant les modalitées de  {}".format(variableName_2, variableName_1)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [[variableName_1, "N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [groupes_uniques[0],  int(len(variable_1)), rg.formatFloat(np.mean(variable_1)), rg.formatFloat(np.std(variable_1, ddof=1)), rg.formatFloat(stats.sem(variable_1, ddof= 1)), rg.formatFloat(variable_1.min()), rg.formatFloat(variable_1.max())], [groupes_uniques[1], int(len(variable_2)), rg.formatFloat(np.mean(variable_2)), rg.formatFloat(np.std(variable_2, ddof=1)), rg.formatFloat(stats.sem(variable_2, ddof= 1)), rg.formatFloat(variable_2.min()), rg.formatFloat(variable_2.max())]])
            self.refCount= self.refCount +1
                
            #Tableau du test de T Student
            interTitle  = f"Tableau du Test de F standard à deux échantillons appariés de {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "DL num", "DL denom", " F ", "p-Value"], ["moy_R1 = moy_R2", ddl_num, ddl_denom, rg.formatFloat(statistique_F), rg.formatpValue(p_value)]])
            self.refCount= self.refCount +1
            
            #Formatage du Test de T_Student
            testTitle = f"Test de F standard à deux échantillons appariés de {variableName_1} et {variableName_2}"
            rg.leftDiv = rg.leftDiv + rg.formatTestLeft(testTitle, pointList)
            rg.rightDiv = rg.rightDiv + rg.formatTestRight(testTitle, partieList)
                
        else:
            
            if self.graphHisto_3.isChecked():
                histoFileName = "hist{}.jpg".format(rg.defRefTestPartie(self.refCount))
                #sns.histplot(variable_1, variable_2, bins=20, kde= True)
                plt.figure()
                plt.title(f"Distribution de {variableName_1}-{variableName_2}")
                
                plt.subplot(2, 1, 1)  # Deux lignes, une colonne, premier sous-graphique
                sns.histplot(variable_1, alpha= 0.5, label= f"{variableName_1}", bins=20, kde= True)
                plt.legend(loc="upper right")
                plt.ylabel("Fréquence")
                
                plt.subplot(2, 1, 2)  # Deux lignes, une colonne, deuxième sous-graphique
                sns.histplot(variable_2, alpha= 0.5, label= f"{variableName_2}", bins=20, kde= True)
                plt.legend(loc="upper right")
                
                plt.xlabel("Valeurs")
                plt.ylabel("Fréquence")
                plt.savefig("{}{}".format(rg.grahFolder, histoFileName))
                plt.close()
                
                interTitle  = f"Histogramme de {variableName_1} et{variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=histoFileName)
                self.refCount= self.refCount +1
            
            if self.graphQQplot_3.isChecked():
                qqplotFileName = "qqplot{}.jpg".format(rg.defRefTestPartie(self.refCount))
                plt.figure(figsize=(10, 5))
                plt.subplot(2,1,1)
                sm.qqplot(variable_1, xlabel ="Quantiles Théoriques", ylabel= f"Quantiles de {variableName_1}", line="q")
                plt.title("QQ Plot de {}".format(variableName_1))
                
                plt.subplot(2,1,2)
                sm.qqplot(variable_2, xlabel ="Quantiles Théoriques", ylabel= f"Quantiles de {variableName_2}", line="q")
                plt.title("QQ Plot de {}".format(variableName_1))
                
                plt.tight_layout()
                plt.savefig("{}{}".format(rg.grahFolder, qqplotFileName))
                plt.close()
                
                interTitle  = f"QQ Plot sur de {variableName_1} et {variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=qqplotFileName)
                self.refCount= self.refCount +1
            
            if self.graphBoite_3.isChecked():
                boiteFileName = "boite{}.jpg".format(rg.defRefTestPartie(self.refCount))
                
                plt.figure(figsize=(8,6))
                plt.grid(True, linestyle='-', alpha=0.6)
                sns.boxplot(data, width=0.2)
                #primaryDataFrame.boxplot(column = [variableName_1, variableName_2], grid= False)
                plt.title("Boîte à moustache des deux échantillons")
                plt.ylabel(variableName_1)
                plt.xlabel(variableName_2)
                plt.savefig("{}{}".format(rg.grahFolder, boiteFileName))
                plt.close()
                
                interTitle  = "Boite à moustache de {variableName_1} et {variableName_2}"
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=boiteFileName)
                self.refCount= self.refCount +1
            #Les mesures de dispersion des deux Ration
            interTitle  = f"Mesures de dispersion de {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["", "N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [variableName_1,  int(len(variable_1)), rg.formatFloat(np.mean(variable_1)), rg.formatFloat(np.std(variable_1, ddof=1)), rg.formatFloat(stats.sem(variable_1, ddof= 1)), rg.formatFloat(variable_1.min()), rg.formatFloat(variable_1.max())], [variableName_2, int(len(variable_2)), rg.formatFloat(np.mean(variable_2)), rg.formatFloat(np.std(variable_1, ddof=1)), rg.formatFloat(stats.sem(variable_2, ddof= 1)), rg.formatFloat(variable_2.min()), rg.formatFloat(variable_2.max())]])
            self.refCount= self.refCount +1
                
            #Tableau du test de T Student
            interTitle  = f"Tableau du Test de F standard à deux échantillons appariés de {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "DL num", "DL denom", " F ", "p-Value"], ["moy_R1 = moy_R2", ddl_num, ddl_denom, rg.formatFloat(statistique_F), rg.formatpValue(p_value)]])
            self.refCount= self.refCount +1
            
            #Formatage du Test de T_Student
            testTitle = f"Test de F standard à deux échantillons appariés de {variableName_1} et {variableName_2}"
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