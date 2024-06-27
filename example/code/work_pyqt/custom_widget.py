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
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QTimer, QTime, Qt


class CustomWidget(QWidget):
    def __init__(self, draw_clock_flag):
        super().__init__()
        self.draw_clock_flag = draw_clock_flag
        self.x = 0
        self.y = 0
        self.labels = ['AAA', 'B', 'C', 'D', 'E']
        self.rhythm_flag = False

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

    def paintEvent(self, event):
        if self.draw_clock_flag:
            self.draw_clock()

    def draw_clock(self):
        painter = QPainter(self)  # 创建一个画笔
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿
        painter.translate(3840 * 0.4 / 2, 2160 * 0.4 / 2)  # 将坐标系的原点移动到窗口的中心
        self.draw_clock_progress(painter, self.labels, 1, 360)  # 绘制时钟的表面
        self.draw_clock_progress_across(painter, self.labels, 2, 330, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 300, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 2, 270, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 4, 240, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 210, Qt.GlobalColor.green)  # 绘制时钟的表面

    def draw_clock_progress(self, painter, labels, idx, line_start, finsh_color=Qt.GlobalColor.green,
                            not_finsh_color=Qt.GlobalColor.white):
        line_num = line_start // 3 + (len(labels) - line_start // 3 % len(labels))
        size = 2  # 粗细
        len_short = 12  # 短的长度
        len_long = 24  # 长的长度
        painter.setPen(QPen(finsh_color, size))  # 前部分，已完成的，颜色
        step = line_num // len(labels)
        for j in range(line_num):  # 遍历0到59
            if (j % step) != 0:  # 未到当前元素列表
                lens = len_long if j % 2 == self.rhythm_flag else len_short  # 当前线条长或短
                painter.drawLine(line_start, -4, line_start + lens, -4)  # 绘制一根线, 略微偏移，|和字符占用空间不同
            else:  # 当前到了要绘制labels的时候
                if j // step == idx:  # 到了当前循环到的，设置颜色，之后的都是未完成
                    painter.setPen(QPen(not_finsh_color, size))  # 设置画笔的颜色和宽度
                painter.drawText(line_start, 0, labels[j // step])  # 绘制标签
            painter.rotate(360 / line_num)  # 旋转画笔，角度为6

    def draw_clock_progress_across(self, painter, labels, idx, line_start, finsh_color=Qt.GlobalColor.green,
                                   not_finsh_color=Qt.GlobalColor.black):
        line_num = line_start // 3 + (len(labels) - line_start // 3 % len(labels))
        size = 2  # 粗细
        len_short = 12  # 短的长度
        len_long = 24  # 长的长度
        painter.setPen(QPen(finsh_color, size))  # 前部分，已完成的，颜色
        step = line_num // len(labels)
        for j in range(line_num):  # 遍历0到线条总数
            if (j % step) != 0:  # 未到当前元素列表
                lens = len_long if j % 2 == self.rhythm_flag else len_short  # 当前线条长或短
                painter.drawLine(0, -line_start, 0, -line_start - lens)  # 绘制一根线
            else:  # 当前到了要绘制labels的时候
                if j // step == idx:  # 到了当前循环到的，设置颜色，之后的都是未完成
                    painter.setPen(QPen(not_finsh_color, size))  # 设置画笔的颜色和宽度
                painter.drawText(-5, -line_start, labels[j // step])  # 绘制标签, 略微偏移，|和字符占用空间不同
            painter.rotate(360 / line_num)  # 旋转画笔，角度为6