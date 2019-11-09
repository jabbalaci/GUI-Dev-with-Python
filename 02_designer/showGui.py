# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(357, 107)
        self.nameEdit = QtWidgets.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(30, 40, 161, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.showButton = QtWidgets.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(240, 40, 71, 30))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        _translate = QtCore.QCoreApplication.translate
        mainDialog.setWindowTitle(_translate("mainDialog", "Main Dialog"))
        self.nameEdit.setPlaceholderText(_translate("mainDialog", "Your name"))
        self.showButton.setText(_translate("mainDialog", "Show!"))
