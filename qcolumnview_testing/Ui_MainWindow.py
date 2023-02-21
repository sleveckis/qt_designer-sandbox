# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer_file.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QColumnView, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.livdbColView = QColumnView(self.centralwidget)
        self.livdbColView.setObjectName(u"livdbColView")
        self.livdbColView.setGeometry(QRect(20, 30, 601, 151))
        self.cool_button = QPushButton(self.centralwidget)
        self.cool_button.setObjectName(u"cool_button")
        self.cool_button.setGeometry(QRect(20, 370, 601, 61))
        self.livdbListView = QListView(self.centralwidget)
        self.livdbListView.setObjectName(u"livdbListView")
        self.livdbListView.setGeometry(QRect(20, 210, 591, 141))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 190, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cool_button.setText(QCoreApplication.translate("MainWindow", u"TestButtonIfNeeded", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QColumnView", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QListView", None))
    # retranslateUi

