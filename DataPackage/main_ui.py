# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                         QCursor, QFont, QFontDatabase, QGradient,
                         QIcon, QImage, QKeySequence, QLinearGradient,
                         QPainter, QPalette, QPixmap, QRadialGradient,
                         QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
                             QMenu, QMenuBar, QPushButton, QSizePolicy,
                             QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem, QTableView,
                             QToolBar, QVBoxLayout, QWidget, QLabel, QComboBox, QLayout, QPlainTextEdit, QScrollArea)


from PySide6.QtWebEngineWidgets import QWebEngineView

import os

#from . import main_event_method as eventLoader

from .DataUi import ui_import_excel, ui_import_sql_file, ui_type_variable
from DataPackage import main_event_method
from TestPackage.GestionTest import test_data as t_data
from TestPackage.GestionTest.resultats_gest import refreshHtmlResult
from TestPackage.GestionTest import resultats_gest as rg

from TestPackage.Tests.statdesc import Ui_StatDesc
from TestPackage.Tests.t_test_un_var import Ui_Test_T_Un_Var
from TestPackage.Tests.t_test_deux_var_Ind import Ui_Test_T_Deux_Ech_Ind
from TestPackage.Tests.t_test_deux_var_App import Ui_Test_T_Deux_Ech_App
from TestPackage.Tests.test_proportion_Bi import Ui_Test_Prop_Bi
from TestPackage.Tests.test_f_standard import Ui_Test_F_STD
from TestPackage.Tests.test_oneway import Ui_Test_One_Way
from TestPackage.Tests.test_twoway import Ui_Test_Two_Way
from TestPackage.Tests.test_prop_multi import Ui_Test_Prop_Multi


from TestPackage.Tests.test_temp import Ui_Test_Mikpor

from . import data_module as dm


