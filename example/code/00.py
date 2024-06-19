#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 21:40
# @Author  : 刘双喜
# @File    : 00.py
# @Description : 添加描述
import sys
import time

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import QTimer


class InfoDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.name = None
        self.age = None
        self.sex = None

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name: ")
        self.name_text = QLineEdit()
        self.name_text.setReadOnly(True)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_text)

        self.age_label = QLabel("Age: ")
        self.age_text = QLineEdit()
        self.age_text.setReadOnly(True)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_text)

        self.sex_label = QLabel("Sex: ")
        self.sex_text = QLineEdit()
        self.sex_text.setReadOnly(True)
        layout.addWidget(self.sex_label)
        layout.addWidget(self.sex_text)

        self.setLayout(layout)
        self.setWindowTitle('Info Display')

        # 创建一个定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)  # 连接超时信号和槽函数
        self.timer.start(100)  # 启动定时器，参数是间隔的毫秒数

    def update_info(self, name=None, age=None, sex=None):
        if name is not None:
            self.name = name
            self.name_text.setText(name)
        if age is not None:
            self.age = age
            self.age_text.setText(str(age))
        if sex is not None:
            self.sex = sex
            self.sex_text.setText(sex)
        # 刷新界面以显示更新
        self.update()


# 测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoDisplay()
    window.show()

    # 模拟循环测试中的信息更新
    for i in range(10):  # 示例循环5次，每次更新信息
        window.update_info(name=f"User{i}", age=i * 2, sex="Male" if i % 2 == 0 else "Female")
        QApplication.processEvents()  # 确保UI更新可见
        time.sleep(10)

        # 注意：实际应用中可能需要根据具体逻辑控制循环和更新频率，避免UI冻结

    sys.exit(app.exec())
