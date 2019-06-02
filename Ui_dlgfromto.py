# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgfromto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgfromto(object):
    def setupUi(self, dlgfromto):
        dlgfromto.setObjectName("dlgfromto")
        dlgfromto.resize(400, 98)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgfromto)
        self.buttonBox.setGeometry(QtCore.QRect(40, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(dlgfromto)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 356, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(dlgfromto)
        self.buttonBox.accepted.connect(dlgfromto.accept)
        self.buttonBox.rejected.connect(dlgfromto.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgfromto)

    def retranslateUi(self, dlgfromto):
        _translate = QtCore.QCoreApplication.translate
        dlgfromto.setWindowTitle(_translate("dlgfromto", "请选择页面区间"))
        self.label.setText(_translate("dlgfromto", "从"))
        self.lineEdit.setInputMask(_translate("dlgfromto", "9999"))
        self.label_2.setText(_translate("dlgfromto", "到"))
        self.lineEdit_2.setInputMask(_translate("dlgfromto", "9999"))

