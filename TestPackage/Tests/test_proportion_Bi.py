# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_proportion_Bi.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget, QTabWidget)

from PySide6.QtWebEngineWidgets import QWebEngineView

from TestPackage.GestionTest import resultats_gest as rg
from scipy import stats

class Ui_Test_Prop_Bi(QMainWindow):
    def __init__(self, tabView: (QTabWidget), webView: (QWebEngineView)):
        super().__init__()
        
        self.refCount = 1
        self.tabView = tabView
        self.webView = webView
        
        self.resize(571, 509)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnAnnuler = QPushButton(self.centralwidget)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(30, 450, 231, 24))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setPointSize(14)
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.clicked.connect(self.onClickBtnAnnuler)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 501, 21))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 321, 16))
        self.label_2.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 100, 331, 16))
        font1 = QFont()
        font1.setFamilies([u"Century"])
        font1.setPointSize(12)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 150, 331, 41))
        self.label_5.setFont(font1)
        self.ledtNEvent = QLineEdit(self.centralwidget)
        self.ledtNEvent.setObjectName(u"ledtNEvent")
        self.ledtNEvent.setGeometry(QRect(370, 150, 181, 25))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.ledtNEvent.setFont(font2)
        self.ledtNObs = QLineEdit(self.centralwidget)
        self.ledtNObs.setObjectName(u"ledtNObs")
        self.ledtNObs.setGeometry(QRect(370, 90, 181, 25))
        self.ledtNObs.setFont(font2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 210, 331, 41))
        self.label_6.setFont(font1)
        self.btnValider = QPushButton(self.centralwidget)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(310, 450, 231, 24))
        self.btnValider.setFont(font)
        self.btnValider.clicked.connect(self.onClickValider)
        
        self.sPProp = QDoubleSpinBox(self.centralwidget)
        self.sPProp.setObjectName(u"sPProp")
        self.sPProp.setGeometry(QRect(370, 210, 181, 25))
        self.sPProp.setFont(font2)
        self.sPProp.setMaximum(1.000000000000000)
        self.sPProp.setSingleStep(0.010000000000000)
        self.sPProp.setStepType(QAbstractSpinBox.DefaultStepType)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 310, 191, 21))
        self.label_7.setFont(font1)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(220, 310, 331, 121))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 260, 321, 21))
        self.label_8.setFont(font1)
        self.sPSeuil = QSpinBox(self.centralwidget)
        self.sPSeuil.setObjectName(u"sPSeuil")
        self.sPSeuil.setGeometry(QRect(370, 260, 181, 22))
        self.sPSeuil.setMinimum(1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test de proportion binomiale ou de proportion sp\u00e9cifi\u00e9e", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test de proportion binomiale ou de proportion sp\u00e9cifi\u00e9e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parametre du Test", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre d'Observations  avec l'evernement :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre d'Observations  l'\u00e9vernement s'est :\n"
"produit l'evernement", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Proportion attendue (Hypoth\u00e8se nulle) :", None))
        self.btnValider.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Commentaire sur le test : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Seuil de significativit\u00e9", None))
    # retranslateUi


    Slot()
    def onClickBtnAnnuler(self):
        self.close()
        
    Slot()
    def onClickValider(self):
        
        partieList = ""
        pointList = ""
        
        succes = int(self.ledtNEvent.text())
        observation = int(self.ledtNObs.text())
        prop_attendu = self.sPProp.value()
        seuil = self.sPSeuil.value()
        hypNull = "prop = {}".format(str(prop_attendu))
        t = stats.binomtest(succes, observation, prop_attendu)
        degre = float(100.0 - seuil)/100.0
        interConf = t.proportion_ci(confidence_level=degre)
        print(t)
        
        
        #Tableau du test de T Student
        interTitle  = "Recapitilatif du test de proportion Binomiale"
        pointList = pointList + rg.formatPoint(self.refCount, interTitle, rg.tableaIconStr)
        partieList = partieList + rg.formatTableHPartie(self.refCount, interTitle, [["Hyp_null", "Nobs","NEvent_prod", " t ", "p-Value", "IC à {}% /Moy".format(str(int(degre * 100.0)))], [hypNull, observation, succes, rg.formatFloat(t.statistic), rg.formatpValue(t.pvalue), "[{} ; {}]".format(rg.formatFloat(interConf.low), rg.formatFloat(interConf.high))]])
        partieList = partieList + "<br><br><u>Commentaire : </u><br><br>{}".format(self.plainTextEdit.toPlainText())
        self.refCount= self.refCount +1
        
        #Formatage du Test de T_Student
        testTitle = "Test de proportion Binomiale"
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