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
        self.pdfName = None     # 文档名
        self.nPages = 0      # 文档总页数
        self.nCurr = -1      # 当前文档页码
        self.docDoc = None      # 当前pymupdf文档对象
        self.bModified = False    #是否已编辑过
        self.nMaxPages = 32   # 最大显示页数
        self.IMAGE_SIZE = QSize(147, 208)  # A4纸210*297, 乘0.7
        self.LISTITEM_SIZE = QSize(160, 250)

        self.labelFileName = QLabel(self.statusbar)    # 状态栏上的文件名
        self.labelPageInfo = QLabel(self.statusbar)    # 状态栏上的页码信息

        self.initUi()             # 初始化相关控件
        self.set_window_status()  # 设置窗口视图状态
        self.init_event_plot()  # 初始化事件

    # 初始化相关控件
    def initUi(self):
        # 初始化listWidget
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(self.IMAGE_SIZE)  # Icon 大小
        self.listWidget.setMovement(QListView.Static)  # Listview显示状态
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setSpacing(12)  # 间距大小
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 初始化状态栏
        self.labelFileName.setMinimumWidth(500)
        self.statusbar.addWidget(self.labelFileName)
        self.statusbar.addWidget(self.labelPageInfo)

    # 设置窗口菜单控件状态
    def set_window_status(self):
        if self.bOpened:
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
            if self.bModified:
                self.actionSave.setEnabled(True)
            else:
                self.actionSave.setEnabled(False)
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
            self.labelFileName.setText("")  # 状态栏上的文件名
            self.labelPageInfo.setText("")  # 状态栏上的页码信息

    # 初始化事件
    def init_event_plot(self):
        # 打开文件
        self.actionOpen.triggered.connect(self.onclicked_actionOpen)
        # 关闭文件
        self.actionClose.triggered.connect(self.onclicked_actionClose)
        # 保存文件
        self.actionSave.triggered.connect(self.onclicked_actionSave)
        # 另存为
        self.actionSaveAs.triggered.connect(self.onclicked_actionSaveAs)
        # 删除当前页
        self.actionDelete.triggered.connect(self.onclicked_actionDelete)

        # 缩略图列表控件单击事件
        self.listWidget.clicked.connect(self.onclicked_listWidget)

    # 打开文件
    def onclicked_actionOpen(self):
        self.pdfName, pdfType = QFileDialog.getOpenFileName(self, "打开pdf文件", "", "*.pdf")
        if self.pdfName:
            self.docDoc = fitz.open(self.pdfName)
            self.bOpened = True  # 设置文件打开
            self.labelFileName.setText(self.pdfName)
            self.set_window_status()  # 激活窗口控件
            self.refresh_listWidget()
            # 显示第一页
            self.nCurr = 0
            self.show_current_page()

    # 刷新listWidget
    def refresh_listWidget(self):
        if not self.bOpened:
            return
        self.listWidget.clear()
        self.nPages = self.docDoc.pageCount
        if self.nPages <= 0:
            return
        for i in range(0, self.nPages):
            page = self.docDoc[i]  # 当前页
            zoom = int(100)
            rotate = int(0)
            trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
            pix = page.getPixmap(matrix=trans, alpha=False)
            fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
            qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)  # 当前页转换为QImage对象

            widget = QWidget(self)
            vboxLayout = QVBoxLayout()
            widget.setLayout(vboxLayout)
            listItem = QListWidgetItem(self.listWidget)  # 列表控件项
            listItem.setSizeHint(self.LISTITEM_SIZE)
            labelimg = QLabel(widget)
            labelimg.setPixmap(QPixmap.fromImage(qtimg).scaled(self.IMAGE_SIZE))  # 显示在一个QLabel上
            labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            labeltxt = QLabel(widget)  # 页码序号
            labeltxt.setText("%d" % int(i + 1))
            labeltxt.setFixedHeight(30)
            labeltxt.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            labeltxt.setWordWrap(True)
            vboxLayout.addWidget(labelimg)  # 图片和页码加入vboxLayout
            vboxLayout.addWidget(labeltxt)
            widget.setFixedHeight(self.LISTITEM_SIZE.height())

            self.listWidget.setItemWidget(listItem, widget)  # 显示到listWidget中
        listItem = QListWidgetItem(self.listWidget)  # listWidget最后一项显示异常,因此多加一项,需要再排查优化
        listItem.setSizeHint(QSize(0, 0))

    # 显示当前页
    def show_current_page(self):
        if not self.bOpened or self.nPages <= 0:
            return
        if self.nCurr < 0:
            return
        if self.nCurr >= self.nPages:
            self.nCurr = self.nPages - 1

        # 得到当前页
        page = self.docDoc[self.nCurr]
        zoom = int(100)
        rotate = int(0)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pix = page.getPixmap(matrix=trans, alpha=False)
        fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
        qtimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt) # 当前页转换为QImage对象
        # 准备显示控件
        widget = QWidget(self)
        vboxLayout = QVBoxLayout()
        labelimg = ShowImageWidget(widget)  # 使用一个自定义的QLabel控件
        labelimg.setpix(QPixmap.fromImage(qtimg).scaled(QSize(pix.width, pix.height)))
        labelimg.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        vboxLayout.addWidget(labelimg)
        widget.setLayout(vboxLayout)
        self.showArea.setWidget(widget)    # 添加到showArea

        # 更新状态栏页码
        self.labelPageInfo.setText("第 %d 页/共 %d 页" % (int(self.nCurr + 1), self.nPages))

    # 缩略图列表控件单击事件
    def onclicked_listWidget(self, index):
        self.nCurr = index.row()
        self.show_current_page()

    # 关闭当前文件
    def onclicked_actionClose(self):
        if self.bOpened and self.bModified:    # 文档已被修改
            self.onclicked_actionSave()
        if self.bOpened:
            self.docDoc.close()
        self.bOpened = False    # 文档是否打开
        self.pdfName = None     # 文档名
        self.nPages = 0         # 文档总页数
        self.nCurr = -1          # 当前文档页码
        self.docDoc = None      # 当前pymupdf文档对象
        self.set_window_status()

    # 保存文档
    def onclicked_actionSave(self):
        if not self.bOpened or not self.bModified:
            return
        ret = QMessageBox.information(self,"Question","文档已修改，是否保存？", QMessageBox.Yes|QMessageBox.No )
        if ret != QMessageBox.Yes:
            return
        self.docDoc.save(self.pdfName, incremental=True)
        self.bModified = False
        self.set_window_status()

    # 另存为
    def onclicked_actionSaveAs(self):
        if not self.bOpened:
            return
        filePath, fname = os.path.split(os.path.abspath(self.pdfName))
        newfileName, ok = QFileDialog.getSaveFileName(self, "文件另存为", filePath, "*.pdf")
        if newfileName:
            self.docDoc.save(newfileName)
            self.pdfName = newfileName
            self.labelFileName.setText(self.pdfName)

    # 删除当前页
    def onclicked_actionDelete(self):
        if not self.bOpened or self.nPages <= 0 or self.nCurr < 0:
            return
        if self.nPages == 1:
            QMessageBox.information(self, "Question", "最后一页，不能删除！", QMessageBox.Ok)
            return
        ret = QMessageBox.information(self, "Question", "是否删除当前页？", QMessageBox.Yes|QMessageBox.No )
        if ret != QMessageBox.Yes:
            return
        self.docDoc.deletePage(self.nCurr)
        # 更新listWidget
        # self.listWidget.removeItemWidget(self.listWidget.takeItem(self.nCurr))   # listWidget中页码没有更正，所以全体刷新
        self.refresh_listWidget()
        # 更改页码
        self.nCurr = self.nCurr - 1
        if self.nPages > 0 and self.nCurr < 0:
            self.nCurr = 0
        # 在scrollArea中显示新页
        self.show_current_page()
        # 更新状态
        self.bModified = True
        self.set_window_status()
        # 更新状态栏页码
        self.labelPageInfo.setText("第 %d 页/共 %d 页" % (int(self.nCurr + 1), self.nPages))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
