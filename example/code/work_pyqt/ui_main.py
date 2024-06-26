#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 0:07
# @Author  : 刘双喜
# @File    : ui_main.py
# @Description : 添加描述
from custom_widget import *
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QPainter, QColor, QPen

class UiMainWindow(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.window_width = 3840 * 0.4
        self.window_height = 2160 * 0.4
        self.rhythm_flag = True
        self.stacked_widget = QStackedWidget()
        self.page1 = CustomWidget(self.main_window)
        self.page2 = CustomWidget(self.main_window)
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.page = CustomWidget(self.main_window)
        self.stacked_widget.setCurrentIndex(0)
        self.main_window.setCentralWidget(self.stacked_widget)
        self.init_ui()

    def init_ui(self):
        # 窗口设置
        self.set_windows()
        # 设置风格
        self.set_style()
        # 背景设置
        self.set_background()
        # 设置部件
        self.set_widget()

    def set_widget(self):
        # 部件设置
        self.but_check = QPushButton("Check", self.main_window)
        self.but_execute = QPushButton("Execute", self.main_window)
        self.but_execute.move(0, 40)
        self.but_check.clicked.connect(self.go_to_page1)
        self.but_execute.clicked.connect(self.go_to_page2)

        self.page1.init_button(370, 370)
        self.page1.init_label()
        self.page2.init_box(value=['A', 'B', 'C', 'D', 'E', 'F'], name='贷款-')
        # 菜单设置
        self.page1.init_menu(name="File", sub_name_lst=['Open', 'Save'])
        # self.page2.init_menu(name="Edit", sub_name_lst=['Copy', 'Paste'])

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def set_windows(self):
        self.main_window.setWindowTitle('我的应用')
        self.main_window.setGeometry(0, 0, self.window_width, self.window_height)
        self.main_window.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        self.set_center()

    def set_style(self):
        self.main_window.setStyleSheet(
            u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "\n"
            "SET APP STYLESHEET - FULL STYLES HERE\n"
            "DARK THEME - DRACULA COLOR BASED\n"
            "\n"
            "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "	font: 10pt \"Segoe UI\";\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Tooltip */\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(255, 121, 198);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Bg App */\n"
            "#bgApp {	\n"
            "	background"
            "-color: rgb(40, 44, 52);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Left Menu */\n"
            "#leftMenuBg {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#topLogo {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	background-image: url(:/images/images/images/PyDracula.png);\n"
            "	background-position: centered;\n"
            "	background-repeat: no-repeat;\n"
            "}\n"
            "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
            "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
            "\n"
            "/* MENUS */\n"
            "#topMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color: transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#topMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#topMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(18"
            "9, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#bottomMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#bottomMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#leftMenuFrame{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Toggle Button */\n"
            "#toggleButton {\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color: rgb(37, 41, 48);\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "	color: rgb(113, 126, 149);\n"
            "}\n"
            "#toggleButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#toggleButton:pressed {\n"
            "	background-color: rgb("
            "189, 147, 249);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#titleRightInfo { padding-left: 10px; }\n"
            "\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Extra Tab */\n"
            "#extraLeftBox {	\n"
            "	background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#extraTopBg{	\n"
            "	background-color: rgb(189, 147, 249)\n"
            "}\n"
            "\n"
            "/* Icon */\n"
            "#extraIcon {\n"
            "	background-position: center;\n"
            "	background-repeat: no-repeat;\n"
            "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
            "}\n"
            "\n"
            "/* Label */\n"
            "#extraLabel { color: rgb(255, 255, 255); }\n"
            "\n"
            "/* Btn Close */\n"
            "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
            "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Extra Content */\n"
            "#extraContent{\n"
            "	border"
            "-top: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "\n"
            "/* Extra Top Menus */\n"
            "#extraTopMenu .QPushButton {\n"
            "background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#extraTopMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Content App */\n"
            "#contentTopBg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#contentBottom{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
            "le: solid; border-radius: 4px; }\n"
            "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Theme Settings */\n"
            "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottomBar { background-color: rgb(44, 49, 58); }\n"
            "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* CONTENT SETTINGS */\n"
            "/* MENUS */\n"
            "#contentSettings .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#contentSettings .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#contentSettings .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb"
            "(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "QTableWidget */\n"
            "QTableWidget {	\n"
            "	background-color: transparent;\n"
            "	padding: 10px;\n"
            "	border-radius: 5px;\n"
            "	gridline-color: rgb(44, 49, 58);\n"
            "	border-bottom: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item{\n"
            "	border-color: rgb(44, 49, 60);\n"
            "	padding-left: 5px;\n"
            "	padding-right: 5px;\n"
            "	gridline-color: rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item:selected{\n"
            "	background-color: rgb(189, 147, 249);\n"
            "}\n"
            "QHeaderView::section{\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	max-width: 30px;\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	border-style: none;\n"
            "    border-bottom: 1px solid rgb(44, 49, 60);\n"
            "    border-right: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::horizontalHeader {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    border: 1px solid rgb(33, 37, 43);\n"
            "	background-co"
            "lor: rgb(33, 37, 43);\n"
            "	padding: 3px;\n"
            "	border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-c"
            "olor: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            ""
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     su"
            "bcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	back"
            "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "RadioButton */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ComboBox */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subco"
            "ntrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb(255, 121, 198);	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Sliders */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    h"
            "eight: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "	border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CommandLinkButton */\n"
            "QCommandLi"
            "nkButton {	\n"
            "	color: rgb(255, 121, 198);\n"
            "	border-radius: 5px;\n"
            "	padding: 5px;\n"
            "	color: rgb(255, 170, 255);\n"
            "}\n"
            "QCommandLinkButton:hover {	\n"
            "	color: rgb(255, 170, 255);\n"
            "	background-color: rgb(44, 49, 60);\n"
            "}\n"
            "QCommandLinkButton:pressed {	\n"
            "	color: rgb(189, 147, 249);\n"
            "	background-color: rgb(52, 58, 71);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Button */\n"
            "#pagesContainer QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pagesContainer QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pagesContainer QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "\n"
            "")

    def set_background(self):
        # 创建一个QPixmap对象，加载图片
        pixmap = QPixmap(r'3.png')
        pixmap = pixmap.scaled(self.main_window.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # 创建一个QPalette对象，设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))

        # 将调色板应用到主窗口
        self.main_window.setPalette(palette)

    def set_center(self):
        qr = self.main_window.frameGeometry()  # 得到矩形窗口
        cp = self.main_window.screen().availableGeometry().center()  # 计算分辨率，然后计算中心点
        qr.moveCenter(cp)  # 计算窗口中心点位置
        self.main_window.move(qr.topLeft())  # 窗口左上角移动到计算出窗口左上角位置

    def paintEvent(self, event):
        painter = QPainter(self.main_window)  # 创建一个画笔
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿
        painter.translate(self.main_window.width() / 2, self.main_window.height() / 2)  # 将坐标系的原点移动到窗口的中心
        self.rhythm_flag = not self.rhythm_flag  # 每次打印都切换长度
        self.draw_clock_progress(painter, self.main_window.labels, 1, 360)  # 绘制时钟的表面
        self.draw_clock_progress_across(painter, self.main_window.labels, 2, 330, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.main_window.labels, 3, 300, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.main_window.labels, 2, 270, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.main_window.labels, 4, 240, Qt.GlobalColor.green)  # 绘制时钟的表面
        self.draw_clock_progress(painter, self.main_window.labels, 3, 210, Qt.GlobalColor.green)  # 绘制时钟的表面

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