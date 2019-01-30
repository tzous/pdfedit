# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog

import sys
import os
import os.path
import shutil

import fitz

import six


from Ui_MainWindow import Ui_MainWindow   # 主窗口


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller会创建临时文件夹temp，并把路径存储在_MEIPASS中
            self.appPath = os.path.dirname(os.path.realpath(sys.executable))
        else:
            self.appPath, filename = os.path.split(os.path.abspath(__file__))
        self.bOpened = True     # 文档是否打开
        self.nPages = 0      # 文档总页数
        self.nCurr = 0       # 当前文档页码
        self.docDoc = None      # 当前pymupdf文档对象
        self.nMaxPages = 32   # 最大显示页数
        self.IMAGE_SIZE = QSize(180,250)

        self.set_menu_status()  # 初始化菜单项状态
        self.initEventPlot()  # 初始化事件

        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(self.IMAGE_SIZE)  # Icon 大小
        self.listWidget.setMovement(QListView.Static)  # Listview显示状态
        self.listWidget.setSpacing(12)  # 间距大小

    # 设置菜单项状态
    def set_menu_status(self):
        if self.bOpened:
            self.actionSave.setEnabled(True)
            self.actionSaveAs.setEnabled(True)
            self.actionClose.setEnabled(True)
            self.actionPrint.setEnabled(True)
            self.actionAppend.setEnabled(True)
            self.actionExtract.setEnabled(True)
            self.actionCopy.setEnabled(True)
            self.actionMove.setEnabled(True)
            self.actionDelete.setEnabled(True)
            self.actionRotate.setEnabled(True)
            self.listWidget.setVisible(True)
            self.showArea.setVisible(True)
        else:
            self.actionSave.setEnabled(False)
            self.actionSaveAs.setEnabled(False)
            self.actionClose.setEnabled(False)
            self.actionPrint.setEnabled(False)
            self.actionAppend.setEnabled(False)
            self.actionExtract.setEnabled(False)
            self.actionCopy.setEnabled(False)
            self.actionMove.setEnabled(False)
            self.actionDelete.setEnabled(False)
            self.actionRotate.setEnabled(False)
            self.listWidget.setVisible(False)
            self.showArea.setVisible(False)

    # 初始化事件
    def initEventPlot(self):
        # 打开文件
        self.actionOpen.triggered.connect(self.onClickedactionOpen)

    # 打开文件
    def onClickedactionOpen(self):
        pdfName, pdfType = QFileDialog.getOpenFileName(self, "打开pdf文件", "", "*.pdf")
        if pdfName:
            self.docDoc = fitz.open(pdfName)
            self.nPages = self.docDoc.pageCount
            #vshowLayout = QVBoxLayout()
            #showwidget = QWidget(self)
            for i in range(0, self.nPages):
                page = self.docDoc[i]
                zoom = int(100)
                rotate = int(0)
                trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
                pix = page.getPixmap(matrix=trans, alpha=False)
                fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
                qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)
                widget = QWidget(self)
                vboxLayout = QVBoxLayout()
                widget.setLayout(vboxLayout)
                listItem = QListWidgetItem(self.listWidget)
                listItem.setSizeHint(QSize(200, 280))
                labelimg = QLabel(widget)
                labelimg.setPixmap(QPixmap.fromImage(qtimg).scaled(self.IMAGE_SIZE))
                labelimg.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
                labeltxt = QLabel(widget)
                labeltxt.setWindowTitle("%d" % i)
                labeltxt.setFixedHeight(30)
                labeltxt.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                labeltxt.setWordWrap(True)
                vboxLayout.addWidget(labelimg)
                vboxLayout.addWidget(labeltxt)

                #vshowLayout.addWidget(labelimg)

                self.listWidget.setItemWidget(listItem, widget)
            #showwidget.setLayout(vshowLayout)
            #self.showArea.setWidget(showwidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
