"""
    uimain.py
    02-20-2023
    Author: Leveckis

    Borrowing QAbstractListModel subclassing via 
    https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/
"""


import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from Ui_MainWindow import Ui_MainWindow
from DatabaseConnect import connect_and_return_databases

"""
    Subclass of QAbstractListModel
    Both QColumnView and QListView are built off of QAbstractListModel
    For Testing Purposes I'm going to make both widgets

    Overloaded constructor sets list data structure to what's given, or empty by default
"""
class LivingDataListModel(QtCore.QAbstractListModel):
    def __init__(self, db_list=None):
        super().__init__()
        self.db_list = db_list or []

    #TODO: I have no idea if these work

    def data(self, index, role):
        # There are other roles outside of 'give me data to display'
        # so we'll specify our type of request when we call the method
        if role == Qt.DisplayRole:
            # Return only the text (forseeably the database name / table name)
            # given the column is always zero in a 1D list, so just return row
            return self.db_list[index.row()]

    def rowCount(self, index):
        return len(self.db_list)


"""
    Subclassing from both PySide6 and our module we made from the .ui file
"""
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Ui_MainWindow has no __init__() so I guess it defaults to QMainWindow's constructor
        super().__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)

        # Get database list and put it in the model and set the model

        list_o_dbs = connect_and_return_databases()

        self.model = LivingDataListModel(list_o_dbs)

        # Access the widgets here via Ui_MainWindow inheritance
        self.livdbListView.setModel(self.model)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
# Pass exit code to system
sys.exit(app.exec())