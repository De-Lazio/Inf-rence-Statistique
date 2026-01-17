
from PySide6.QtCore import (Qt, QRect, Slot)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QMainWindow, QAbstractButton, QApplication, QLabel,
    QPushButton, QStatusBar, QWidget, QComboBox, QFrame, QMenuBar)

from DataPackage import data_module as dm

class Ui_VariableType(QMainWindow):
    
    ui_fixe = None
    
    def __init__(self):
        super().__init__()
        self.setObjectName("VariableType")
        self.setWindowTitle("Type de variables")
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.resize(556, 368)
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.label = QLabel( "Configuration du type de chaque variable", self.centralwidget)
        self.label.setGeometry(QRect(60, 30, 411, 31))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(10, 70, 531, 16))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        
        
        self.label_2 = QLabel("Variable :", self.centralwidget)
        self.label_2.setGeometry(QRect(210, 100, 101, 21))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        
        self.cbVariable = QComboBox(self.centralwidget)
        self.cbVariable.setGeometry(QRect(70, 150, 401, 31))
        font.setPointSize(12)
        self.cbVariable.setFont(font)
        self.cbVariable.setObjectName("cbVariable")
        self.cbVariable.addItems(dm.dictGlobalData[dm.key_main_column_head_list])
        self.cbVariable.currentTextChanged.connect(self.oncbVariableChange)
        
        
        self.label_3 = QLabel("Type de la variable :", self.centralwidget)
        self.label_3.setGeometry(QRect(160, 210, 201, 31))
        font = QFont()
        font.setFamily("Century")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        
        self.cbTypeVariable = QComboBox(self.centralwidget)
        self.cbTypeVariable.setGeometry(QRect(70, 260, 401, 31))
        font.setPointSize(12)
        self.cbTypeVariable.setFont(font)
        self.cbTypeVariable.setObjectName("cbTypeVariable")
        
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 556, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        
    @Slot()
    def oncbVariableChange(self):
        if(dm.dictGlobalData[dm.key_main_data_frame][self.cbVariable.currentText()].dtypes in ['int64', 'int32', 'float64', 'float32']):
            self.cbTypeVariable.clear()
            self.cbTypeVariable.addItems([dm.var_qt, dm.var_ord])
        elif(dm.dictGlobalData[dm.key_main_data_frame][self.cbVariable.currentText()].dtypes in ['object', 'category']):
            self.cbTypeVariable.clear()
            self.cbTypeVariable.addItems([dm.var_ql, dm.var_ord])
        elif(dm.dictGlobalData[dm.key_main_data_frame][self.cbVariable.currentText()].dtypes in ['bool']):
            self.cbTypeVariable.clear()
            self.cbTypeVariable.addItems([dm.var_binaire, dm.var_qt, dm.var_ql, dm.var_ord])
        elif(dm.dictGlobalData[dm.key_main_data_frame][self.cbVariable.currentText()].dtypes in ['bool']):
            self.cbTypeVariable.clear()
            self.cbTypeVariable.addItems([dm.var_binaire, dm.var_qt, dm.var_ql, dm.var_ord])
        elif(dm.dictGlobalData[dm.key_main_data_frame][self.cbVariable.currentText()].dtypes in ['datetime64', 'timedelta']):
            self.cbTypeVariable.clear()
            self.cbTypeVariable.addItems([dm.var_temp , dm.var_ql])

    def createUiConfigVar(cls):
        Ui_VariableType.ui_fixe = Ui_VariableType()
        Ui_VariableType.ui_fixe.setWindowModality(Qt.ApplicationModal)
        Ui_VariableType.ui_fixe.show()
    
    createUiConfigVar = classmethod(createUiConfigVar)    
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_VariableType()
    ui.show()
    sys.exit(app.exec())
