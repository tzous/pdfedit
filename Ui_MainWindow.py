# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.indexArea = QtWidgets.QScrollArea(self.centralwidget)
        self.indexArea.setMinimumSize(QtCore.QSize(200, 0))
        self.indexArea.setMaximumSize(QtCore.QSize(200, 16777215))
        self.indexArea.setWidgetResizable(True)
        self.indexArea.setObjectName("indexArea")
        self.indexAreaWidgetContents = QtWidgets.QWidget()
        self.indexAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 533))
        self.indexAreaWidgetContents.setObjectName("indexAreaWidgetContents")
        self.indexArea.setWidget(self.indexAreaWidgetContents)
        self.horizontalLayout.addWidget(self.indexArea)
        self.displayArea = QtWidgets.QScrollArea(self.centralwidget)
        self.displayArea.setWidgetResizable(True)
        self.displayArea.setObjectName("displayArea")
        self.displayAreaWidgetContents = QtWidgets.QWidget()
        self.displayAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 572, 533))
        self.displayAreaWidgetContents.setObjectName("displayAreaWidgetContents")
        self.displayArea.setWidget(self.displayAreaWidgetContents)
        self.horizontalLayout.addWidget(self.displayArea)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAppend = QtWidgets.QAction(MainWindow)
        self.actionAppend.setObjectName("actionAppend")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        self.actionExtract.setObjectName("actionExtract")
        self.actionMove = QtWidgets.QAction(MainWindow)
        self.actionMove.setObjectName("actionMove")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionpictopdf = QtWidgets.QAction(MainWindow)
        self.actionpictopdf.setObjectName("actionpictopdf")
        self.actionmerge = QtWidgets.QAction(MainWindow)
        self.actionmerge.setObjectName("actionmerge")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionPicToPdf = QtWidgets.QAction(MainWindow)
        self.actionPicToPdf.setObjectName("actionPicToPdf")
        self.actionMerge = QtWidgets.QAction(MainWindow)
        self.actionMerge.setObjectName("actionMerge")
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveAs)
        self.menu.addSeparator()
        self.menu.addAction(self.actionPrint)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionAppend)
        self.menu_2.addAction(self.actionExtract)
        self.menu_2.addAction(self.actionCopy)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionMove)
        self.menu_2.addAction(self.actionRotate)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionDelete)
        self.menu_3.addAction(self.actionHelp)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAbout)
        self.menu_4.addAction(self.actionPicToPdf)
        self.menu_4.addAction(self.actionMerge)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdfEdit"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "操作"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.menu_4.setTitle(_translate("MainWindow", "转换"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionOpen.setText(_translate("MainWindow", "打开..."))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存为..."))
        self.actionPrint.setText(_translate("MainWindow", "打印"))
        self.actionClose.setText(_translate("MainWindow", "关闭"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionAppend.setText(_translate("MainWindow", "追加"))
        self.actionDelete.setText(_translate("MainWindow", "删除"))
        self.actionExtract.setText(_translate("MainWindow", "导出"))
        self.actionMove.setText(_translate("MainWindow", "移动"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About ..."))
        self.actionCopy.setText(_translate("MainWindow", "拷贝"))
        self.actionpictopdf.setText(_translate("MainWindow", "pictopdf"))
        self.actionmerge.setText(_translate("MainWindow", "merge"))
        self.actionRotate.setText(_translate("MainWindow", "旋转"))
        self.actionPicToPdf.setText(_translate("MainWindow", "图片转PDF"))
        self.actionMerge.setText(_translate("MainWindow", "合并PDF"))

