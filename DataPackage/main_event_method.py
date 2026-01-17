from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QTableWidget, QComboBox, QPlainTextEdit

from TestPackage.GestionTest import test_data as t_data


"""
        Evernement lier au action de la barre de menu principale
"""


"""
        Evernement de l'onglet Test
"""

def cbGpTestChanged(cb_gp_value, are_describ: QPlainTextEdit, cb_test:QComboBox):
        are_describ.setPlainText(t_data.Test.test_groupe_dict[cb_gp_value][t_data.Test.description])
        cb_test.clear()
        cb_test.addItems([value['title'] for value in t_data.Test.test_dict.values() if cb_gp_value in value[t_data.Test.groupe_list]])
        
def cbTestChanged(cb_test_value, are_describ: QPlainTextEdit):
        are_describ.setPlainText(t_data.Test.test_dict[cb_test_value][t_data.Test.description])
        

        