#!/usr/bin/env python3

"""
I want to make 'q' work with and without the menu bar. If you press 'q', the app. should close.
File -> Quit would do the same.
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut

from pprint import pprint


def print_variables_of(obj):
    """variables of an object"""
    pprint(vars(obj))


def print_callables_of(obj):
    """callables (functions too) of an object"""
    li = []
    for name in dir(obj):
        attr = getattr(obj, name)
        if hasattr(attr, '__call__'):
            li.append(name)
    pprint(li)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.shortcutQuit = QShortcut(QKeySequence("q"), self)
        self.shortcutQuit.activated.connect(self.close)
        self.shortcutQuit.setEnabled(False)

        self.InitWindow()

    def InitWindow(self):
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("&File")

        hideItem = QAction("Hide Menu Bar", self)
        hideItem.setShortcut("h")
        # print(hideItem.shortcut().keyBindings())
        # print(hideItem.shortcut().listToString())
        hideItem.triggered.connect(self.my_hide)

        quitItem = QAction("Quit", self)
        quitItem.setShortcut("Q")
        quitItem.triggered.connect(self.close)

        fileMenu.addAction(hideItem)
        fileMenu.addAction(quitItem)

    def my_hide(self):
        self.mainMenu.hide()
        self.shortcutQuit.setEnabled(True)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())