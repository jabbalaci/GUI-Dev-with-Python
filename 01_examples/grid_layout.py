#!/usr/bin/env python3

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, QDialog, QPushButton, QGridLayout


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 GridLayout"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)
        # self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.grid_layout_creation()

        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)
        self.setLayout(vbox)

        self.show()

    def grid_layout_creation(self):
        self.group_box = QGroupBox("Grid layout")

        layout = QGridLayout()
        layout.addWidget(QPushButton("1"), 0, 0)
        layout.addWidget(QPushButton("2"), 0, 1)
        layout.addWidget(QPushButton("3"), 1, 0)
        layout.addWidget(QPushButton("4"), 1, 1)

        self.group_box.setLayout(layout)




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
