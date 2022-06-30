class Venda:
    def __init__(self, id, data, valorpago, valortotal, troco, ficha, id_vendedor):
        super().__init__()
        self.id = id
        self.VetorProdutos = []
        self.totalVenda = valortotal
        self.data = data
        self.valorpago = valorpago
        self.ficha = ficha
        self.troco = troco
        self.id_vendedor = id_vendedor
    def AdicionarProdutos(self, produto):
        self.VetorProdutos.append(produto)
        self.totalVenda += produto.getValor()

    def RemoverProdutos(self, produto):
        if produto in self.VetorProdutos:
            self.VetorProdutos.remove(produto)
            self.totalVenda -= produto.getValor()

    def LimparTudo(self):
        self.VetorProdutos = []
        self.id = None
        self.totalVenda = 0

    def getTotal(self):
        return self.totalVenda
    def getId(self):
        return  self.id
    def getTroco(self):
        return self.troco
    def getFicha(self):
        return self.ficha
    def getValorPago(self):
        return self.valorpago
    def getData(self):
        return self.data
    def getIdVendedor(self):
        return self.id_vendedor