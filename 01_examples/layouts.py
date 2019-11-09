#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, QDialog, QPushButton


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layouts"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)
        # self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.horizontal_layout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)
        self.setLayout(vbox)

        self.show()

    def horizontal_layout(self):
        self.group_box = QGroupBox("What's your favourite sports?")
        layout = QHBoxLayout()
        btn1 = QPushButton("Football", self)
        btn2 = QPushButton("Handball", self)
        btn3 = QPushButton("Volleyball", self)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        self.group_box.setLayout(layout)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
