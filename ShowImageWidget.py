# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ShowImageWidget(QLabel):
    def __init__(self, *args, **kwargs):
        super(ShowImageWidget, self).__init__(*args, **kwargs)  # 继承父类
        self.setMouseTracking(True)  # 保证得到鼠标信息
        self.m_pixmap = None         # 原始QPixmap图像
        self.m_factor = 1            # 缩放因子

    # 设置显示图片
    def setpix(self, pix):
        self.m_pixmap = pix
        self.setPixmap(pix)

    # 鼠标滚轮事件
    def wheelEvent(self, ev):
        if ev.modifiers() & Qt.ControlModifier:  # 鼠标左键及Ctrl同时按下
            if ev.angleDelta().y() > 0:
                self.m_factor = self.m_factor * 1.05
            else:
                if self.m_factor > 0.2:
                    self.m_factor = self.m_factor * 0.95
            width = int(self.m_pixmap.width() * self.m_factor)
            height = int(self.m_pixmap.height() * self.m_factor)
            self.setPixmap(self.m_pixmap.scaled(QSize(width, height)))
