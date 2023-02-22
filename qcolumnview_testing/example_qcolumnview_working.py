from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget, QApplication, QBoxLayout, QColumnView
from PySide6.QtGui import QStandardItem, QStandardItemModel
import sys
 
 
class MainWindow(QMainWindow):
    def __init__(self, parent=None, model=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QColumnView Example")
        self.central_widget = FormWidget(parent=self, model=model) 
        self.setCentralWidget(self.central_widget)
        self.resize(400, 100)
 
 
class FormWidget(QWidget):
    def __init__(self, parent, model=None):
        super(FormWidget, self).__init__(parent)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.column_view = QColumnView()
        self.column_view.setModel(model)
        self.column_view.setColumnWidths([120, 120, 120])
        self.column_view.clicked.connect(self.on_data)
        self.column_view.setResizeGripsVisible(False)
        layout.addWidget(self.column_view)
 
    def on_data(self):
        print("[SIG] Column widths: %s" % self.column_view.columnWidths())
 
 
class CustomModel(QStandardItemModel):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.setVerticalHeaderItem(0, QStandardItem("Team"))
        self.setVerticalHeaderItem(1, QStandardItem("Player"))
 
    def generate_tree(self):
 
        d_team = {"Inter": ["Handanovic", "D'Ambrosio", "De Vrij"],
                  "Milan": ["Donnarumma", "Calabria", "Romagnoli"],
                  "Juve": ["Szczezny", "De Sciglio", "Chiellini"]}
        for row, team in enumerate(d_team.keys()):
            self.setItem(row, 0, QStandardItem(team))
            item = self.item(row, 0)
            for rrow, player in enumerate(d_team.get(item.text())):
                item.setChild(rrow, 0, QStandardItem(player))
 
 

app = QApplication(sys.argv)
model = CustomModel()
model.generate_tree()
main_window = MainWindow(parent=None, model=model)
main_window.show()
sys.exit(app.exec_())