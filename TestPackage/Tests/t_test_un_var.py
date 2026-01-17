# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_test_un_var.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform, QDoubleValidator, )
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QWidget, QTabWidget, QLineEdit, QRadioButton)

from PySide6.QtWebEngineWidgets import QWebEngineView

from pandas.core.series import Series
from DataPackage import data_module as dm
from TestPackage.GestionTest import resultats_gest as rg
from scipy import stats
import numpy as np
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st
import matplotlib.pyplot as plt

class Ui_Test_T_Un_Var(QMainWindow):
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
        self.label.setGeometry(QRect(30, 40, 501, 21))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 321, 16))
        self.label_2.setFont(font)
        
        self.cBNomVar = QComboBox(self.centralwidget)
        self.cBNomVar.setObjectName(u"cBNomVar")
        self.cBNomVar.setGeometry(QRect(280, 140, 291, 27))
        self.cBNomVar.setFont(font)
        
        self.gBGraph = QGroupBox("Choix des graphiques à tracer", self.centralwidget)
        self.gBGraph.setObjectName(u"gBGraph")
        self.gBGraph.setGeometry(QRect(30, 300, 250, 181))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.gBGraph.setFont(font1)
        
        self.graphHisto = QCheckBox("Histogramme", self.gBGraph)
        self.graphHisto.setObjectName(u"graphHist")
        self.graphHisto.setGeometry(QRect(30, 40, 181, 30))
        self.graphHisto.setFont(font1)
        
        self.graphBoite = QCheckBox(self.gBGraph)
        self.graphBoite.setObjectName(u"graphBoite")
        self.graphBoite.setGeometry(QRect(30, 70, 221, 20))
        self.graphBoite.setFont(font1)
        
        self.graphQQplot = QCheckBox(self.gBGraph)
        self.graphQQplot.setObjectName(u"graphQQplot")
        self.graphQQplot.setGeometry(QRect(30, 100, 241, 20))
        self.graphQQplot.setFont(font1)
        
        self.gBTestCaude = QGroupBox("Hypothèse null", self.centralwidget)
        self.gBTestCaude.setObjectName(u"gBGraph")
        self.gBTestCaude.setGeometry(QRect(310, 300, 250, 181))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.gBTestCaude.setFont(font1)
        
        self.cbBicaudale = QRadioButton("moy = moy témoin", self.gBTestCaude)
        self.cbBicaudale.setObjectName(u"cbBicaudale")
        self.cbBicaudale.setGeometry(QRect(30, 40, 181, 20))
        self.cbBicaudale.setFont(font1)
        self.cbBicaudale.setChecked(True)
        
        self.cbUnicaudaleG = QRadioButton("moy >= moy témoin", self.gBTestCaude)
        self.cbUnicaudaleG.setObjectName(u"cbUnicaudaleG")
        self.cbUnicaudaleG.setGeometry(QRect(30, 70, 221, 20))
        self.cbUnicaudaleG.setFont(font1)
        
        self.cbUnicaudaleD = QRadioButton("moy <= moy témoin", self.gBTestCaude)
        self.cbUnicaudaleD.setObjectName(u"cbUnicaudaleD")
        self.cbUnicaudaleD.setGeometry(QRect(30, 100, 241, 20))
        self.cbUnicaudaleD.setFont(font1)
        
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
        self.label_3.setGeometry(QRect(70, 150, 111, 16))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 190, 181, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 230, 211, 21))
        self.label_5.setFont(font1)
        self.ledtMoyTemoin = QLineEdit(self.centralwidget)
        self.ledtMoyTemoin.setObjectName(u"ledtMoyTemoin")
        self.ledtMoyTemoin.setGeometry(QRect(280, 190, 291, 22))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.ledtMoyTemoin.setFont(font2)
        self.ledtMoyTemoin.setValidator(QDoubleValidator())
        self.sPSeuil = QSpinBox(self.centralwidget)
        self.sPSeuil.setObjectName(u"sPSeuil")
        self.sPSeuil.setGeometry(QRect(280, 230, 291, 22))
        self.sPSeuil.setFont(font2)
        self.sPSeuil.setMinimum(1)
        self.sPSeuil.setMaximum(99)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        #Chargement des variable
        self.cBNomVar.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == dm.var_qt)
        
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test T de Student", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test T de Student sur une variable quantitative unique", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.graphBoite.setText(QCoreApplication.translate("MainWindow", u"Bo\u00eete de moustache", None))
        self.graphQQplot.setText(QCoreApplication.translate("MainWindow", u"Q_Q Plot", None))
        
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variable :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Moyenne T\u00e9moin :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
    # retranslateUi

    Slot()
    def onClickBtnAnnuler(self):
        self.close()
        
    Slot()
    def onClickValider(self):
        
        partieList = ""
        pointList = ""
        variableName = self.cBNomVar.currentText()
        if variableName != "":
            
            variable :(Series) = dm.dictGlobalData[dm.key_main_data_frame][variableName].dropna()
            nObs = len(variable)
            interTitle = ""
            testLaterale = "two-sided"
            hypNull = "moy = moy temoin"
            
            moyenne = np.mean(variable)
            devStd = np.std(variable, ddof=1)
            
            #t = (np.mean(variable) - self.ledtMoyTemoin.value())/(np.std(variable)* np.sqrt(nObs))
            if self.cbBicaudale.isChecked():
                testLaterale = "two-sided"
                hypNull = self.cbBicaudale.text()
            elif self.cbUnicaudaleG.isChecked():
                testLaterale = "less"
                hypNull = self.cbUnicaudaleG.text()
            elif self.cbUnicaudaleD.isChecked():
                testLaterale = "greater"
                hypNull = self.cbUnicaudaleD.text()
                
            t = stats.ttest_1samp(variable, popmean=float(self.ledtMoyTemoin.text()), alternative=testLaterale)
            degre = float(100.0 - self.sPSeuil.value())/100.0
            interConf= t.confidence_interval(confidence_level= (degre))
            
            if self.graphHisto.isChecked():
                histoFileName = "hist{}.jpg".format(rg.defRefTestPartie(self.refCount))
                sns.histplot(data = variable, bins=20, kde= True)
                plt.title("Histogramme de {}".format(variableName))
                plt.xlabel(variableName)
                plt.ylabel("Fréquence")
                plt.savefig("{}{}".format(rg.grahFolder, histoFileName))
                plt.close()
                
                interTitle  = "Histogramme sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=histoFileName)
                self.refCount= self.refCount +1
            
            if self.graphQQplot.isChecked():
                qqplotFileName = "qqplot{}.jpg".format(rg.defRefTestPartie(self.refCount))
                sm.qqplot(variable, xlabel ="Quantiles Théoriques", ylabel= "Quantiles de {}".format(variableName), line="q")
                plt.title("QQ Plot de {}".format(variableName))
                plt.savefig("{}{}".format(rg.grahFolder, qqplotFileName))
                plt.close()
                
                interTitle  = "QQ Plot sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=qqplotFileName)
                self.refCount= self.refCount +1
            
            if self.graphBoite.isChecked():
                boiteFileName = "boite{}.jpg".format(rg.defRefTestPartie(self.refCount))
                sns.boxplot(y = variable, width=0.2)
                plt.title("Boîte à moustache de {}".format(variableName))
                plt.savefig("{}{}".format(rg.grahFolder, boiteFileName))
                plt.close()
                
                interTitle  = "Boite à moustache sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=boiteFileName)
                self.refCount= self.refCount +1
                
                
            interTitle  = "Mesures de dispersion sur {}".format(variableName)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [int(len(variable)), rg.formatFloat(np.mean(variable)), rg.formatFloat(devStd), rg.formatFloat(stats.sem(variable, ddof= 1)), rg.formatFloat(variable.min()), rg.formatFloat(variable.max())]])
            self.refCount= self.refCount +1
                
            #Tableau du test de T Student
            interTitle  = "Recapitilatif du test de T Stuedent sur {}".format(variableName)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "DL", " t ", "p-Value", "IC à {}% /Moy".format(str(degre * 100.0))], [hypNull, str(t.df), rg.formatFloat(t.statistic), rg.formatpValue(t.pvalue), "[{} ; {}]".format(rg.formatFloat(interConf.low), rg.formatFloat(interConf.high))]])
            self.refCount= self.refCount +1
            
            #Formatage du Test de T_Student
            testTitle = "Test T de Student sur {}".format(variableName)
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