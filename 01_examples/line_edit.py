#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window :)"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.line_edit = QLineEdit(self)
        self.line_edit.move(100, 100)
        self.line_edit.resize(200, 30)
        self.line_edit.returnPressed.connect(self.show_text)

        self.btn = QPushButton("Show Text", self)
        self.btn.move(100, 140)
        self.btn.clicked.connect(self.show_text)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()

    def show_text(self):
        QMessageBox.information(self, "Info", self.line_edit.text())


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
