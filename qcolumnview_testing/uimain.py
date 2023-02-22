"""
    uimain.py
    02-20-2023
    Author: Leveckis

    Borrowing QAbstractListModel subclassing via 
    https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/

    Borrowing QStandardItemModel subclassing (which is what I actually use for QColumnView) via
    https://bancaldo.wordpress.com/2019/05/16/pyqt5-qcolumnview/
    (google translate it to english)
"""


import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
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
class LivingDataListofListsModel(QtCore.QAbstractListModel):
    def __init__(self, db_list=None):
        super().__init__()
        self.db_list = db_list or []

    #TODO: I have no idea if these work

    def data(self, index, role):
        # There are other roles outside of 'give me data to display'
        # so we'll specify our type of request when we call the method
        if role == Qt.DisplayRole:
            return self.db_list[index.column()][index.row()]

    def rowCount(self, index):
        return len(self.db_list)
"""

class CustomModel(QStandardItemModel):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.setVerticalHeaderItem(0, QStandardItem("Database"))
        self.setVerticalHeaderItem(1, QStandardItem("Table"))
 
    def generate_tree(self):
 
        """
        d_team = {"Inter": ["Handanovic", "D'Ambrosio", "De Vrij"],
                  "Milan": ["Donnarumma", "Calabria", "Romagnoli"],
                  "Juve": ["Szczezny", "De Sciglio", "Chiellini"]}
        """

        #TODO: numbers come up as a blank in the UI
        test_dba = {
            "dab1":  [101, "hellow", "yeehaw"],
            "dab2":  [202, "salutations", "cowabunga"],
            "dab3":  [303, "greetings", "weeeee"],
            "dab4":  [404, "howdy", "expelliarmus"],
        }
        # Here's the magic
        for row, db in enumerate(test_dba.keys()):
            self.setItem(row, 0, QStandardItem(db))
            item = self.item(row, 0)
            for rrow, table in enumerate(test_dba.get(item.text())):
                item.setChild(rrow, 0, QStandardItem(table))

"""
    Subclassing from both PySide6 and our module we made from the .ui file
"""
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Ui_MainWindow has no __init__() so I guess it defaults to QMainWindow's constructor
        super().__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        self.model = CustomModel()
        self.model.generate_tree() 

        # Get database list and put it in the model and set the model
        list_o_dbs = connect_and_return_databases()

        #self.model = LivingDataListModel(list_o_dbs)

        # Access the list view widget in our app here, via inheritance, and set it to MainWindow's model
        # self.livdbListView.setModel(self.model)




        self.livdbListView.setModel(LivingDataListModel(list_o_dbs))
        self.livdbColView.setModel(self.model)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
# Pass exit code to system
sys.exit(app.exec())