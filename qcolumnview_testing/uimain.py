"""
    uimain.py
    02-20-2023
    Author: Leveckis

    Borrowing QAbstractListModel subclassing via 
    https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/
"""


import sys

from PySide6 import QtCore, QtGui, QtWidgets
from Ui_MainWindow import Ui_MainWindow

"""
    Subclass of QAbstractListModel
    Both QColumnView and QListView are built off of QAbstractListModel
    For Testing Purposes I'm going to make both widgets
"""
class LivingDataListModel(QtCore.QAbstractListModel):
    """
        Elsewhere, we'll instantiate with an existing list, or an empty one
    """
    def __init__(self, list=None):
        super().__init__()
        self.list = list or []

    #TODO: I have no idea if these work

    def data(self, index, role):
        # There are other roles outside of 'give me data to display'
        # so we'll specify our type of request when we call the method
        if role == Qt.DisplayRole:
            # Return only the text (forseeably the database name / table name)
            # given the column is always zero in a 1D list, so just return row
            return self.list[index.row()]

    def rowCount(self, index):
        return len(self.list)


"""
    Subclassing from both PySide6 and our module we made from the .ui file
"""
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Ui_MainWindow has no __init__() so I guess it defaults to QMainWindow's constructor
        super().__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        #self.model = LivingDataListModel()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
# Pass exit code to system
sys.exit(app.exec())