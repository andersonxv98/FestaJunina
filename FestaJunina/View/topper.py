from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout


class TopMidlleFiddleStrick(QVBoxLayout):
    def  __init__(self):
        super(TopMidlleFiddleStrick, self).__init__()
        self.btn_atualizarVendas = QPushButton("ATUALIZAR VENDAS")
        self.btn_limparCarrinho = QPushButton("LIMPAR CARRINHO")

        self.btn_atualizarVendas.setMinimumHeight(300)
        self.btn_limparCarrinho.setMinimumHeight(300)

        self.addWidget(self.btn_atualizarVendas)
        self.addWidget(self.btn_limparCarrinho)

