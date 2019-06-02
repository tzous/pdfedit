# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from Ui_dlgabout import Ui_DlgAbout   #


class About(QtWidgets.QDialog, Ui_DlgAbout):

    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
