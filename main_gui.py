# -*- coding: utf-8 -*-
""" 
Created on 8/13/2021 9:42 PM
@author  : Kuro Kien
@File name    : main_gui.py
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLineEdit, QMessageBox, QAction, QMainWindow, QBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.title = "Kuro App"
        self.left = 100
        self.top  = 100
        self.width = 420
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.textbox = QLineEdit(self)
        # self.move(10,30)
        # self.textbox.resize(280,20)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('file')
        editMenu = main_menu.addMenu('edit')
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        file_menu.addAction(exitButton)

        # button = QPushButton('Button 1', self)
        # button.setToolTip('author: Kuro')
        # button.move(100,70)
        # button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        text_box_value = self.textbox.text()
        QMessageBox.question(self, "message", "you typed: "+text_box_value, QMessageBox.Ok, QMessageBox.Cancel)
        self.textbox.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



