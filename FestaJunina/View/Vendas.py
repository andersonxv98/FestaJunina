
from PyQt6.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView


class VendasView(QTableWidget):
    def __init__(self):
        super().__init__()


        self.setColumnCount(6)

        self.setHorizontalHeaderLabels(('ID', 'VALOR TOTAL', 'VALOR PAGO', 'TROCO', "DATA", "NOME VENDEDOR"))

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)

        self.setMaximumWidth(400)