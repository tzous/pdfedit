# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from Ui_dlgto import Ui_dlgto   # 页面选择区间


class dlgto(QtWidgets.QDialog, Ui_dlgto):

    def __init__(self):
        super(dlgto, self).__init__()
        self.setupUi(self)
