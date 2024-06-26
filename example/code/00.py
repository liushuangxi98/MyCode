from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QVBoxLayout, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        self.page1 = QWidget()
        self.page2 = QWidget()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        self.button1 = QPushButton("Go to Page 2")
        self.button1.clicked.connect(self.go_to_page2)

        self.button2 = QPushButton("Go back to Page 1")
        self.button2.clicked.connect(self.go_to_page1)

        self.label1 = QLabel("This is Page 1")
        self.label2 = QLabel("This is Page 2")

        layout1 = QVBoxLayout(self.page1)
        layout1.addWidget(self.label1)
        layout1.addWidget(self.button1)

        layout2 = QVBoxLayout(self.page2)
        layout2.addWidget(self.label2)
        layout2.addWidget(self.button2)

        self.setCentralWidget(self.stacked_widget)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
