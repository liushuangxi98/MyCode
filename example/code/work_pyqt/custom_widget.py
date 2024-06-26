#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 0:08
# @Author  : 刘双喜
# @File    : custom_widget.py
# @Description : 添加描述

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QWidget, \
    QPushButton, QVBoxLayout, QToolTip, QMessageBox, QLabel, QLineEdit, QProgressBar, QComboBox, QMenu, QStackedWidget
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class CustomWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.x = 0
        self.y = 0


    def get_default_xy(self, x, y):
        _x = self.x = self.x if x is None else x  # 当前的
        _y = self.y = self.y if y is None else y
        if y is None:
            self.y += 30  # 下次的默认值
        return _x, _y  # 返回当前的

    def init_button(self, x=None, y=None):
        x, y = self.get_default_xy(x, y)
        # 在这里创建和设置部件
        _button = QPushButton('点击我退出', self)
        _button.clicked.connect(QApplication.instance().quit)
        _button.setToolTip('这是一个按钮部件，点击它会退出程序')
        _button.move(x, y)
        self.y += 30
        return _button

    def init_label(self, x=None, y=None):
        x, y = self.get_default_xy(x, y)
        # 在这里创建和设置部件
        _label = QLabel(self)
        _label.setText("这是一个标签")
        _label.move(x, y)
        return _label

    def init_box(self, x=None, y=None, value: list = None, name: str = ''):
        x, y = self.get_default_xy(x, y)
        _combo_box = QComboBox(self)
        _combo_box.move(x, y)
        for i in value:
            _combo_box.addItem(name + i)
        # _combo_box.addItem('贷款')  # 必须先有
        # _combo_box.setCurrentText('贷款')
        selected_text = _combo_box.currentText()
        print(selected_text)
        return _combo_box

    def init_menu(self, x=None, y=None, name: str = None, sub_name_lst: list = None):
        # x, y = self.get_default_xy(x, y)
        self.menu_bar = QMenuBar(self)
        self.menu_bar.setGeometry(0, 100, 100, 30)
        self.file_menu = QMenu(name, self)  # 菜单1-文件
        self.menu_bar.addMenu(self.file_menu)
        for i in sub_name_lst:
            # 创建一个菜单项
            open_action = QAction(i, self)
            # 将菜单项添加到菜单中
            self.file_menu.addAction(open_action)
        return self.file_menu
