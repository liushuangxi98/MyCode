from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QStackedWidget, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction

app = QApplication([])

window = QMainWindow()

# 创建一个堆栈式部件
stacked_widget = QStackedWidget(window)

# 创建一些页面
label1 = QLabel("Page 1")
label2 = QLabel("Page 2")
label3 = QLabel("Page 3")

# 将页面添加到堆栈式部件中
stacked_widget.addWidget(label1)
stacked_widget.addWidget(label2)
stacked_widget.addWidget(label3)

# 创建一个按钮
button = QPushButton("Menu", window)
button.setMenu(QMenu(window))  # 设置按钮的菜单

# 创建一些菜单项
action1 = QAction("Option 1", window)
action2 = QAction("Option 2", window)
action3 = QAction("Option 3", window)

# 当点击菜单项时，切换到对应的页面
action1.triggered.connect(lambda: stacked_widget.setCurrentIndex(0))
action2.triggered.connect(lambda: stacked_widget.setCurrentIndex(1))
action3.triggered.connect(lambda: stacked_widget.setCurrentIndex(2))

# 将菜单项添加到按钮的菜单中
button.menu().addAction(action1)
button.menu().addAction(action2)
button.menu().addAction(action3)

# 移动按钮到窗口中的其他位置
button.move(100, 100)

window.setCentralWidget(stacked_widget)
window.show()

app.exec()
