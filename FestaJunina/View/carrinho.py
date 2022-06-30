from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QPushButton


class Carrinho(QTableWidget):
    def __init__(self):
        super().__init__()

        self.n_rows = 0


        
        self.setRowCount(self.n_rows)
        self.setColumnCount(5)


        self.setHorizontalHeaderLabels(('REMOVER','ID', 'PRODUTO', 'DESCRICAO', 'VALOR'))

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.setMinimumWidth(800)

