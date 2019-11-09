#!/usr/bin/env python3

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


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
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        aboutBtn = QPushButton("About", self)
        aboutBtn.move(50, 50)
        aboutBtn.clicked.connect(self.About)

        self.show()

    def About(self):
        QMessageBox.about(self, "About", "This app was written by Jabba Laci\n2018")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
