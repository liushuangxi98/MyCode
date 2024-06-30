#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 20:57
# @Author  : 刘双喜
# @File    : css.py
# @Description : 添加描述
"""
Qt::color0：颜色0，通常为纯黑色
Qt::color1：颜色1，通常为纯白色
Qt::black：黑色
Qt::white：白色
Qt::darkGray：深灰色
Qt::gray：灰色
Qt::lightGray：浅灰色
Qt::red：红色
Qt::green：绿色
Qt::blue：蓝色
Qt::cyan：青色
Qt::magenta：洋红色
Qt::yellow：黄色
Qt::darkRed：深红色
Qt::darkGreen：深绿色
Qt::darkBlue：深蓝色
Qt::darkCyan：深青色
Qt::darkMagenta：深洋红色
Qt::darkYellow：深黄色
Qt::transparent：透明色
"""
css_all = """
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
"""
button_css = '''
QPushButton {
    /* 设置按钮的背景颜色 */
    background-color: transparent;
    /* 设置按钮的边框样式 */
    border-style: none;
    /* 设置按钮的边框宽度 */
    border-width: 2px;
    /* 设置按钮的边框颜色 */
    border-color: beige;
    /* 设置按钮的字体颜色 */
    color: gray;
    /* 设置按钮的字体大小 */
    font: bold 14px;
    /* 设置按钮的最小宽度和最小高度 */
    min-width: 7em;
    min-height: 2.5em;
    /* 设置按钮的边框圆角 */
    border-radius: 10px;
    /* 字体粗细 */
    font-weight: bold;
}

QPushButton:hover {
    /* 设置鼠标悬停时的背景颜色 */
    background-color: #ADD8E6;
}

QPushButton:pressed {
    /* 设置鼠标按下时的背景颜色 */
    background-color: #ADD8E6;
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
    min-width: 1em;
    min-height: 0.5px;
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
