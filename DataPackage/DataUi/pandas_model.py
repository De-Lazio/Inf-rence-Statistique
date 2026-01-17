import sys

import pandas as pd

from PySide6.QtCore import (QAbstractTableModel, Qt)

from PySide6.QtWidgets import (QApplication, QTableView)

class pandasModel(QAbstractTableModel):
    
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
        
    def rowCount(self, parent= None):
        return self._data.shape[0]
    
    def columnCount(self, parent= None):
        return self._data.shape[1]
    
    def data(self, index, role= Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, col, orientation: Qt.Orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            
            if orientation == Qt.Orientation.Horizontal:
                return self._data.columns[col]
            
            if orientation == Qt.Orientation.Vertical:
                return self._data.index[col]
            
        return None
    
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable|Qt.ItemFlag.ItemIsEnabled|Qt.ItemFlag.ItemIsEditable