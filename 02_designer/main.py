#!/usr/bin/env python3
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

import showGui


class Window(QDialog, showGui.Ui_mainDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.showButton.clicked.connect(self.greet)

    def greet(self):
        name = self.nameEdit.text()
        QMessageBox.information(self, "", f"Hello {name}!")


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
