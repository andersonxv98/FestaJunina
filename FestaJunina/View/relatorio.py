from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView


class Relatorio(QTableWidget):
    def __init__(self):
        super().__init__()



        self.n_colunas = 7

        self.setColumnCount(self.n_colunas)
        self.setHorizontalHeaderLabels(('ID', 'PRODUTO','QUANTIDADE TOTAL'))

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
