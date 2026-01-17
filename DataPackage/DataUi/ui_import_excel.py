import sys

import pandas as pd

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QFile, QTextStream, Slot, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget, QFileDialog, QTableWidget, QTableView, QTableWidgetItem, QComboBox, 
    QListWidget, QListWidgetItem, QVBoxLayout)


from DataPackage import  main_ui
from DataPackage import data_module as dm
from . import pandas_model

class Ui_ImportExcel(QMainWindow):
    
    
    parametresDict = { }
    ui_fixe = None

        
    
    def __init__(self, layout: QVBoxLayout, main_data_table, dictGlobalData,):
        super().__init__()
        
        self.parametresDict = {
                        
                        'texts': ['Feuille', 'En-tete', 'nom', 'colonne ref', 'colonnes'],
                        'keys_list': ['sheet_name', 'header', 'names', 'index_col', 'usecols'],
                        'param_inter': {},
                        'new_values': {'key': 'value'},
                        'default_values': {
                            
                                            'sheet_name': 0,
                                            'header': 0,
                                            'names': None,
                                            'index_col': None,
                                            'usecols': None,
                                            'squeeze': None,
                                            'dtype': None,
                                            'engine': None,
                                            'converters': None,
                                            'true_values': None,
                                            'false_values': None,
                                            'skiprows': None,
                                            'nrows': None,
                                            'na_values': None,
                                            'keep_default_na': True,
                                            'na_filter': True,
                                            'verbose': False,
                                            'parse_dates': False,
                                            'date_parser': None,
                                            'thousands': None,
                                            'decimal': '.',
                                            'skipfooter': 0,
                                            'comment': None,
                                            'convert_float': None,
                                            'mangle_dupe_cols': True,
                                            'storage_options': None,
                                            
                                        }
                        
    }

        
        self.setWindowTitle("Importer DB Excel")
        #self.setWindowModality(Qt.WindowModal)
        self.resize(517, 430)
        
        
        #Partie Centrale
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appliqueStylsheet("DataPackage/DataUi/data_ui_qss.qss")
                
        self.label = QLabel("Importation d'une DB Excel", self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 301, 21))
        print(self.parametresDict['param_inter'])
        
        self.btnValider = QPushButton(self.centralwidget, text= "Valider")
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(133, 370, 100, 27))
        self.btnValider.clicked.connect(lambda j: self.onbtnValider(layout, main_data_table, dictGlobalData, self.lineEditFileName.text()))
        
        self.btnAnnuler = QPushButton(self.centralwidget, text= "Annuler")
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(283, 370, 100, 27))
        self.btnAnnuler.clicked.connect(self.onbtnAnnuler)
        
        
        self.btnChoixFile = QPushButton(self.centralwidget, text= "Choisir")
        self.btnChoixFile.setObjectName(u"btnChoixFile")
        self.btnChoixFile.setGeometry(QRect(390, 90, 91, 27))
        self.btnChoixFile.setStatusTip("Selectionner le fichier Excel")
        self.btnChoixFile.clicked.connect(self.openFile)
        
        self.lineEditFileName = QLineEdit(self.centralwidget)
        self.lineEditFileName.setObjectName(u"lineEditFileName")
        self.lineEditFileName.setGeometry(QRect(30, 90, 331, 27))
        
        self.cbbArg = QComboBox(self.centralwidget)
        self.cbbArg.setObjectName(u"cbbArg")
        self.cbbArg.addItems(self.parametresDict['texts'])
        self.setCbData(self.parametresDict['keys_list'], self.cbbArg)
        self.cbbArg.setGeometry(QRect(30, 190, 211, 27))
        
        self.lineEditArg = QLineEdit(self.centralwidget)
        self.lineEditArg.setObjectName(u"lineEditArg")
        self.lineEditArg.setGeometry(QRect(30, 250, 211, 27))
        
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(280, 130, 201, 161))
        
        self.btnAjouter = QPushButton(self.centralwidget, text ="Ajouter")
        self.btnAjouter.setObjectName(u"btnAjouter")
        self.btnAjouter.setGeometry(QRect(70, 310, 131, 27))
        self.btnAjouter.clicked.connect(self.onaddParameter)
        
        self.btnSupprimer = QPushButton(self.centralwidget, text ="Supprimer")
        self.btnSupprimer.setObjectName(u"btnSupprimer")
        self.btnSupprimer.setGeometry(QRect(320, 310, 131, 27))
        self.btnSupprimer.clicked.connect(self.onremoveParameter)
        
        self.label_2 = QLabel("Paramétre de l'importation", self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 150, 251, 20))
        font = QFont()
        font.setFamilies([u"Century"])
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        
        self.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        
    
    def appliqueStylsheet(self, fileName:str):
        file = QFile(fileName)
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())
        file.close()
        
    @Slot()
    def openFile(self):
        fileName, filter = QFileDialog.getOpenFileName(parent=self, caption="Open Exce File", dir='.', filter='Excel_xlsx (*.xlsx)')
        
        if fileName:
            self.lineEditFileName.setText(fileName)
        else:
            self.setStatusTip("Veillez s'il vous plaît sélectionné un fichier valide")
            
    @Slot()
    def onbtnValider(self,layout, main_data_table, dictGlobalData, path):
        if self.importExcelData(layout, main_data_table, dictGlobalData, path):
            Ui_ImportExcel.ui_fixe.close()
            
        
    @Slot()
    def onbtnAnnuler(self):
        self.close()
       
    @Slot() 
    def importExcelData(self, layout: QVBoxLayout, main_data_table, dictGlobalData, path: str):
        
        charged = False
        
        
        try:
            
            self.parametresDict['new_values'] = self.parametresDict['default_values']
            self.refreshParmeterValue()
            print(self.parametresDict['new_values'])
            
            dictGlobalData[dm.key_main_data_frame] = pd.read_excel(path, sheet_name= self.parametresDict['new_values']['sheet_name'],
                                                    header= self.parametresDict['new_values']['header'],
                                                    names= self.parametresDict['new_values']['names'],
                                                    index_col= self.parametresDict['new_values']['index_col'],
                                                    usecols= self.parametresDict['new_values']['usecols'],
                                                    squeeze= self.parametresDict['new_values']['squeeze'],
                                                    dtype= self.parametresDict['new_values']['dtype'],
                                                    engine= self.parametresDict['new_values']['engine'],
                                                    converters= self.parametresDict['new_values']['converters'],
                                                    true_values= self.parametresDict['new_values']['true_values'],
                                                    false_values= self.parametresDict['new_values']['false_values'],
                                                    skiprows= self.parametresDict['new_values']['skiprows'],
                                                    nrows= self.parametresDict['new_values']['nrows'],
                                                    na_values= self.parametresDict['new_values']['na_values'],
                                                    keep_default_na= self.parametresDict['new_values']['keep_default_na'],
                                                    na_filter= self.parametresDict['new_values']['na_filter'],
                                                    verbose= self.parametresDict['new_values']['verbose'],
                                                    parse_dates= self.parametresDict['new_values']['parse_dates'],
                                                    date_parser= self.parametresDict['new_values']['date_parser'],
                                                    thousands= self.parametresDict['new_values']['thousands'],
                                                    decimal= self.parametresDict['new_values']['decimal'],
                                                    comment= self.parametresDict['new_values']['comment'],
                                                    skipfooter= self.parametresDict['new_values']['skipfooter'],
                                                    convert_float= self.parametresDict['new_values']['convert_float'],
                                                    storage_options= self.parametresDict['new_values']['storage_options'],
                                                    
                                                    )
            
            dictGlobalData[dm.key_main_column_head_list] = dictGlobalData[dm.key_main_data_frame].columns
            
            for column in dictGlobalData[dm.key_main_data_frame].select_dtypes(include=['object', 'category']).columns:
                dictGlobalData[dm.key_main_column_dtype_dict][str(column)] = dm.var_ql
            
            for column in dictGlobalData[dm.key_main_data_frame].select_dtypes(include= ['int64', 'float64', 'int32', 'float32']).columns:
                dictGlobalData[dm.key_main_column_dtype_dict][str(column)] = dm.var_qt
               
            for column in dictGlobalData[dm.key_main_data_frame].select_dtypes(include='bool').columns:
                dictGlobalData[dm.key_main_column_dtype_dict][str(column)] = dm.var_binaire
               
            for column in dictGlobalData[dm.key_main_data_frame]:
                if(dictGlobalData[dm.key_main_data_frame][str(column)].nunique() == 2):
                    dictGlobalData[dm.key_main_column_dtype_dict][str(column)] = dm.var_binaire
              
            for column in dictGlobalData[dm.key_main_data_frame].select_dtypes(include= ['datetime64', 'timedelta']).columns:
                dictGlobalData[dm.key_main_column_dtype_dict][str(column)] = dm.var_temp
               
            print(dictGlobalData[dm.key_main_column_dtype_dict])
            model = pandas_model.pandasModel(dictGlobalData[dm.key_main_data_frame])
            main_data_table = QTableView()
            main_data_table.setModel(model)
            layout.takeAt(0).widget().deleteLater()
            layout.insertWidget(0, main_data_table)
            #layout.replaceWidget(from_= layout.takeAt(0).widget(), to=main_data_table)
            
            
        except FileNotFoundError: 
            
            self.statusbar.showMessage("Le fichier est introuvable!")
        except Exception as e:
            # Capturer n'importe quelle exception et afficher le message d'erreur
            #print("Une erreur s'est produite :", e)
                    
            self.statusbar.showMessage("Erreur lors du chargement du fichier Excel")
            
        
        else:
            charged = True
            
        finally:
            return charged
        
    @Slot()
    def onaddParameter(self):
        if self.lineEditArg.text() != "" and self.parametresDict['param_inter'].get(self.cbbArg.currentData())==None:
            item = QListWidgetItem()
            item.setText("{}:{}".format(self.cbbArg.currentText(), self.lineEditArg.text()))
            self.parametresDict['param_inter'][self.cbbArg.currentData()] = self.lineEditArg.text()
            item.setData(1, "{}".format(self.cbbArg.currentData()))
            self.listWidget.addItem(item)
            print("Parametre inter")
            print(self.parametresDict['param_inter'])
        
    @Slot()
    def onremoveParameter(self):
        self.parametresDict['param_inter'].pop(self.listWidget.currentItem().data(1))
        self.listWidget.currentItem().setHidden(True)
       
    
    def setCbData(self, dataList: list, cb: QComboBox):
        i=0
        for element in dataList:
            cb.setItemData(i, dataList[i])
            i+=1
            
    def refreshParmeterValue(self):
        for k, v in self.parametresDict['param_inter'].items():
            
            if(self.parametresDict['new_values'].get(k, 'inValide')!= 'inValide'):
                
                try:
                    v= int(v)
                except:
                    pass
                finally:
                    self.parametresDict['new_values'][k] = v
                    
    @Slot()
    def createUiIportExcel(cls, layout, main_data_table, dictGlobalData):
    
        Ui_ImportExcel.ui_fixe = Ui_ImportExcel(layout, main_data_table, dictGlobalData)
        Ui_ImportExcel.ui_fixe.setWindowModality(Qt.ApplicationModal)
        Ui_ImportExcel.ui_fixe.show()
        
    createUiIportExcel = classmethod(createUiIportExcel)

        
        
        

        
        
if __name__ == '__main__':
    
        app = QApplication(sys.argv)
        myWindow = Ui_ImportExcel()
        myWindow.show()
        sys.exit(app.exec())
        
    