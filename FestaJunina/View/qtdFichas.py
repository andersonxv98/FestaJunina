from PyQt6.QtGui import QWindow, QFont
from PyQt6.QtWidgets import QTableWidget, QLabel, QWidget, QVBoxLayout, QHeaderView, QAbstractItemView


class QtdFichas(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(400)
        self.n_row = 0
        self.setColumnCount(3)

        self.setHorizontalHeaderLabels(('TIPO', 'VALOR', 'QUANTIDADE'))
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
