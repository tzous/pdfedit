# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ShowImageWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super(ShowImageWidget, self).__init__(*args, **kwargs)  # 继承父类
        self.setMouseTracking(True)  # 保证得到鼠标信息

    # 鼠标滚轮事件
    def wheelEvent(self, ev):
        if ev.modifiers() & Qt.ControlModifier:  # 鼠标左键及Ctrl同时按下
            pix = self.pixmap()
            width = pix.width()
            height = pix.height()
            if ev.delta() > 0:
                width = int(width * 1.05)
                height = int(height * 1.05)
            else:
                if width > 200:
                    width = int(width * 0.95)
                    height = int(height * 0.95)
            self.setPixmap(pix.scaled(QSize(width,height)))
