# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgabout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName("DlgAbout")
        DlgAbout.resize(287, 120)
        self.pushButton = QtWidgets.QPushButton(DlgAbout)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(DlgAbout)
        self.toolButton.setGeometry(QtCore.QRect(20, 20, 64, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/e7cd7b899e510fb3a3306f9bd433c895d1430c94.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(DlgAbout)
        self.label.setGeometry(QtCore.QRect(100, 20, 81, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(DlgAbout)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 141, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.toolButton.raise_()
        self.label.raise_()

        self.retranslateUi(DlgAbout)
        self.pushButton.clicked.connect(DlgAbout.close)
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        _translate = QtCore.QCoreApplication.translate
        DlgAbout.setWindowTitle(_translate("DlgAbout", "About ..."))
        self.pushButton.setText(_translate("DlgAbout", "OK"))
        self.toolButton.setText(_translate("DlgAbout", "..."))
        self.label.setText(_translate("DlgAbout", "pdfedit 0.1"))
        self.label_2.setText(_translate("DlgAbout", "tzous@126.com"))

