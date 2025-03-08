#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:43
# @Author  : 刘双喜
# @File    : app.py
# @Description : 添加描述
from PyQt6.QtWidgets import QApplication

from controllers.main_controller import MainController
from core.window import MainWindow
from utils.logger import setup_logging

# core/app.py 更新
class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        setup_logging()
        self.main_window = MainWindow()
        # 初始化控制器
        self.controller = MainController(self.main_window)
        self.main_window.show()