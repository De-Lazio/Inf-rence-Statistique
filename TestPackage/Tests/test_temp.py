# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_test_un_var.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import ( QUrl,Slot)

from PySide6.QtWidgets import ( QMainWindow, QTabWidget)

from PySide6.QtWebEngineWidgets import QWebEngineView

from DataPackage import data_module as dm
from TestPackage.GestionTest import resultats_gest as rg
from scipy import stats
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

class Ui_Test_Mikpor(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        self.onClickValider()
        
    Slot()
    def onClickValider(self):
        
        partieList = ""
        pointList = ""
        
        
        variableName = "Mikpor"
        
        #Parametres
        
        variable = np.linspace(0, 20, 100)
        
        if variableName != "":
            
            
            #Les calcules 
            
            
            
            
            
            
            
            
            
            #Présentation des résultats
            
            if True: #Histogramme
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
            
            if True: #QQplot
                qqplotFileName = "qqplot{}.jpg".format(rg.defRefTestPartie(self.refCount))
                sm.qqplot(variable, xlabel ="Quantiles Théoriques", ylabel= "Quantiles de {}".format(variableName), line="q")
                plt.title("QQ Plot de {}".format(variableName))
                plt.savefig("{}{}".format(rg.grahFolder, qqplotFileName))
                plt.close()
                
                interTitle  = "QQ Plot sur {}".format(variableName)
                pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.graphIconStr)
                partieList = partieList + rg.formatImgPartie(self.refCount, interTitle, partieImg=qqplotFileName)
                self.refCount= self.refCount +1
            
            if True: #Boite
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
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["N_Obs", "Moyenne","Ec_Type", "Err_Type","minimum", "maximum"], [int(len(variable)), rg.formatFloat(np.mean(variable)), rg.formatFloat(10.23), rg.formatFloat(stats.sem(variable, ddof= 1)), rg.formatFloat(variable.min()), rg.formatFloat(variable.max())]])
            self.refCount= self.refCount +1
                
            #Tableau du test de T Student
            interTitle  = "Recapitilatif du test de T Stuedent sur {}".format(variableName)
            pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
            partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "DL", " t ", "p-Value", "IC à {}% /Moy".format(str(2 * 100.0))], ["h0>0", str(12), rg.formatFloat(13.3), rg.formatpValue(100.23), "[{} ; {}]".format(rg.formatFloat(20), rg.formatFloat(50))]])
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