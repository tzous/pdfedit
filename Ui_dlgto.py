# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgto(object):
    def setupUi(self, dlgto):
        dlgto.setObjectName("dlgto")
        dlgto.resize(300, 102)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgto)
        self.buttonBox.setGeometry(QtCore.QRect(-70, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(dlgto)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(dlgto)
        self.buttonBox.accepted.connect(dlgto.accept)
        self.buttonBox.rejected.connect(dlgto.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgto)

    def retranslateUi(self, dlgto):
        _translate = QtCore.QCoreApplication.translate
        dlgto.setWindowTitle(_translate("dlgto", "请输入页码"))
        self.label.setText(_translate("dlgto", "页码："))
        self.lineEdit.setInputMask(_translate("dlgto", "9999"))

