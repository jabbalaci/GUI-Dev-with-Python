#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


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
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        viewMenu = mainMenu.addMenu("&View")
        editMenu = mainMenu.addMenu("&Edit")

        exitItem = QAction(QIcon("exit.png"), "Quit", self)
        exitItem.setShortcut("Ctrl+Q")
        exitItem.setStatusTip("Quit Application")
        exitItem.triggered.connect(self.close)

        fileMenu.addAction(exitItem)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon("icon.png"))
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
