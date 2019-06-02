# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from Ui_dlgfromto import Ui_dlgfromto   # 页面选择区间


class dlgfromto(QtWidgets.QDialog, Ui_dlgfromto):

    def __init__(self):
        super(dlgfromto, self).__init__()
        self.setupUi(self)
