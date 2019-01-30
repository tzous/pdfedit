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
from ShowImageWidget import ShowImageWidget   # 显示图片控件


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller会创建临时文件夹temp，并把路径存储在_MEIPASS中
            self.appPath = os.path.dirname(os.path.realpath(sys.executable))
        else:
            self.appPath, filename = os.path.split(os.path.abspath(__file__))
        self.bOpened = False    # 文档是否打开
        self.nPages = 0      # 文档总页数
        self.nCurr = 0       # 当前文档页码
        self.docDoc = None      # 当前pymupdf文档对象
        self.nMaxPages = 32   # 最大显示页数
        self.IMAGE_SIZE = QSize(147, 208)  # A4纸210*297, 乘0.7
        self.LISTITEM_SIZE = QSize(160, 250)

        self.set_window_status()  # 初始化窗口视图状态
        self.init_event_plot()  # 初始化事件

        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(self.IMAGE_SIZE)  # Icon 大小
        self.listWidget.setMovement(QListView.Static)  # Listview显示状态
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(12)  # 间距大小
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # 初始化窗口视图状态
    def set_window_status(self):
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
    def init_event_plot(self):
        # 打开文件
        self.actionOpen.triggered.connect(self.onclicked_actionOpen)
        # 缩略图列表控件单击事件
        self.listWidget.clicked.connect(self.onclicked_listWidget)

    # 打开文件
    def onclicked_actionOpen(self):
        pdfName, pdfType = QFileDialog.getOpenFileName(self, "打开pdf文件", "", "*.pdf")
        if pdfName:
            self.docDoc = fitz.open(pdfName)
            self.nPages = self.docDoc.pageCount
            self.bOpened = True    # 设置文件打开
            self.set_window_status()    # 激活窗口控件
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
                listItem.setSizeHint(self.LISTITEM_SIZE)
                labelimg = QLabel(widget)
                labelimg.setPixmap(QPixmap.fromImage(qtimg).scaled(self.IMAGE_SIZE))
                labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                labeltxt = QLabel(widget)
                labeltxt.setText("%d" % int(i+1))
                labeltxt.setFixedHeight(30)
                labeltxt.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                labeltxt.setWordWrap(True)
                vboxLayout.addWidget(labelimg)
                vboxLayout.addWidget(labeltxt)
                widget.setFixedHeight(self.LISTITEM_SIZE.height())

                self.listWidget.setItemWidget(listItem, widget)
            listItem = QListWidgetItem(self.listWidget)     # listWidget最后一项显示异常,因此多加一项,需要再排查优化
            listItem.setSizeHint(QSize(0, 0))
            # 显示第一页
            self.nCurr = 0
            self.show_current_page()

    # 显示当前页
    def show_current_page(self):
        if not self.bOpened or self.nPages <= 0:
            return
        if self.nCurr >= self.nPages:
            self.nCurr = self.nPages - 1
        if self.nCurr < 0:
            self.nCurr = 0

        # 得到当前页
        page = self.docDoc[self.nCurr]
        zoom = int(100)
        rotate = int(0)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pix = page.getPixmap(matrix=trans, alpha=False)
        fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
        qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)
        # 准备显示控件
        widget = QWidget(self)
        vboxLayout = QVBoxLayout()
        labelimg = ShowImageWidget(widget)
        labelimg.setPixmap(QPixmap.fromImage(qtimg).scaled(QSize(pix.width, pix.height)))
        labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vboxLayout.addWidget(labelimg)
        widget.setLayout(vboxLayout)
        self.showArea.setWidget(widget)

    # 缩略图列表控件单击事件
    def onclicked_listWidget(self, index):
        self.nCurr = index.row()
        self.show_current_page()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
