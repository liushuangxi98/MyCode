#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 19:22
# @Author  : 刘双喜
# @File    : event_thread.py
# @Description : 添加描述
import time

from PyQt6.QtCore import QThread, pyqtSignal


class EventThread(QThread):
    event = pyqtSignal(str)

    def __init__(self, action):
        super().__init__()
        self.fun = action
        self.running = False

    def run(self) -> None:
        if self.fun == 'fun1':
            self.fun1()

    def fun1(self):
        self.running = True
        for i in range(5):
            self.event.emit(f'fun1 emit {i}')
            time.sleep(2)
        self.running = False
