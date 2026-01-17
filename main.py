import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton

from DataPackage import main_ui





if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)
    
    #data_module.load_global_data()
    # On instancie une fenêtre graphique et l'affiche.
    myWindow = main_ui.MyWindow()
    myWindow.showMaximized()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())