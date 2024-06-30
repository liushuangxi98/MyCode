from PyQt6.QtWidgets import QApplication, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor
import sys


class Table(QTableView):
    def __init__(self):
        super().__init__()
        self.table_view([{'H1': 11, 'H2': 22, 'H3': 33},
                         {'H1': 111, 'H2': 222, 'H3': 333}, {'H1': 1111, 'H2': 2222, 'H3': 3333}])

    def table_view(self, data: list):
        head_lst = ["Header 1", "Header 2", "Header 3"]
        head_key = ["H1", "H2", "H3"]
        model = QStandardItemModel(len(data), len(head_lst))
        model.setHorizontalHeaderLabels(head_lst)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        for i in range(len(data)):
            line = data[i]
            for j in range(len(head_lst)):
                item = QStandardItem(str(line.get(head_key[j])))
                if (i + j) % 2 == 0:
                    item.setBackground(QColor(173, 216, 230))  # 浅蓝色
                else:
                    item.setBackground(QColor(240, 230, 140))  # 浅黄色
                model.setItem(i, j, item)
        self.setModel(model)


app = QApplication(sys.argv)
table = Table()
table.show()
sys.exit(app.exec())
