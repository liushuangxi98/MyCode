#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 0:08
# @Author  : 刘双喜
# @File    : custom_widget.py
# @Description : 添加描述

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QWidget, \
    QPushButton, QVBoxLayout, QToolTip, QMessageBox, QLabel, QLineEdit, QProgressBar, QComboBox, QMenu, QStackedWidget
from PyQt6.QtWidgets import QMenuBar, QFrame, QGraphicsDropShadowEffect, QTextEdit
from PyQt6.QtGui import QAction
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import QTimer, QTime, Qt, QRect
from css import *
from event_thread import *
from PyQt6.QtWidgets import QApplication, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor


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
            self.y += 50  # 下次的默认值
        return _x, _y  # 返回当前的

    def init_button(self, x=None, y=None, name=None, _css=css.get('QButton'), windows=None):
        x, y = self.get_default_xy(x, y)
        # 在这里创建和设置部件
        _button = QPushButton(name or '没有名称', windows or self)
        _button.setToolTip('这是一个按钮部件')
        _button.move(x, y)
        _button.setStyleSheet(_css)
        self.y += 30
        return _button

    def init_label(self, x=None, y=None, _css=css.get('QLabel')):
        x, y = self.get_default_xy(x, y)
        # 在这里创建和设置部件
        _label = QLabel(self)
        _label.setText("这是一个标签")
        _label.move(x, y)
        _label.setStyleSheet(_css)
        return _label

    def init_box(self, x=None, y=None, value: list = None, name: str = '', _css=css.get('QComboBox')):
        x, y = self.get_default_xy(x, y)
        _combo_box = QComboBox(self)
        _combo_box.move(x, y)
        for i in value:
            _combo_box.addItem(name + i)
        # _combo_box.addItem('贷款')  # 必须先有
        # _combo_box.setCurrentText('贷款')
        selected_text = _combo_box.currentText()
        _combo_box.setStyleSheet(_css)
        return _combo_box

    def init_test_edit(self, x=None, y=None, width=None, height=None, _css=css.get('QTextEdit'), windows=None):
        x, y = self.get_default_xy(x, y)
        _test_edit = QTextEdit(windows or self)
        _test_edit.resize(width, height)
        _test_edit.move(x, y)
        # _test_edit.setStyleSheet(_css)
        font = QFont("Comic Sans MS", 13)
        _test_edit.setFont(font)
        _test_edit.setStyleSheet("""
            QTextEdit {
                color: #ADD8E6;
            }
        """)
        return _test_edit

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
        line = QPainter(self)
        pen = QPen(Qt.GlobalColor.gray, 2)
        line.setPen(pen)
        line.drawLine(150, 0, 150, 1080 * 0.7)
        line.end()

    def draw_clock(self):
        self.rhythm_flag = not self.rhythm_flag
        painter = QPainter(self)  # 创建一个画笔
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿
        x_center, y_center = 1920 * 0.7 // 2 - 130, 1080 * 0.7 // 2
        painter.translate(x_center, y_center)  # 将坐标系的原点移动到窗口的中心
        self.draw_clock_progress(painter, self.labels, 1, 330, Qt.GlobalColor.darkCyan)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 2, 280, Qt.GlobalColor.darkYellow)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 230, Qt.GlobalColor.magenta)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 2, 180, Qt.GlobalColor.darkGreen)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 4, 130, Qt.GlobalColor.darkBlue)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 80, Qt.GlobalColor.cyan)  # 绘制时钟的表面
        self.draw_ring(painter, 100, 0.4533)

    def draw_clock_progress(self, painter, labels, idx, line_start, finsh_color=Qt.GlobalColor.green,
                            not_finsh_color=Qt.GlobalColor.darkGray):
        line_num = line_start // 3 + (len(labels) - line_start // 3 % len(labels))
        size = 2  # 粗细
        len_short = 20  # 短的长度
        len_long = 40  # 长的长度
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

    def draw_ring(self, painter, side, percent):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 确保矩形的宽度和高度相等，以便绘制圆形
        rect = QRect(-side / 2, -side / 2, side, side)

        # 绘制未完成部分（）
        painter.setPen(QPen(QColor('darkGray'), 20, Qt.PenStyle.SolidLine))
        painter.drawArc(rect, 0, 360 * 16)

        # 绘制已完成部分（）
        painter.setPen(QPen(QColor(173, 216, 230), 20, Qt.PenStyle.SolidLine))
        painter.drawArc(rect, 90 * 16, -percent * 360 * 16)

        # 在圆环中央添加数字显示进度
        font = painter.font()
        font.setPointSize(18)  # 设置字体大小
        painter.setFont(font)
        painter.setPen(QColor('black'))  # 设置字体颜色
        textRect = QRect(-side / 2, -side / 2, side, side)  # 创建一个位于圆环中心的矩形区域
        progressText = "{}%".format(round(percent * 100, 1))  # 创建进度百分比的文本
        # 在指定的矩形区域内绘制文本，文本居中对齐
        painter.drawText(textRect, Qt.AlignmentFlag.AlignCenter, progressText)

    def draw_table_view(self, data: list):
        head_lst = ["Header 1", "Header 2", "Header 3"]
        head_key = ["H1", "H2", "H3"]
        model = QStandardItemModel(len(data), len(head_lst))
        model.setHorizontalHeaderLabels(head_lst)
        self.table_view = QTableView(self)
        self.table_view.move(159, 400)
        self.table_view.resize(1150, 300)  # 设置QTableView的宽度为800，高度为600
        self.table_view.setStyleSheet("""
            /* 设置表格的网格线颜色、背景色和交替背景色 */
            QTableView {
                gridline-color: black;
                background-color: rgb(108, 108, 108);
                alternate-background-color: rgb(64, 64, 64);
            }
            /* 设置单元格的内边距 */
            QTableView::item {
                padding: 5px;
            }
            /* 设置表头的背景色 */
            QHeaderView::section {
                background-color: lightgreen;
            }
            /* 设置垂直滚动条的背景色和滑块颜色 */
            QScrollBar:vertical {
                background: rgb(188, 224, 235);
            }
            QScrollBar::handle:vertical {
                background: rgb(71, 153, 176);
            }
            /* 设置水平滚动条的背景色和滑块颜色 */
            QScrollBar:horizontal {
                background: rgb(188, 224, 235);
            }
            QScrollBar::handle:horizontal {
                background: rgb(71, 153, 176);
            }
        """)

        self.table_view.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)  # 不可编辑
        for i in range(len(data)):
            line = data[i]
            for j in range(len(head_lst)):
                item = QStandardItem(str(line.get(head_key[j])))
                if (i + j) % 2 == 0:
                    item.setBackground(QColor(173, 216, 230))  # 浅蓝色
                else:
                    item.setBackground(QColor(240, 230, 140))  # 浅黄色
                model.setItem(i, j, item)
        self.table_view.setModel(model)
