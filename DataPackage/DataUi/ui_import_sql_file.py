import sys

import sqlite3

import openpyxl

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QFile, QTextStream, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)


from DataPackage import main_ui


class Ui_ImportSQL(QMainWindow):
    def __init__(self, tableWidget: QTableWidget):
        super().__init__()
        
        self.setWindowTitle("Charger un fichier DB SQL")
        #self.setWindowModality(Qt.WindowModal)
        self.resize(517, 315)
        
        
        #Partie Centrale
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appliqueStylsheet("DataPackage/DataUi/data_ui_qss.qss")
                
        self.label = QLabel("Importation d'une DB SQL", self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 300, 24))
        
        self.btnValider = QPushButton(self.centralwidget, text= "Valider")
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(250, 250, 111, 31))
        self.btnValider.clicked.connect(lambda j: self.onbtnValider(tableWidget, self.lineEditFileName.text()))
        
        self.btnAnnuler = QPushButton(self.centralwidget, text= "Annuler")
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(390, 250, 111, 31))
        self.btnAnnuler.clicked.connect(self.onbtnAnnuler)
        
        
        self.btnChoixFile = QPushButton(self.centralwidget, text= "Choisir")
        self.btnChoixFile.setObjectName(u"btnChoixFile")
        self.btnChoixFile.setGeometry(QRect(380, 130, 91, 31))
        self.btnChoixFile.setStatusTip("Selectionner le fichier SQL")
        self.btnChoixFile.clicked.connect(self.openFile)
        
        self.lineEditFileName = QLineEdit(self.centralwidget)
        self.lineEditFileName.setObjectName(u"lineEditFileName")
        self.lineEditFileName.setGeometry(QRect(50, 130, 301, 31))
        
        self.label_2 = QLabel(self.centralwidget, text="Nom de la table :")
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 190, 91, 21))
        
        self.ledtTableName = QLineEdit(self.centralwidget)
        self.ledtTableName.setObjectName(u"ledtTableName")
        self.ledtTableName.setGeometry(QRect(170, 187, 301, 25))
        
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
    def onbtnValider(self, tableWidget, path):
        if self.importExcelData(tableWidget, path):
            main_ui.dictMainUi["UiImportSQLFile"].close()
            main_ui.dictMainUi.pop("UiImportSQLFile")
        
    @Slot()
    def onbtnAnnuler(self, ):
        main_ui.dictMainUi["UiImportSQLFile"].close()
        main_ui.dictMainUi.pop("UiImportSQLFile")
       
       
    @Slot() 
    def importSQLData(self, tableWidget: QTableWidget, path: str, tableName: str):
        
        charged = False
        
        try:
            
            connection = sqlite3.connect(path) #Connection à la base de donnée 
            
            query = f'SELECT * FROM D:\De_Lazio\Workspace\pycharmeWorkspace\elearning\db.sqlite3'
            
            result:list = connection.execute(query) #Recuperation des imformation de la base de donnée
            
            
            tableWidget.clear()
            tableWidget.setRowCount(len(result[0]))
            tableWidget.setColumnCount(len(result))

            listValues = list(result)

            tableWidget.setHorizontalHeaderLabels(listValues[0])

            rowIndex = 0
            for valuesTuple in listValues[1:]:
            
                columnIndex = 0
                for value in valuesTuple:
                    tableWidget.setItem(rowIndex, columnIndex, QTableWidgetItem(str(value)))
                    columnIndex +=1
            
                rowIndex += 1
        
        except: 
            
            self.statusbar.showMessage("Erreur lors du chargement du fichier SQL")
        
        else:
            charged = True
            
        finally:
            return charged
   
        

@Slot()
def createUiIportSQL(tableWidget: QTableWidget):
    
    if main_ui.dictMainUi.get("UiImportSQLFile") == None:
        main_ui.dictMainUi["UiImportSQLFile"] = Ui_ImportSQL(tableWidget)
        main_ui.dictMainUi["UiImportSQLFile"].show()
    
if __name__ == '__main__':
    
        app = QApplication(sys.argv)
        myWindow = Ui_ImportSQL()
        myWindow.show()
        sys.exit(app.exec())
        
    