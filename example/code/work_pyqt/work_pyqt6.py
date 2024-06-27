#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/23 12:33
# @Author  : 刘双喜
# @File    : work_pyqt6.py
# @Description : 添加描述
import sys
from custom_widget import *
from ui_main import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rhythm_flag = True
        # self.timer = QTimer()  # 创建一个定时器
        # self.timer.timeout.connect(self.update)  # 当定时器超时时，更新窗口
        # self.timer.start(500)  # 每秒触发一次定时器
        self.ui = UiMainWindow(self)

    # def paintEvent(self, event):
    #     self.ui.paintEvent(event)



def main():
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()
