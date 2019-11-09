#!/usr/bin/env python3

import sys

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.shortcutQuit = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcutQuit.activated.connect(self.close)

        self.InitWindow()

    def closeEvent(self, event):
        print("# doing some cleanup...")

    def InitWindow(self):
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("&File")

        quitItem = QAction("Quit", self)
        quitItem.setShortcut("Q")
        quitItem.triggered.connect(self.close)

        fileMenu.addAction(quitItem)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())