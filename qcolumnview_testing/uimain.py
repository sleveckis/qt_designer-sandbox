import sys
from PySide6 import QtCore, QtGui, QtWidgets
from Ui_MainWindow import Ui_MainWindow

class LivingDataBaseModel(QtCore.QAbstractListModel):
    pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Look up meaning of super() in context of multiple inhereitance 
        super().__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        #self.model = LivingDatabaseModel()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
# Pass exit code to system
sys.exit(app.exec())