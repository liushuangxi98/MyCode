#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/23 12:33
# @Author  : 刘双喜
# @File    : 62.work_pyqt6.py
# @Description : 添加描述
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QWidget, \
    QPushButton, QVBoxLayout, QToolTip, QMessageBox, QLabel, QLineEdit, QProgressBar, QComboBox, QMenu
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QPainter, QColor, QPen


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
        _button = QPushButton('点击我退出', self.parent)
        _button.clicked.connect(QApplication.instance().quit)
        _button.setToolTip('这是一个按钮部件，点击它会退出程序')
        _button.move(x, y)
        self.y += 30
        return _button

    def init_label(self, x=None, y=None):
        x, y = self.get_default_xy(x, y)
        # 在这里创建和设置部件
        _label = QLabel(self.parent)
        _label.setText("这是一个标签")
        _label.move(x, y)
        return _label

    def init_box(self, x=None, y=None, value: list = None, name: str = ''):
        x, y = self.get_default_xy(x, y)
        _combo_box = QComboBox(self.parent)
        _combo_box.move(x, y)
        for i in value:
            _combo_box.addItem(name + i)
        # _combo_box.addItem('贷款')  # 必须先有
        # _combo_box.setCurrentText('贷款')
        selected_text = _combo_box.currentText()
        print(selected_text)
        return _combo_box

    def init_menu(self, x=None, y=None, name: str = ''):
        # x, y = self.get_default_xy(x, y)
        menu_bar = self.parent.menuBar()  # 创建菜单条
        file_menu = QMenu(name, self.parent)  # 菜单1-文件
        # 创建一个菜单项
        open_action = QAction(name, self.parent)
        # 将菜单项添加到菜单中
        file_menu.addAction(open_action)
        menu_bar.addMenu(file_menu)
        return file_menu

    # def init_menu(self, x=None, y=None, value: list = None, name: str = ''):
    #     x, y = self.get_default_xy(x, y)
    #
    #     _menu_bar = QMenuBar(self.parent)
    #     _menu = QMenu(name, self.parent)
    #     _menu_sub = QAction(name + ' sub', self.parent)
    #     _menu.addAction(_menu_sub)
    #     _menu_bar.addMenu(_menu)
    #     # _menu.move(x, y)
    #     return _menu
    #
    #
    # def init_menu_action(self, x=None, y=None, name: str = ''):
    #     x, y = self.get_default_xy(x, y)
    #     return _menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rhythm_flag = True
        self.labels = ['AAA', 'B', 'C', 'D', 'E']
        self.timer = QTimer()  # 创建一个定时器
        self.window_width = 1000
        self.window_height = 1000
        self.init_ui()

    def init_ui(self):
        # 窗口设置
        self.setWindowTitle('我的应用')
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)
        self.timer.timeout.connect(self.update)  # 当定时器超时时，更新窗口
        self.timer.start(500)  # 每秒触发一次定时器
        self.set_center()

        # 部件设置
        custom_widget = CustomWidget(self)
        custom_widget.init_button(370, 370)
        custom_widget.init_label()
        custom_widget.init_box(value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-')
        # 菜单设置
        file_menu = custom_widget.init_menu(name="File")


    def set_center(self):
        qr = self.frameGeometry()  # 得到矩形窗口
        cp = self.screen().availableGeometry().center()  # 计算分辨率，然后计算中心点
        qr.moveCenter(cp)  # 计算窗口中心点位置
        self.move(qr.topLeft())  # 窗口左上角移动到计算出窗口左上角位置

    def paintEvent(self, event):
        painter = QPainter(self)  # 创建一个画笔
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿
        painter.translate(self.width() / 2, self.height() / 2)  # 将坐标系的原点移动到窗口的中心
        self.rhythm_flag = not self.rhythm_flag  # 每次打印都切换长度
        self.draw_clock_progress(painter, self.labels, 1, 360)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 2, 330, Qt.GlobalColor.blue)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 300, Qt.GlobalColor.yellow)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 2, 270, Qt.GlobalColor.darkCyan)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 4, 240, Qt.GlobalColor.gray)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.labels, 3, 210, Qt.GlobalColor.lightGray)  # 绘制时钟的表面

    def draw_clock_progress(self, painter, labels, idx, line_start, finsh_color=Qt.GlobalColor.green,
                            not_finsh_color=Qt.GlobalColor.black):
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