# On définit une classe de fenêtre par héritage.
class MyWindow(QMainWindow):

    ui_tempo = None
    # Le constructeur de la classe nous permet de changer quelques caractéristiques.
    def __init__(self):
        # Appel au constructeur parent (QMainWindow).
        super().__init__()
        # On change le titre de la fenêtre.
        self.setWindowTitle("Statistique")
        # On change l'icône affichée dans le bandeau supérieur de la fenêtre.
        self.setWindowIcon(QIcon("icons/file.png"))
        # On retaille la fenêtre (800 pixels de large et 600 en hauteur).
        self.resize(800, 600)

        
        #Gestion de la partie centrale de la fenetre principale
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        #Creation des onglet
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")

        #Onglet Base de donnees
        self.tabDB = QWidget()
        self.tabDB.setObjectName(u"tabDB")
        self.verticalLayout_2 = QVBoxLayout(self.tabDB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        dm.dictGlobalData[dm.key_main_table] = QTableWidget()
        self.tableWidgetDB = dm.dictGlobalData[dm.key_main_table]
        self.tableWidgetDB.setObjectName(u"tableWidgetDB")
        
        self.verticalLayout_2.addWidget(self.tableWidgetDB)

        self.hlGestionDB = QHBoxLayout()
        self.hlGestionDB.setObjectName(u"hlGestionDB")

        self.btnAddColumn = QPushButton("Colonne (+)", self.tabDB)
        self.btnAddColumn.setObjectName(u"btnAddColumn")
        self.hlGestionDB.addWidget(self.btnAddColumn)

        self.btnAddLine = QPushButton("Ligne (+)", self.tabDB)
        self.btnAddLine.setObjectName(u"btnAddLine")
        self.hlGestionDB.addWidget(self.btnAddLine)

        self.btnValideDB = QPushButton("Valider DB", self.tabDB)
        self.btnValideDB.setObjectName(u"btnValideDB")
        self.hlGestionDB.addWidget(self.btnValideDB)

        self.btnRemoveColumn = QPushButton("Colonne (-)", self.tabDB)
        self.btnRemoveColumn.setObjectName(u"btnRemoveColumn")
        self.hlGestionDB.addWidget(self.btnRemoveColumn)

        self.btnRemoveLine = QPushButton("Ligne (-)", self.tabDB)
        self.btnRemoveLine.setObjectName(u"btnRemoveLine")
        self.hlGestionDB.addWidget(self.btnRemoveLine)

        self.verticalLayout_2.addLayout(self.hlGestionDB)

        self.tabWidget.addTab(self.tabDB, "Data Base")
        
        
        
        
        
        
        
        
        
        

        #onglet des test statistique
        self.tabTest = QWidget()
        self.tabTest.setObjectName(u"tabTest")
        
        self.vlTestTab = QVBoxLayout(self.tabTest)
        self.vlTestTab.setObjectName(u"vlTestTab")
        
        
        #Contenue de l'onglet Test
        
        self.ztest_label_4 = QLabel(self.tabTest)
        self.ztest_label_4.setText("")
        self.ztest_label_4.setObjectName("label_4")
        self.vlTestTab.addWidget(self.ztest_label_4)
        
        
        self.ztest_label = QLabel("Inférence Statistique", self.tabTest)
        self.ztest_label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.ztest_label.setFont(font)
        self.ztest_label.setStyleSheet("")
        self.ztest_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ztest_label.setObjectName("label")
        self.vlTestTab.addWidget(self.ztest_label)
        
        
        self.ztest_horizontalLayout_2 = QHBoxLayout()
        self.ztest_horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ztest_horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.ztest_cb_gp_test = QComboBox(self.tabTest)
        self.ztest_cb_gp_test.setMaximumSize(QSize(500, 16777215))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(12)
        self.ztest_cb_gp_test.setFont(font)
        self.ztest_cb_gp_test.setStyleSheet("")
        self.ztest_cb_gp_test.setObjectName("cb_gp_test")
        self.ztest_cb_gp_test.addItems(t_data.Test.test_gp_list)
        self.ztest_cb_gp_test.currentTextChanged.connect(lambda x: main_event_method.cbGpTestChanged(str(self.ztest_cb_gp_test.currentText()), self.ztest_plainTextEdit_3, self.ztest_cb_test))
        
        self.ztest_horizontalLayout_2.addWidget(self.ztest_cb_gp_test)
        self.vlTestTab.addLayout(self.ztest_horizontalLayout_2)
        
        self.ztest_horizontalLayout_6 = QHBoxLayout()
        self.ztest_horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ztest_horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.ztest_sc_area_gp_test = QScrollArea(self.tabTest)
        self.ztest_sc_area_gp_test.setMaximumSize(QSize(600, 125))
        self.ztest_sc_area_gp_test.setWidgetResizable(True)
        self.ztest_sc_area_gp_test.setObjectName("sc_area_gp_test")
        
        self.ztest_scrollAreaWidgetContents_3 = QWidget()
        self.ztest_scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 598, 123))
        self.ztest_scrollAreaWidgetContents_3.setStyleSheet("m")
        self.ztest_scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.ztest_plainTextEdit_3 = QPlainTextEdit(self.ztest_scrollAreaWidgetContents_3)
        
        self.ztest_plainTextEdit_3.setGeometry(QRect(0, 0, 600, 131))
        self.ztest_plainTextEdit_3.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(10)
        self.ztest_plainTextEdit_3.setFont(font)
        self.ztest_plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.ztest_plainTextEdit_3.setEnabled(False)
        self.ztest_sc_area_gp_test.setWidget(self.ztest_scrollAreaWidgetContents_3)
        self.ztest_horizontalLayout_6.addWidget(self.ztest_sc_area_gp_test)
        self.vlTestTab.addLayout(self.ztest_horizontalLayout_6)
        
        self.ztest_label_2 = QLabel("Text Statistique", self.tabTest)
        self.ztest_label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.ztest_label_2.setFont(font)
        self.ztest_label_2.setStyleSheet("margin-top:20")
        self.ztest_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ztest_label_2.setObjectName("label_2")
        self.vlTestTab.addWidget(self.ztest_label_2)
        
        self.ztest_horizontalLayout = QHBoxLayout()
        self.ztest_horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ztest_horizontalLayout.setObjectName("horizontalLayout")
        
        self.ztest_cb_test = QComboBox(self.tabTest)
        self.ztest_cb_test.setMaximumSize(QSize(500, 16777215))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(12)
        self.ztest_cb_test.setFont(font)
        self.ztest_cb_test.setStyleSheet("")
        self.ztest_cb_test.setObjectName("cb_test")
        self.ztest_cb_test.currentTextChanged.connect(lambda x: main_event_method.cbTestChanged(str(self.ztest_cb_test.currentText()), self.ztest_plainTextEdit_2))
        self.ztest_horizontalLayout.addWidget(self.ztest_cb_test)
        self.vlTestTab.addLayout(self.ztest_horizontalLayout)
        
        self.ztest_horizontalLayout_4 = QHBoxLayout()
        self.ztest_horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ztest_horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.ztest_sc_area_test = QScrollArea(self.tabTest)
        self.ztest_sc_area_test.setMaximumSize(QSize(600, 125))
        self.ztest_sc_area_test.setWidgetResizable(True)
        self.ztest_sc_area_test.setObjectName("sc_area_test")
        
        self.ztest_scrollAreaWidgetContents_2 = QWidget()
        self.ztest_scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 598, 123))
        self.ztest_scrollAreaWidgetContents_2.setStyleSheet("m")
        self.ztest_scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ztest_plainTextEdit_2 = QPlainTextEdit(self.ztest_scrollAreaWidgetContents_2)
        
        self.ztest_plainTextEdit_2.setGeometry(QRect(0, 0, 600, 131))
        self.ztest_plainTextEdit_2.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(10)
        self.ztest_plainTextEdit_2.setFont(font)
        self.ztest_plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.ztest_plainTextEdit_2.setEnabled(False)
        
        self.ztest_sc_area_test.setWidget(self.ztest_scrollAreaWidgetContents_2)
        self.ztest_horizontalLayout_4.addWidget(self.ztest_sc_area_test)
        self.vlTestTab.addLayout(self.ztest_horizontalLayout_4)
        
        self.ztest_horizontalLayout_3 = QHBoxLayout()
        self.ztest_horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.ztest_horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.ztest_btn_test = QPushButton("Allez au Test", self.tabTest)
        self.ztest_btn_test.setMinimumSize(QSize(0, 55))
        self.ztest_btn_test.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        self.ztest_btn_test.setFont(font)
        self.ztest_btn_test.setStyleSheet("margin-top:20")
        self.ztest_btn_test.setObjectName("btn_test")
        self.ztest_btn_test.clicked.connect(lambda x: self.onClicklancerTest(self= self, testName= self.ztest_cb_test.currentText(), tabView=self.tabWidget, webView=self.webEngineViewResult))
        self.ztest_horizontalLayout_3.addWidget(self.ztest_btn_test)
        
        self.vlTestTab.addLayout(self.ztest_horizontalLayout_3)
        self.ztest_label_3 = QLabel(self.tabTest)
        self.ztest_label_3.setText("")
        self.ztest_label_3.setObjectName("label_3")
        self.vlTestTab.addWidget(self.ztest_label_3)
        
        

        self.tabWidget.addTab(self.tabTest, "Test")
        
        
        
        
        
        
        
        

        #Onglet resultat
        self.tabResult = QWidget()
        self.tabResult.setObjectName(u"tabResult")
        self.verticalLayout_5 = QVBoxLayout(self.tabResult)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0,0,0,0)
        self.webEngineViewResult = QWebEngineView(self.tabResult)
        self.webEngineViewResult.setObjectName(u"webEngineViewResult")
        self.webEngineViewResult.setUrl(QUrl(rg.resultPath))
        
        self.verticalLayout_5.addWidget(self.webEngineViewResult)
        

        self.tabWidget.addTab(self.tabResult, "Resultats")

        self.tabWidget.setCurrentIndex(2)
        #self.tabWidget.setCurrentWidget(self.tabResult)
        self.verticalLayout.addWidget(self.tabWidget)


        self.setCentralWidget(self.centralwidget)

        #Fin de la partie centrale
        
        
        #definition des action de la fenetre principale
        self.actionNouveau = QAction(QIcon("icons/new.png"), "&Nouveau", self)
        self.actionNouveau.setObjectName(u"actionNouveau")
        self.actionNouveau.setShortcut("Ctrl+N")
        self.actionNouveau.setStatusTip("Crée un nouveau Fichier")

        self.actionOuvrir = QAction(QIcon("icons/new.png"), "&Ouvrir", self)
        self.actionOuvrir.setObjectName(u"actionOuvrir")
        self.actionOuvrir.setShortcut("Ctrl+O")
        self.actionOuvrir.setStatusTip("Ouvrir un nouveau Fichier")

        self.actionExcel_Data = QAction(QIcon("icons/new.png"), "&Excel Data", self)
        self.actionExcel_Data.setObjectName(u"actionExcel_Data")
        self.actionExcel_Data.setShortcut("Ctrl+E")
        self.actionExcel_Data.setStatusTip("Importer une base de donnée Excel")
        self.actionExcel_Data.triggered.connect(lambda x:  ui_import_excel.Ui_ImportExcel.createUiIportExcel(self.verticalLayout_2, self.tableWidgetDB, dm.dictGlobalData))

        self.actionSQL_Data = QAction(QIcon("icons/new.png"), "S&QL Data Fichier", self)
        self.actionSQL_Data.setObjectName(u"actionSQL_Data")
        self.actionSQL_Data.setShortcut("Ctrl+Q")
        self.actionSQL_Data.setStatusTip("Importer une base de donnée SQL")
        self.actionSQL_Data.triggered.connect(lambda x:  ui_import_sql_file.createUiIportSQL(self.tableWidgetDB))
        
        self.actionSQL_DData = QAction(QIcon("icons/new.png"), "&Connexion DB SQL", self)
        self.actionSQL_DData.setObjectName(u"actionSQL_Data")
        self.actionSQL_DData.setStatusTip("Importer une base de donnée SQL")

        self.actionTexte_Data = QAction(QIcon("icons/new.png"), "&Texte Data", self)
        self.actionTexte_Data.setObjectName(u"actionTexte_Data")
        self.actionTexte_Data.setStatusTip("Importer une base de donnée Texte")

        self.actionAccess_Data = QAction(QIcon("icons/new.png"), "&Access Data", self)
        self.actionAccess_Data.setObjectName(u"actionAccess_Data")
        self.actionAccess_Data.setStatusTip("Importer une base de donnée Excel")

        self.actionWord = QAction(QIcon("icons/new.png"), "Office &Word", self)
        self.actionWord.setObjectName(u"actionWord")
        self.actionWord.setShortcut("Ctrl+W")
        self.actionWord.setStatusTip("Exporter au format de Office Word")

        self.actionPDF = QAction(QIcon("icons/new.png"), "&PDF", self)
        self.actionPDF.setObjectName(u"actionPDF")
        self.actionPDF.setStatusTip("Exporter au format PDF")

        self.actionHtml = QAction(QIcon("icons/new.png"), "&Web format", self)
        self.actionHtml.setObjectName(u"actionHtml")
        self.actionHtml.setStatusTip("Exporter au format du Web")
        
        #Action du menue Edit
        self.configVar = QAction(QIcon("icons/new.png"), "&Config Variable", self)
        self.configVar.setObjectName(u"cofigVar")
        self.configVar.setStatusTip("Configurer les types des variables")
        self.configVar.setShortcut("Ctrl+C")
        self.configVar.triggered.connect(lambda x: ui_type_variable.Ui_VariableType.createUiConfigVar())

        
        
        #Action du menu visualisation
        self.actionHistogramme = QAction(QIcon("icons/new.png"), "&Histogramme", self)
        self.actionHistogramme.setObjectName(u"actionHistogramme")
        self.actionHistogramme.setStatusTip("Dessiner un Histogramme")

        self.actionCambert = QAction(QIcon("icons/new.png"), "&Camabert", self)
        self.actionCambert.setObjectName(u"actionCambert")
        self.actionCambert.setStatusTip("Dessiner un Camabert")


        
        
        
        

        #Les menus

        #Barre de menu
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 605, 22))

        #menu File
        self.menuFile = self.menubar.addMenu("&File")
        self.menuFile.setObjectName(u"menuFile")

        self.menuFile.addAction(self.actionNouveau)
        self.menuFile.addAction(self.actionOuvrir)
        self.menuFile.addSeparator()

        #menu Importer
        self.menuImporter = self.menuFile.addMenu("&Importer")
        self.menuImporter.setObjectName(u"menuImporter")


        self.menuImporter.addAction(self.actionExcel_Data)
        
        #Sous menu d'importation des DB SQL (ficher ou distant)
        self.menuImporterSQL = self.menuImporter.addMenu("&Importer SQL DB")
        self.menuImporterSQL.setObjectName(u"menuImporter")
        
        self.menuImporterSQL.addAction(self.actionSQL_Data)
        self.menuImporterSQL.addAction(self.actionSQL_DData)
        #Fin de sous menu d'imortation des SQL
        
        self.menuImporter.addAction(self.actionTexte_Data)
        self.menuImporter.addAction(self.actionAccess_Data)


        self.menuFile.addMenu(self.menuImporter)

        #menu Exporter
        self.menuExporter = self.menuFile.addMenu("&Exporter")
        self.menuExporter.setObjectName(u"menuExporter")


        self.menuExporter.addAction(self.actionWord)
        self.menuExporter.addAction(self.actionPDF)
        self.menuExporter.addAction(self.actionHtml)

        
        
        
        #menu Edit
        self.menuEdit = self.menubar.addMenu("E&dit")
        self.menuEdit.setObjectName(u"menuEdit")
        
        self.menuEdit.addAction(self.configVar)

        #menu Visualisation
        self.menuVisualisation = self.menubar.addMenu("&Visualisation")
        self.menuVisualisation.setObjectName(u"menuVisualisation")

        self.menuVisualisation.addAction(self.actionHistogramme)
        self.menuVisualisation.addAction(self.actionCambert)


        #menu Test
        self.menuTest = self.menubar.addMenu("&Test")
        self.menuTest.setObjectName(u"menuTest")

        #menu Theme
        self.menuTheme = self.menubar.addMenu("T&heme")
        self.menuTheme.setObjectName(u"menuTheme")

        #menu Option
        self.menuOption = self.menubar.addMenu("O&ption")
        self.menuOption.setObjectName(u"menuOption")

        self.setMenuBar(self.menubar) # Ajouter la barre des menus


        #barre des status
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar) # Ajouter la barre des status


        #barre d'outils
        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName(u"toolBar")
        self.addToolBar(Qt.TopToolBarArea, self.toolBar) # Ajouter la barre d'outils

        
        QMetaObject.connectSlotsByName(self)
        
        refreshHtmlResult()


    """
        Les actions de l'onget de test statistique
        
    """
    def onClicklancerTest(cls, self, testName: (str), tabView: (QTabWidget), webView: (QWebEngineView)):
        if testName == t_data.Test.desc_stat:
            MyWindow.ui_tempo = Ui_StatDesc(tabView, webView)
        elif testName == t_data.Test.t_T_1v_qt:
            MyWindow.ui_tempo = Ui_Test_T_Un_Var(tabView, webView)
        elif testName == t_data.Test.t_T_2v_qt_Ind:
            MyWindow.ui_tempo = Ui_Test_T_Deux_Ech_Ind(tabView, webView)
        elif testName == t_data.Test.t_T_2v_qt_App:
            MyWindow.ui_tempo = Ui_Test_T_Deux_Ech_App(tabView, webView)
        elif testName == t_data.Test.t_prop_Bi:
            MyWindow.ui_tempo = Ui_Test_Prop_Bi(tabView, webView)
        elif testName == t_data.Test.t_f_std:
            MyWindow.ui_tempo = Ui_Test_F_STD(tabView, webView)
        elif testName == t_data.Test.t_oneway:
            MyWindow.ui_tempo = Ui_Test_One_Way(tabView, webView)
        elif testName == t_data.Test.t_twoway:
            MyWindow.ui_tempo = Ui_Test_Two_Way(tabView, webView)
        elif testName == t_data.Test.t_prop_multi:
            MyWindow.ui_tempo = Ui_Test_Prop_Multi(tabView, webView)
            
        elif testName == t_data.Test.t_essaie:
            MyWindow.ui_tempo = Ui_Test_Mikpor(tabView, webView)
            
        MyWindow.ui_tempo.setWindowModality(Qt.WindowModality.WindowModal)
        MyWindow.ui_tempo.show()
        
    onClicklancerTest = classmethod(onClicklancerTest)
        

        