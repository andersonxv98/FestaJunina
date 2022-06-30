from poplib import POP3_SSL

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget

from Controllers.controller import MainController



class MainWindow(QMainWindow):
    def __init__(self, id_user):
        super(MainWindow, self).__init__()
        self.id_user = id_user
        self.setWindowTitle("TESTE")
        self.layout =QVBoxLayout()



        layoutcima = QHBoxLayout()
        layoutbaixo = QHBoxLayout()
        prodLayout =  QVBoxLayout()




        P_control =  MainController(self.id_user)

        topbtns = P_control.topButtons
        tabelaProdutos =P_control.viewProdutos
        novaVenda = P_control.viewCarrinho
        qtdFichas = P_control.viewFichas
        tabelaRegistroVendas = P_control.viewVendas
        barra_pesquisa = P_control.barraPesquisa
        btn_reset = P_control.btn_reset

        #layoutcima.addLayout(topbtns)
        layoutcima.addWidget(tabelaRegistroVendas)
        #layoutcima.addWidget(tabelaProdutos)
        prodLayout.addWidget(barra_pesquisa)
        prodLayout.addWidget(tabelaProdutos)
        layoutcima.addLayout(prodLayout)
        layoutbaixo.addWidget(novaVenda)
        layoutbaixo.addWidget(qtdFichas)

        self.layoutCollections = P_control.footer


        self.layout.addWidget(btn_reset)
        self.layout.addLayout(layoutcima)
        self.layout.addLayout(layoutbaixo)
        self.layout.addLayout(self.layoutCollections)

        self.layoutCollections.setAlignment(Qt.AlignmentFlag.AlignRight)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