def main():
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


button_css = '''
QPushButton {
    /* 设置按钮的背景颜色 */
    background-color: #3D94F6;
    /* 设置按钮的边框样式 */
    border-style: outset;
    /* 设置按钮的边框宽度 */
    border-width: 2px;
    /* 设置按钮的边框颜色 */
    border-color: beige;
    /* 设置按钮的字体颜色 */
    color: white;
    /* 设置按钮的字体大小 */
    font: bold 14px;
    /* 设置按钮的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置按钮的边框圆角 */
    border-radius: 10px;
}

QPushButton:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #37a0e6;
}

QPushButton:pressed {
    /* 设置鼠标按下时的背景颜色 */
    background-color: #2f89d2;
    /* 设置鼠标按下时的边框样式 */
    border-style: inset;
}
'''
label = '''
QLabel {
    /* 设置标签的背景颜色 */
    background-color: #F0F0F0;
    /* 设置标签的边框样式 */
    border-style: solid;
    /* 设置标签的边框宽度 */
    border-width: 1px;
    /* 设置标签的边框颜色 */
    border-color: #000000;
    /* 设置标签的字体颜色 */
    color: #000000;
    /* 设置标签的字体大小 */
    font: 14px;
    /* 设置标签的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置标签的边框圆角 */
    border-radius: 5px;
    /* 设置标签的内边距 */
    padding: 5px;
}

QLabel:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #E0E0E0;
}

QLabel:disabled {
    /* 设置禁用状态下的背景颜色 */
    background-color: #D0D0D0;
    /* 设置禁用状态下的字体颜色 */
    color: #808080;
}
'''
enter_edit = '''
QLineEdit {
    /* 设置输入框的背景颜色 */
    background-color: #F0F0F0;
    /* 设置输入框的边框样式 */
    border-style: solid;
    /* 设置输入框的边框宽度 */
    border-width: 1px;
    /* 设置输入框的边框颜色 */
    border-color: #000000;
    /* 设置输入框的字体颜色 */
    color: #000000;
    /* 设置输入框的字体大小 */
    font: 14px;
    /* 设置输入框的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置输入框的边框圆角 */
    border-radius: 5px;
    /* 设置输入框的内边距 */
    padding: 5px;
}

QLineEdit:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #E0E0E0;
}

QLineEdit:disabled {
    /* 设置禁用状态下的背景颜色 */
    background-color: #D0D0D0;
    /* 设置禁用状态下的字体颜色 */
    color: #808080;
}
'''
process_bar = '''
QProgressBar {
    /* 设置进度条的背景颜色 */
    background-color: #74c8ff;
    /* 设置进度条的字体颜色 */
    color: #0a9dff;
    /* 设置进度条的边框样式 */
    border-style: outset;
    /* 设置进度条的边框宽度 */
    border-width: 2px;
    /* 设置进度条的边框颜色 */
    border-color: #74c8ff;
    /* 设置进度条的边框圆角 */
    border-radius: 7px;
    /* 设置进度条的文本对齐方式 */
    text-align: left;
}

QProgressBar::chunk {
    /* 设置进度条的填充颜色 */
    background-color: #FFD700;
}
'''
pull_lst = '''
QComboBox {
    /* 设置下拉框的背景颜色 */
    background-color: #F0F0F0;
    /* 设置下拉框的边框样式 */
    border-style: solid;
    /* 设置下拉框的边框宽度 */
    border-width: 1px;
    /* 设置下拉框的边框颜色 */
    border-color: #000000;
    /* 设置下拉框的字体颜色 */
    color: #000000;
    /* 设置下拉框的字体大小 */
    font: 14px;
    /* 设置下拉框的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置下拉框的边框圆角 */
    border-radius: 5px;
    /* 设置下拉框的内边距 */
    padding: 5px;
}

QComboBox:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #E0E0E0;
}

QComboBox:disabled {
    /* 设置禁用状态下的背景颜色 */
    background-color: #D0D0D0;
    /* 设置禁用状态下的字体颜色 */
    color: #808080;
}

QComboBox::drop-down {
    /* 设置下拉按钮的样式 */
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    /* 设置下拉箭头的样式 */
    image: url(:/icons/down_arrow.png);
    width: 7px;
    height: 5px;
}

QComboBox QAbstractItemView {
    /* 设置下拉列表的样式 */
    border: 2px solid darkgray;
    selection-background-color: #111;
}
'''
box = '''
QCheckBox {
    /* 设置复选框的背景颜色 */
    background-color: #F0F0F0;
    /* 设置复选框的边框样式 */
    border-style: solid;
    /* 设置复选框的边框宽度 */
    border-width: 1px;
    /* 设置复选框的边框颜色 */
    border-color: #000000;
    /* 设置复选框的字体颜色 */
    color: #000000;
    /* 设置复选框的字体大小 */
    font: 14px;
    /* 设置复选框的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置复选框的边框圆角 */
    border-radius: 5px;
    /* 设置复选框的内边距 */
    padding: 5px;
}

QCheckBox:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #E0E0E0;
}

QCheckBox:disabled {
    /* 设置禁用状态下的背景颜色 */
    background-color: #D0D0D0;
    /* 设置禁用状态下的字体颜色 */
    color: #808080;
}

QCheckBox::indicator:checked {
    /* 设置选中状态下的样式 */
    background-color: #FFD700;
}
'''
slider = '''
QSlider {
    /* 设置滑块的最小高度 */
    min-height: 20px;
}

QSlider::groove:horizontal {
    /* 设置水平滑道的高度 */
    height: 10px;
    /* 设置滑道的背景颜色 */
    background: #d3d3d3;
    /* 设置滑道的边框圆角 */
    border-radius: 4px;
}

QSlider::handle:horizontal {
    /* 设置滑块的背景颜色 */
    background: #f0f0f0;
    /* 设置滑块的边框样式 */
    border: 1px solid #5c5c5c;
    /* 设置滑块的宽度和高度 */
    width: 18px;
    height: 18px;
    /* 设置滑块的边框圆角 */
    border-radius: 9px;
    /* 设置滑块的边距，使滑块在滑道中居中 */
    margin: -4px 0;
}

QSlider::handle:horizontal:hover {
    /* 设置鼠标悬停时滑块的背景颜色 */
    background: #a0a0a0;
}

QSlider::sub-page:horizontal {
    /* 设置滑块左侧（或上侧）滑道的背景颜色 */
    background: #5c5c5c;
    /* 设置滑道的边框圆角 */
    border-radius: 4px;
}

QSlider::add-page:horizontal {
    /* 设置滑块右侧（或下侧）滑道的背景颜色 */
    background: #c0c0c0;
    /* 设置滑道的边框圆角 */
    border-radius: 4px;
}
'''
lst_view = '''
QListView {
    /* 设置列表框的背景颜色 */
    background-color: #F0F0F0;
    /* 设置列表框的边框样式 */
    border-style: solid;
    /* 设置列表框的边框宽度 */
    border-width: 1px;
    /* 设置列表框的边框颜色 */
    border-color: #000000;
    /* 设置列表框的字体颜色 */
    color: #000000;
    /* 设置列表框的字体大小 */
    font: 14px;
    /* 设置列表框的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置列表框的边框圆角 */
    border-radius: 5px;
    /* 设置列表框的内边距 */
    padding: 5px;
}

QListView::item:hover {
    /* 设置鼠标悬停时列表项的背景颜色 */
    background-color: #E0E0E0;
}

QListView::item:selected {
    /* 设置选中状态下列表项的背景颜色 */
    background-color: #D0D0D0;
}

QListView::item:checked {
    /* 设置选中状态下列表项的背景颜色 */
    background-color: #FFD700;
}
'''
table = '''
QTableWidget {
    /* 设置表格的背景颜色 */
    background-color: #F0F0F0;
    /* 设置表格的边框样式 */
    border-style: solid;
    /* 设置表格的边框宽度 */
    border-width: 1px;
    /* 设置表格的边框颜色 */
    border-color: #000000;
    /* 设置表格的字体颜色 */
    color: #000000;
    /* 设置表格的字体大小 */
    font: 14px;
    /* 设置表格的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置表格的边框圆角 */
    border-radius: 5px;
    /* 设置表格的内边距 */
    padding: 5px;
}

QTableWidget::item {
    /* 设置表格单元格的边框样式 */
    border: 1px solid #5c5c5c;
    /* 设置表格单元格的内边距 */
    padding: 5px;
}

QTableWidget::item:hover {
    /* 设置鼠标悬停时表格单元格的背景颜色 */
    background-color: #E0E0E0;
}

QTableWidget::item:selected {
    /* 设置选中状态下表格单元格的背景颜色 */
    background-color: #D0D0D0;
}
'''
tree = '''
QTreeWidget {
    /* 设置树形控件的背景颜色 */
    background-color: #F0F0F0;
    /* 设置树形控件的边框样式 */
    border-style: solid;
    /* 设置树形控件的边框宽度 */
    border-width: 1px;
    /* 设置树形控件的边框颜色 */
    border-color: #000000;
    /* 设置树形控件的字体颜色 */
    color: #000000;
    /* 设置树形控件的字体大小 */
    font: 14px;
    /* 设置树形控件的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置树形控件的边框圆角 */
    border-radius: 5px;
    /* 设置树形控件的内边距 */
    padding: 5px;
}

QTreeWidget::item {
    /* 设置树形控件单元格的边框样式 */
    border: 1px solid #5c5c5c;
    /* 设置树形控件单元格的内边距 */
    padding: 5px;
}

QTreeWidget::item:hover {
    /* 设置鼠标悬停时树形控件单元格的背景颜色 */
    background-color: #E0E0E0;
}

QTreeWidget::item:selected {
    /* 设置选中状态下树形控件单元格的背景颜色 */
    background-color: #D0D0D0;
}
'''
dock = '''
QDockWidget {
    /* 设置停靠窗口的背景颜色 */
    background-color: #F0F0F0;
    /* 设置停靠窗口的边框样式 */
    border-style: solid;
    /* 设置停靠窗口的边框宽度 */
    border-width: 1px;
    /* 设置停靠窗口的边框颜色 */
    border-color: #000000;
    /* 设置停靠窗口的字体颜色 */
    color: #000000;
    /* 设置停靠窗口的字体大小 */
    font: 14px;
    /* 设置停靠窗口的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置停靠窗口的边框圆角 */
    border-radius: 5px;
    /* 设置停靠窗口的内边距 */
    padding: 5px;
}

QDockWidget::title {
    /* 设置标题栏的样式 */
    background-color: #D0D0D0;
    text-align: center;
    height: 24px;
}

QDockWidget::close-button, QDockWidget::float-button {
    /* 设置关闭按钮和浮动按钮的样式 */
    border: 1px solid transparent;
    background: darkgray;
    padding: 0px;
    icon-size: 12px;
    subcontrol-origin: padding;
    subcontrol-position: top right;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    /* 设置鼠标悬停时关闭按钮和浮动按钮的样式 */
    background: gray;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    /* 设置鼠标按下时关闭按钮和浮动按钮的样式 */
    background: red;
}
'''
tool_bar = '''
QToolBar {
    /* 设置工具栏的背景颜色 */
    background-color: #F0F0F0;
    /* 设置工具栏的边框样式 */
    border-style: solid;
    /* 设置工具栏的边框宽度 */
    border-width: 1px;
    /* 设置工具栏的边框颜色 */
    border-color: #000000;
    /* 设置工具栏的字体颜色 */
    color: #000000;
    /* 设置工具栏的字体大小 */
    font: 14px;
    /* 设置工具栏的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置工具栏的边框圆角 */
    border-radius: 5px;
    /* 设置工具栏的内边距 */
    padding: 5px;
}

QToolBar::handle {
    /* 设置工具栏手柄的样式 */
    image: url(:/icons/handle.png);
}

QToolBar::icon {
    /* 设置工具栏图标的样式 */
    width: 32px;
    height: 32px;
}

QToolBar::button:hover {
    /* 设置鼠标悬停时工具栏按钮的背景颜色 */
    background-color: #E0E0E0;
}

QToolBar::button:pressed {
    /* 设置鼠标按下时工具栏按钮的背景颜色 */
    background-color: #D0D0D0;
}
'''
state_bar = '''
QStatusBar {
    /* 设置状态栏的背景颜色 */
    background-color: #F0F0F0;
    /* 设置状态栏的边框样式 */
    border-style: solid;
    /* 设置状态栏的边框宽度 */
    border-width: 1px;
    /* 设置状态栏的边框颜色 */
    border-color: #000000;
    /* 设置状态栏的字体颜色 */
    color: #000000;
    /* 设置状态栏的字体大小 */
    font: 14px;
    /* 设置状态栏的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置状态栏的边框圆角 */
    border-radius: 5px;
    /* 设置状态栏的内边距 */
    padding: 5px;
}

QStatusBar::item {
    /* 设置状态栏项目的边框样式 */
    border: 1px solid #5c5c5c;
    /* 设置状态栏项目的边框圆角 */
    border-radius: 3px;
}
'''
menu = '''
/* QMenu样式 */
QMenu {
    /* 设置菜单的背景颜色 */
    background-color: #F0F0F0;
    /* 设置菜单的边框样式 */
    border-style: solid;
    /* 设置菜单的边框宽度 */
    border-width: 1px;
    /* 设置菜单的边框颜色 */
    border-color: #000000;
    /* 设置菜单的字体颜色 */
    color: #000000;
    /* 设置菜单的字体大小 */
    font: 14px;
    /* 设置菜单的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置菜单的边框圆角 */
    border-radius: 5px;
    /* 设置菜单的内边距 */
    padding: 5px;
}

QMenu::item {
    /* 设置菜单项的背景颜色 */
    background-color: #D0D0D0;
}

QMenu::item:selected {
    /* 设置选中状态下菜单项的背景颜色 */
    background-color: #FFD700;
}'''
menu_bar = '''
/* QMenuBar样式 */
QMenuBar {
    /* 设置菜单栏的背景颜色 */
    background-color: #F0F0F0;
    /* 设置菜单栏的边框样式 */
    border-style: solid;
    /* 设置菜单栏的边框宽度 */
    border-width: 1px;
    /* 设置菜单栏的边框颜色 */
    border-color: #000000;
    /* 设置菜单栏的字体颜色 */
    color: #000000;
    /* 设置菜单栏的字体大小 */
    font: 14px;
    /* 设置菜单栏的最小宽度和最小高度 */
    min-width: 10em;
    min-height: 2.5em;
    /* 设置菜单栏的边框圆角 */
    border-radius: 5px;
    /* 设置菜单栏的内边距 */
    padding: 5px;
}

QMenuBar::item {
    /* 设置菜单项的背景颜色 */
    background-color: #D0D0D0;
}

QMenuBar::item:selected {
    /* 设置选中状态下菜单项的背景颜色 */
    background-color: #FFD700;
}'''
css = {
    'QButton': button_css,
    'QLabel': label,
    'QLineEdit': enter_edit,
    'QTextEdit': enter_edit,
    'QProgressBar': process_bar,
    'QComboBox': pull_lst,
    'QCheckBox': box,  # 复选
    'QRadioButton': box,  # 单选
    'QSlider': slider,  # 滑块选值
    'QListView': lst_view,  # 列表查看
    'QTableWidget': table,  # 表格
    'QTreeWidget': tree,  # 树状结构
    'QDockWidget': dock,  # 停靠窗口
    'QToolBar': tool_bar,  # 工具栏
    'QStatusBar': state_bar,  # 底部状态栏
    'QMenu': menu,  # 菜单
    'QMenuBar': menu_bar,  # 菜单空间
}
if __name__ == '__main__':
    main()
