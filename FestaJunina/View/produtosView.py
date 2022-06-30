from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView




class ProdutosView(QTableWidget):
    def __init__(self):
        super().__init__()
        labels = QTableWidgetItem("teste")


        self.n_colunas = 7

        self.setColumnCount(self.n_colunas)
        self.setHorizontalHeaderLabels(('ID', 'PRODUTO','QUANTIDADE', 'DESCRICAO', 'VALOR', 'ADICIONAR (+)', 'REMOVER (-)'))

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)





