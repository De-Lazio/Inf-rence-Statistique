# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stat_desc.ui'
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
    QWidget, QTabWidget)

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
class Ui_StatDesc(QMainWindow):
    
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        #[value['title'] for value in t_data.Test.test_dict.values() if cb_gp_value in value[t_data.Test.groupe_list]]
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        self.setObjectName(u"MainWindow")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 30, 441, 21))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 321, 16))
        self.label_2.setFont(font)
        
        self.cBNatureVar = QComboBox(self.centralwidget)
        self.cBNatureVar.setObjectName(u"cBNatureVar")
        self.cBNatureVar.setGeometry(QRect(10, 160, 341, 27))
        self.cBNatureVar.setFont(font)
        self.cBNatureVar.addItems(dm.variableTypeList[0:4])
        self.cBNatureVar.currentTextChanged.connect(self.changeNatureVar)
        
        self.cBNomVar = QComboBox(self.centralwidget)
        self.cBNomVar.setObjectName(u"cBNomVar")
        self.cBNomVar.setGeometry(QRect(400, 160, 381, 27))
        self.cBNomVar.setFont(font)
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 201, 16))
        self.label_3.setFont(font)
        
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 130, 181, 16))
        self.label_4.setFont(font)
        
        self.gBCalc = QGroupBox(self.centralwidget)
        self.gBCalc.setObjectName(u"gBCalc")
        self.gBCalc.setGeometry(QRect(20, 270, 331, 231))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.gBCalc.setFont(font1)
        
        self.calcCentiles = QCheckBox(self.gBCalc)
        self.calcCentiles.setObjectName(u"calcCentiles")
        self.calcCentiles.setGeometry(QRect(30, 100, 141, 20))
        self.calcCentiles.setFont(font1)
        self.calcMesureCentrale = QCheckBox(self.gBCalc)
        self.calcMesureCentrale.setObjectName(u"calcMesureCentrale")
        self.calcMesureCentrale.setGeometry(QRect(30, 70, 241, 20))
        self.calcMesureCentrale.setFont(font1)
        self.calcMesDispersion = QCheckBox(self.gBCalc)
        self.calcMesDispersion.setObjectName(u"calcMesDispersion")
        self.calcMesDispersion.setGeometry(QRect(30, 130, 221, 20))
        self.calcMesDispersion.setFont(font1)
        self.label_5 = QLabel(self.gBCalc)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 251, 16))
        self.label_5.setFont(font1)
        self.gBGraph = QGroupBox(self.centralwidget)
        self.gBGraph.setObjectName(u"gBGraph")
        self.gBGraph.setGeometry(QRect(410, 270, 351, 231))
        self.gBGraph.setFont(font1)
        self.graphHisto = QCheckBox(self.gBGraph)
        self.graphHisto.setObjectName(u"graphHisto")
        self.graphHisto.setGeometry(QRect(30, 70, 181, 20))
        self.graphHisto.setFont(font1)
        
        self.graphQQplot = QCheckBox(self.gBGraph)
        self.graphQQplot.setObjectName(u"graphQQplot")
        self.graphQQplot.setGeometry(QRect(30, 100, 241, 20))
        self.graphQQplot.setFont(font1)
        
        
        self.graphBoite = QCheckBox(self.gBGraph)
        self.graphBoite.setObjectName(u"graphBoite")
        self.graphBoite.setGeometry(QRect(30, 130, 221, 20))
        self.graphBoite.setFont(font1)
        
        self.label_6 = QLabel(self.gBGraph)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 251, 16))
        self.label_6.setFont(font1)
        
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(430, 540, 231, 24))
        self.btnValider.setFont(font)
        self.btnValider.clicked.connect(self.onClickValider)
        
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(90, 540, 231, 24))
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 230, 341, 16))
        self.label_7.setFont(font1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
        self.changeNatureVar()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Statistique Descriptive", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Statistique Descriptive de variable quantitative ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Selectionn\u00e9 la variable :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nature de variable : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nom de la variable : ", None))
        self.gBCalc.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.calcCentiles.setText(QCoreApplication.translate("MainWindow", u"Les centiles", None))
        self.calcMesureCentrale.setText(QCoreApplication.translate("MainWindow", u"Mesure de tendance centrale", None))
        self.calcMesDispersion.setText(QCoreApplication.translate("MainWindow", u"Mesure de dispersion", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choix des valeurs \u00e0 calculer: ", None))
        self.gBGraph.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.graphHisto.setText(QCoreApplication.translate("MainWindow", u"Histogramme ", None))
        self.graphBoite.setText(QCoreApplication.translate("MainWindow", u"Bo\u00eete de moustache", None))
        self.graphQQplot.setText(QCoreApplication.translate("MainWindow", u"Q_Q Plot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Choix des graph \u00e0 tracer : ", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Parametr\u00e9 l'annalyse descriptive", None))
    # retranslateU
    def changeNatureVar(self):
        print(dm.dictGlobalData[dm.key_main_column_dtype_dict])
        self.cBNomVar.clear()
        self.cBNomVar.addItems(varName for varName, varType in zip(dm.dictGlobalData[dm.key_main_column_dtype_dict].keys(), dm.dictGlobalData[dm.key_main_column_dtype_dict].values()) if varType == self.cBNatureVar.currentText())
        if self.cBNatureVar.currentText() != "Variable Quantitative":
            self.gBCalc.setDisabled(True)
            self.gBGraph.setDisabled(True)
        else:
            self.gBCalc.setDisabled(False)
            self.gBGraph.setDisabled(False)
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
            interTitle = ""
        
            if self.cBNatureVar.currentText() == "Variable Quantitative":
                #Annalyse descriptive de variable quantitative
                moyenne = np.mean(variable)
                devStd = np.std(variable, ddof=1)
                mediane = np.median(variable)
                cv = (devStd/moyenne) * 100
                ca_pearson = (3/devStd) * (moyenne - mediane)
                
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
                    
                
                #Mesure de tendance centrale
                if self.calcMesureCentrale.isChecked():
                    interTitle  = "Mesure de tendance centrale sur {}".format(variableName)
                    pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                    partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Moy Arth", "Moy Geo", "Moy Har", "Médiane", "Mode"], [rg.formatFloat(moyenne), rg.formatFloat(stats.gmean(variable)), rg.formatFloat(stats.hmean(variable)), rg.formatFloat(mediane), rg.formatFloat(st.mode(variable))]])
                    self.refCount= self.refCount +1
                    
                #Mesure de dispersion -centiles
                if self.calcCentiles.isChecked():
                    interTitle  = "Centiles et étandues sur  {}".format(variableName)
                    pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                    partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["25ème Cen", "50ème Cen", "75ème Cen", "Etendue", "Et_Inter_Qua"], [rg.formatFloat(np.percentile(variable, 25)), rg.formatFloat(np.percentile(variable, 50)), rg.formatFloat(np.percentile(variable, 75)), rg.formatFloat(np.max(variable) - np.min(variable)), rg.formatFloat(np.percentile(variable, 75) - np.percentile(variable, 25))]])
                    self.refCount= self.refCount +1
                    
                if self.calcMesDispersion.isChecked():
                    interTitle  = "Mesures de dispersin sur {}".format(variableName)
                    pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                    partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["N_Obs", "Variance", "Dev_std","Coéf_Var", "CA_Pearson"], [int(len(variable)), rg.formatFloat(np.var(variable, ddof=1)), rg.formatFloat(devStd), rg.formatFloat(cv), rg.formatFloat(ca_pearson)]])
                    self.refCount= self.refCount +1
                    
            else: 
                #Annalyse descriptive de variable Qualitative
                
                #Tableau de fréquence de la variable qualitative
                desc = variable.value_counts()
                tabDesc = [["Valeur", "Frequence"]]
                for line in str(desc).split("\n")[:-1]:
                    tabDesc.append(line.split("    "))
                interTitle  = "Tableau de Fréquence sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
                partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, tabDesc)
                self.refCount= self.refCount +1
                
                #Diagramme en batton su  la variable qualitative
                diabarFileName = "diabar{}.jpg".format(rg.defRefTestPartie(self.refCount))
                #plt.figure().set_figheight(9)
                desc.plot.bar(xlabel=variableName, ylabel= "Fréquence")
                plt.savefig("{}{}".format(rg.grahFolder, diabarFileName))
                plt.close()
                
                interTitle  = "Diagramme en batton sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=diabarFileName)
                self.refCount= self.refCount +1
                
                
            testTitle = "Statisque Descriptive sur {}".format(variableName)
            rg.leftDiv = rg.leftDiv + rg.formatTestLeft(testTitle, pointList)
            rg.rightDiv = rg.rightDiv + rg.formatTestRight(testTitle, partieList)
            
            rg.refreshHtmlResult()
            self.tabView.setCurrentIndex(2)
            self.webView.reload()
            self.webView.setUrl(QUrl("{}#ref{}".format(rg.resultPath, str(rg.testCouter))))
            self.webView.reload()
            rg.testCouter = rg.testCouter + 1
            self.refCount = 1
            self.close()
        
        