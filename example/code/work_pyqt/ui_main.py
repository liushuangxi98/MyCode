#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 0:07
# @Author  : 刘双喜
# @File    : ui_main.py
# @Description : 添加描述
from custom_widget import *
from PyQt6.QtGui import QPixmap, QPalette, QBrush
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width = int(1920 * 0.7)
        self.window_height = int(1080 * 0.7)
        self.init_obj()
        self.init_ui()

    def init_obj(self):
        # 分页对象
        self.page = CustomWidget(False)
        self.page1 = CustomWidget(False)
        self.page2 = CustomWidget(True)
        self.page3 = CustomWidget(False)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.setCentralWidget(self.stacked_widget)
        # 各个业务函数对象
        self.fun1_thread = EventThread('fun1')
        self.fun1_thread.event.connect(self.fun1_ret)

    def fun1_task(self):
        if self.fun1_thread.running is False:
            self.fun1_thread.start()
        else:
            self.fun1_ret('正在运行，请稍后')

    def fun1_ret(self, ret):
        self.print(ret)

    def init_ui(self):
        # 窗口设置
        self.set_windows()
        # 设置风格
        # self.set_style()
        # 背景设置
        self.set_background()
        # 设置部件
        self.set_widget()

    def set_widget(self):
        # 主界面部件
        self.but_check = self.page.init_button(0, 10, name='天天发财', windows=self)
        self.but_execute = self.page.init_button(0, 70, name='年年好运', windows=self)
        self.but_ins = self.page.init_button(0, 130, name='事事顺利', windows=self)
        self.but_check.clicked.connect(self.go_to_page1)
        self.but_execute.clicked.connect(self.go_to_page2)
        self.but_ins.clicked.connect(self.go_to_page3)
        self.test_edit = self.page.init_test_edit(self.window_width // 1.4 + 10, 10, width=360, height=200, windows=self)

        # 页面1 按钮
        y1 = 10
        self.page1.init_box(200, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-')
        self.page1.init_box(300, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-1')
        self.page1.init_box(400, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-2')
        self.page1.init_box(500, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-3')
        self.page1.init_box(600, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-4')
        self.page1.init_box(700, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-5')
        self.page1.init_box(800, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-6')
        y1 += 50
        self.page1.init_box(200, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-')
        self.page1.init_box(300, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-1')
        self.page1.init_box(400, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-2')
        self.page1.init_box(500, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-3')
        self.page1.init_box(600, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-4')
        self.page1.init_box(700, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-5')
        self.page1.init_box(800, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-6')
        y1 += 50
        self.page1.init_box(200, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-')
        self.page1.init_box(300, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-1')
        self.page1.init_box(400, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-2')
        self.page1.init_box(500, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-3')
        self.page1.init_box(600, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-4')
        self.page1.init_box(700, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-5')
        self.page1.init_box(800, y1, value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-6')
        y1 += 50
        self.p1b1 = self.page1.init_button(200, y1, name='好的看看')
        self.p1b1.clicked.connect(self.fun1_task)
        self.page1.init_button(400, y1, name='好的再看看')

        # 菜单设置
        # self.page1.init_menu(name="File", sub_name_lst=['Open', 'Save'])
        # self.page2.init_menu(name="Edit", sub_name_lst=['Copy', 'Paste'])

    def print(self, text):
        self.test_edit.insertPlainText(str(text) + '\n')

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_page2(self):
        # self.update()
        self.page2.update()
        self.stacked_widget.setCurrentIndex(1)

    def go_to_page3(self):
        self.page3.draw_table_view([{'H1': 11, 'H2': 22, 'H3': 33}, {'H1': 111, 'H2': 222, 'H3': 333},
                               {'H1': 1111, 'H2': 2222, 'H3': 3333}])
        self.stacked_widget.setCurrentIndex(2)

    def set_windows(self):
        self.setWindowTitle('我的应用')
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        self.set_center()

    def set_background(self):
        # 创建一个QPixmap对象，加载图片
        pixmap = QPixmap(r'2.png')
        pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)

        # 创建一个QPalette对象，设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))

        # 将调色板应用到主窗口
        self.setPalette(palette)

    def set_center(self):
        qr = self.frameGeometry()  # 得到矩形窗口
        cp = self.screen().availableGeometry().center()  # 计算分辨率，然后计算中心点
        qr.moveCenter(cp)  # 计算窗口中心点位置
        self.move(qr.topLeft())  # 窗口左上角移动到计算出窗口左上角位置

    def set_style(self):
        self.setStyleSheet(css_all)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
