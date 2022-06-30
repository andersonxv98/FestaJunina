class Produto:
    def __init__(self, id, nome, descricao, valor, quantidade):
        super().__init__()
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade  = quantidade




    def getId(self):
        return self.id

    def getNome(self):
        return self.nome
    def getDescricao(self):
        return self.descricao

    def getValor(self):
        return self.valor

    def getQuantidade(self):
        return self.quantidade

    def addQuantidade(self):
        self.quantidade += 1

    def rmvQuantidade(self):
        if self.quantidade > 0:
            self.quantidade -=1


    def resetQuantidade(self):
        self.quantidade = 0