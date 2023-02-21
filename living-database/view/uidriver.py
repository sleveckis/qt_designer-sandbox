import sys 
from PySide6.QtWidgets import QApplication, QMainWindow

# Custom Module
from .Generated import Ui_MainWindow 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1_action)

    def button1_action(self):
        print("Good Evening")

def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

