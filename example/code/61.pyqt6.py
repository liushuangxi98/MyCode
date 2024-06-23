#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/21 20:27
# @Author  : 刘双喜
# @File    : 61.pyqt6.py
# @Description : 添加描述
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QToolTip, QMessageBox, QLabel, QLineEdit, QProgressBar, QComboBox, QMainWindow
from PyQt6.QtGui import QFont


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置window标题
        self.setWindowTitle('我的第一个PyQt6程序')
        # 设置window大小
        self.setGeometry(100, 100, 400, 300)
        # 设置window悬停提示字体和信息
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 居中
        self.set_center()

        # 绝对布局 - 按钮，位于self父窗口
        btn = QPushButton('点击我，不带弹出', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 调整为推荐大小
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        btn.setStyleSheet('''
            QPushButton {  /* 按钮的默认样式 */
                background-color: #F0F0F0;  /* 背景色 */
                color: #333;  /* 文字颜色 */
                border: 2px solid #555;  /* 边框，2px宽，实线，颜色为#555 */
                border-radius: 10px;  /* 边框圆角半径 */
                padding: 5px;  /* 内边距 */
                min-width: 80px;  /* 最小宽度 */
            }
            QPushButton:hover {  /* 鼠标悬停在按钮上时的样式 */
                background-color: #FFF;  /* 背景色 */
                border: 2px solid #F00;  /* 边框，2px宽，实线，颜色为#F00 */
            }
            QPushButton:pressed {  /* 按钮被按下时的样式 */
                background-color: #F00;  /* 背景色 */
                border: 2px solid #FFF;  /* 边框，2px宽，实线，颜色为#FFF */
            }
        ''')

        # 绝对布局，标签
        label = QLabel(self)
        label.setText("这是一个标签")
        label.move(0, 30)

        # 绝对布局，输入框
        line_edit = QLineEdit(self)
        line_edit.move(0, 60)
        text = line_edit.text()  # 获取输入

        # 绝对布局，进度条
        progress_bar = QProgressBar(self)
        progress_bar.setValue(50)
        progress_bar.move(0, 100)

        # 绝对布局，下拉条
        combo_box = QComboBox(self)
        combo_box.move(0,160)
        combo_box.addItem("选项1")
        combo_box.addItem("选项2")
        selected_text = combo_box.currentText()

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建按钮并连接信号槽
        button = QPushButton("点击我，带弹出")
        button.clicked.connect(self.on_button_clicked)

        # 将按钮添加到布局中
        layout.addWidget(button)

        # 设置窗口的布局为刚才创建的布局
        self.setLayout(layout)

        self.show()

    # 重写关闭按钮
    def closeEvent(self, event):
        # 入参，标题，打印信息，第一个按钮，第二个按钮，默认按钮
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  #
        else:
            event.ignore()

    # 重写按钮连接槽函数
    def on_button_clicked(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to execute?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # QApplication.instance().quit()  # 会调用closeEvent
            print('执行')
        else:
            print('取消')

    def fun1(self):
        print(111)


    def set_center(self):
        qr = self.frameGeometry()  # 得到矩形窗口
        cp = self.screen().availableGeometry().center()  # 计算分辨率，然后计算中心点
        qr.moveCenter(cp)  # 计算窗口中心点位置
        self.move(qr.topLeft())  # 窗口左上角移动到计算出窗口左上角位置
        # self.move(qr.center())  # 窗口左上角移动到计算出窗口中心点位置



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    # app.setStyle('Fusion')
    # app.setStyle('Windows')
    ex = MyApp()
    sys.exit(app.exec())
