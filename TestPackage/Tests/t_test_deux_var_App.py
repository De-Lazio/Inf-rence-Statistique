# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_test_deux_var_Ind.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QWidget, QTabWidget, QLineEdit)

from PySide6.QtWebEngineWidgets import QWebEngineView

from pandas.core.series import Series
from DataPackage import data_module as dm
from TestPackage.GestionTest import resultats_gest as rg
from scipy import stats
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st
import matplotlib.pyplot as plt

class Ui_Test_T_Deux_Ech_App(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        self.resize(601, 567)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 501, 21))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 321, 16))
        self.label_2.setFont(font)
        self.cBNomVar_1 = QComboBox(self.centralwidget)
        self.cBNomVar_1.setObjectName(u"cBNomVar_1")
        self.cBNomVar_1.setGeometry(QRect(280, 160, 291, 27))
        self.cBNomVar_1.setFont(font)
        self.cBNomVar_1.currentTextChanged.connect(self.variableUnChoisi)
        
        self.gBGraph = QGroupBox(self.centralwidget)
        self.gBGraph.setObjectName(u"gBGraph")
        self.gBGraph.setGeometry(QRect(130, 350, 331, 161))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.gBGraph.setFont(font1)
        self.graphHisto = QCheckBox(self.gBGraph)
        self.graphHisto.setObjectName(u"graphHisto")
        self.graphHisto.setGeometry(QRect(30, 40, 181, 20))
        self.graphHisto.setFont(font1)
        self.graphBoite = QCheckBox(self.gBGraph)
        self.graphBoite.setObjectName(u"graphBoite")
        self.graphBoite.setGeometry(QRect(30, 70, 221, 20))
        self.graphBoite.setFont(font1)
        self.graphQQplot = QCheckBox(self.gBGraph)
        self.graphQQplot.setObjectName(u"graphQQplot")
        self.graphQQplot.setGeometry(QRect(30, 100, 241, 20))
        self.graphQQplot.setFont(font1)
        
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(310, 520, 231, 24))
        self.btnValider.setFont(font)
        self.btnValider.clicked.connect(self.onClickValider)
        
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(30, 520, 231, 24))
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 170, 111, 16))
        self.label_3.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 310, 211, 21))
        self.label_5.setFont(font1)
        self.sPSeuil = QSpinBox(self.centralwidget)
        self.sPSeuil.setObjectName(u"sPSeuil")
        self.sPSeuil.setGeometry(QRect(280, 310, 291, 22))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.sPSeuil.setFont(font2)
        self.cBNomVar_2 = QComboBox(self.centralwidget)
        self.cBNomVar_2.setObjectName(u"cBNomVar_2")
        self.cBNomVar_2.setGeometry(QRect(280, 210, 291, 27))
        self.cBNomVar_2.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 220, 111, 16))
        self.label_7.setFont(font1)
        self.cBHypNull = QComboBox(self.centralwidget)
        self.cBHypNull.setObjectName(u"cBHypNull")
        self.cBHypNull.setGeometry(QRect(280, 260, 291, 27))
        self.cBHypNull.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 270, 171, 21))
        self.label_8.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 120, 211, 16))
        self.label_4.setFont(font1)
        self.ledtVarQtName = QLineEdit(self.centralwidget)
        self.ledtVarQtName.setObjectName(u"ledtVarQtName")
        self.ledtVarQtName.setGeometry(QRect(280, 110, 291, 25))
        self.ledtVarQtName.setFont(font2)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        #Chargement des variables
        self.cBNomVar_1.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
        #self.cBNomVar_2.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        self.variableUnChoisi()
        self.cBHypNull.addItems(["moy_R1 = moy_R2", "moy_R1 >= moy_R2", "moy_R1 <= moy_R2"])
        
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test T de Student", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test T de Student sur deux echantillons independantes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.gBGraph.setTitle(QCoreApplication.translate("MainWindow", u"Choix des graph \u00e0 tracer : ", None))
        self.graphHisto.setText(QCoreApplication.translate("MainWindow", u"Histogramme ", None))
        self.graphBoite.setText(QCoreApplication.translate("MainWindow", u"Bo\u00eete de moustache", None))
        self.graphQQplot.setText(QCoreApplication.translate("MainWindow", u"Q_Q Plot", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ration 1 :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ration 2 :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyppoth\u00e8se null :", None))
    # retranslateUi

    def variableUnChoisi(self):
        self.cBNomVar_2.clear()
        ncount = len(dm.dictGlobalData[dm.key_main_data_frame][self.cBNomVar_1.currentText()].dropna())
        varQtList = list(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        v2_df = dm.dictGlobalData[dm.key_main_data_frame][varQtList].loc[:, dm.dictGlobalData[dm.key_main_data_frame][varQtList].apply(lambda col: col.dropna().size == ncount)]
        self.cBNomVar_2.addItems(v2_df.columns.tolist())
        
    Slot()
    def onClickBtnAnnuler(self):
        self.close()
        
    Slot()
    def onClickValider(self):
        
        partieList = ""
        pointList = ""
        variableQtName = self.ledtVarQtName.text()
        variableName_1 = self.cBNomVar_1.currentText()
        variableName_2 = self.cBNomVar_2.currentText()
        if variableName_1 != "" and variableName_2 != "":
            
            variable_1 :(Series) = dm.dictGlobalData[dm.key_main_data_frame][variableName_1].dropna()
            variable_2 :(Series) = dm.dictGlobalData[dm.key_main_data_frame][variableName_2].dropna()
            data = pd.DataFrame({
                variableName_1: variable_1, 
                variableName_2: variable_2
            })
            diffVar = variable_1 -variable_2
            diffVarName = "{} - {}".format(variableName_1, variableName_2)
            
            nObs = len(diffVar)
            interTitle = ""
            testLaterale = "two-sided"
            hypNull = "moy = moy temoin"
            
            moyenne = np.mean(diffVar)
            devStd = np.std(diffVar, ddof=1)
            
            #Determination de l'hypothèse null
            hypNull = self.cBHypNull.currentText()
            if hypNull == "moy_R1 = moy_R2":
                testLaterale = "two-sided"
            elif hypNull == "moy_R1 <= moy_R2":
                testLaterale = "less"
            elif hypNull == "moy_R1 >= moy_R2":
                testLaterale = "greater"
              
            #Calcul du test statistique  
            t = stats.ttest_rel(variable_1, variable_2, alternative=testLaterale)
            degre = float(100.0 - self.sPSeuil.value())/100.0
            interConf= t.confidence_interval(confidence_level= (degre))
            
            if self.graphHisto.isChecked():
                histoFileName = "hist{}.jpg".format(rg.defRefTestPartie(self.refCount))
                #sns.histplot(variable_1, variable_2, bins=20, kde= True)
                plt.figure(figsize=(8,6))
                sns.histplot(variable_1, alpha= 0.5, label= variableName_1, bins=20, kde= True)
                sns.histplot(variable_2, alpha= 0.5, label= variableName_2, bins=20, kde= True)
                plt.legend(loc="upper right")
                plt.title("Histogramme des deux échantillons")
                plt.xlabel("Valeurs")
                plt.ylabel("Fréquence")
                plt.savefig("{}{}".format(rg.grahFolder, histoFileName))
                plt.close()
                
                interTitle  = "Histogramme sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=histoFileName)
                self.refCount= self.refCount +1
                
            if self.graphQQplot.isChecked():
                qqplotFileName = "qqplot{}.jpg".format(rg.defRefTestPartie(self.refCount))
                sm.qqplot(diffVar, xlabel ="Quantiles Théoriques", ylabel= "Quantiles de {}".format(diffVarName), line="q")
                plt.title("QQ Plot de {}".format(diffVarName))
                plt.savefig("{}{}".format(rg.grahFolder, qqplotFileName))
                plt.close()
                
                interTitle  = "QQ Plot sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=qqplotFileName)
                self.refCount= self.refCount +1
            
            if self.graphBoite.isChecked():
                boiteFileName = "boite{}.jpg".format(rg.defRefTestPartie(self.refCount))
                
                plt.figure(figsize=(8,6))
                sns.boxplot(data, width=0.2)
                #dm.dictGlobalData[dm.key_main_data_frame].boxplot(column = [variableName_1, variableName_2], grid= False)
                plt.title("Boîte à moustache des deux échantillons")
                plt.ylabel(variableQtName)
                plt.savefig("{}{}".format(rg.grahFolder, boiteFileName))
                plt.close()
                
                interTitle  = "Boite à moustache sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=boiteFileName)
                self.refCount= self.refCount +1
                
                
            interTitle  = "Mesures de dispersion sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Groupe", "N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [variableName_1, int(len(variable_1)), rg.formatFloat(np.mean(variable_1)), rg.formatFloat(np.std(variable_1, ddof=1)), rg.formatFloat(stats.sem(variable_1, ddof= 1)), rg.formatFloat(variable_1.min()), rg.formatFloat(variable_1.max())], [variableName_2, int(len(variable_2)), rg.formatFloat(np.mean(variable_2)), rg.formatFloat(np.std(variable_2, ddof=1)), rg.formatFloat(stats.sem(variable_2, ddof= 1)), rg.formatFloat(variable_2.min()), rg.formatFloat(variable_2.max())], [diffVarName, int(len(diffVar)), rg.formatFloat(np.mean(diffVar)), rg.formatFloat(devStd), rg.formatFloat(stats.sem(diffVar, ddof= 1)), rg.formatFloat(diffVar.min()), rg.formatFloat(diffVar.max())]])
            self.refCount= self.refCount +1
                
            #Tableau du test de T Student
            interTitle  = "Tableau du test T Stuedent à deux échantillons appariés sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "DL", " t ", "p-Value", "IC à {}% /diffMoy".format(str(degre * 100.0))], [hypNull, str(t.df), rg.formatFloat(t.statistic), rg.formatpValue(t.pvalue), "[{} ; {}]".format(rg.formatFloat(interConf.low), rg.formatFloat(interConf.high))]])
            self.refCount= self.refCount +1
            
            #Formatage du Test de T_Student
            testTitle = "T Stuedent à deux échantillons appariés sur {} de {} et {}".format(variableQtName, variableName_1, variableName_2)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
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