from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMenuBar, QMenu
from PyQt6.QtGui import QAction

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.menu_bar = QMenuBar(self)
        self.menu_bar.setGeometry(0, 0, self.width(), 30)

        self.file_menu = QMenu("File", self)
        self.menu_bar.addMenu(self.file_menu)

        self.open_action = QAction("Open", self)
        self.file_menu.addAction(self.open_action)

        self.save_action = QAction("Save", self)
        self.file_menu.addAction(self.save_action)

app = QApplication([])
window = CustomWidget()
window.show()
app.exec()
