#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window :)"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        btn = QPushButton("Color", self)
        btn.move(10, 10)
        btn.resize(380, 380)

        # btn.setStyleSheet("background-color: rgb(46, 204, 113); border: none;")
        # btn.setStyleSheet("background-color:#D8BFD8; border: none;");
        btn.setStyleSheet("background-color: rgb(95,135,255); border: none;");

        btn.setToolTip("This is a <i>Click Me</i> button")

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
