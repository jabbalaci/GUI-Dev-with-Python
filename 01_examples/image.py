#!/usr/bin/env python3

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Jabba's Image Viewer 0.0.1"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.imageLabel = QLabel(self)

        self.setCurrentImage("burned_man.jpg")

    def setCurrentImage(self, fname):
        self.currentImageFname = fname
        self.currentImagePixmap = QPixmap(fname)
        self.redraw()

    def resizeEvent(self, event):
        self.redraw()

    def redraw(self):
        # print("redraw")
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        # print(self.width, self.height)
        #
        pm = self.currentImagePixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # avoid upscale
        if pm.width() > self.currentImagePixmap.width() or pm.height() > self.currentImagePixmap.height():
            pm = self.currentImagePixmap
        # print("Pic: {} x {}".format(pm.width(), pm.height()))
        self.imageLabel.setPixmap(pm)
        # center the image
        self.imageLabel.setGeometry((self.width - pm.width()) / 2,
                                    (self.height - pm.height()) / 2,
                                    pm.width(),
                                    pm.height())

def main():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
