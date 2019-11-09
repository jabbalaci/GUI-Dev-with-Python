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

        exitAct = QAction(QIcon("exit.png"), "Quit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.triggered.connect(self.close)

        steamAct = QAction(QIcon("steam.svg"), "Steam", self)

        terminalAct = QAction(QIcon("terminal.svg"), "Terminal", self)

        truecryptAct = QAction(QIcon("truecrypt.svg"), "Truecrypt", self)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(steamAct)
        self.toolbar.addAction(terminalAct)
        self.toolbar.addAction(truecryptAct)



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
