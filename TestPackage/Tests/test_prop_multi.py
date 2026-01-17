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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from seaborn_qqplot import pplot
import statistics as st
from scipy.stats import chi2_contingency

class Ui_Test_Prop_Multi(QMainWindow):
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
        
        self.cBHypNull.addItems(["propotions égales"])
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proportion Multinomiale", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyppoth\u00e8se null :", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Variable D\u00e9pendante : ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Seuil de Sigificativit\u00e9 (%) : ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test de proportion multinomiale", None))
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
        
        # Regroupement des données par la variable qualitative et calcul des fréquences
        secondaryDataFrame = primaryDataFrame.groupby(variableName_1)[variableName_2].sum()
        
        if variableName_1 != "" and variableName_2 != "":
             # Effectuer le test de proportion multinomiale (test du chi-squared)
            chi2_stat = chi2_contingency(secondaryDataFrame.values)
            
           
            #Tableau du test One Way ANOVA
            interTitle  = f"Tableau de fréquence"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            
            
            
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, secondaryDataFrame)
            self.refCount= self.refCount +1
            
            #Tableau du test de T Student
            interTitle  = f"Tableau 2 du Test One Way ANOVA sur les variables {variableName_1} et {variableName_2}"
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["F", "p_value"], [statistique_F, p_value]])
            self.refCount= self.refCount +1
            
            
            
        #Chargement des Resultats
        rg.refreshHtmlResult()
        self.tabView.setCurrentIndex(2)
        self.webView.reload()
        self.webView.setUrl(QUrl("{}#ref{}".format(rg.resultPath, str(rg.testCouter))))
        self.webView.reload()
        rg.testCouter = rg.testCouter + 1
        self.refCount = 1
        self.close()