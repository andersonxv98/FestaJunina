import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QWindow
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QVBoxLayout, QDialog

from DAO.ProdutosDAO import ProdutosDAO
from DAO.VendaDao import VendaDAO
from DAO.Venda_ProdutoDAO import Venda_ProdutoDAO

from DAO.conexao import Conexao
from Model.Produto import Produto
from Model.Venda import Venda
from View.Vendas import VendasView
from View.aguarde import MsgAguarde
from View.alertWindow import AlertWindow

from View.carrinho import Carrinho
from View.finalColletionsObjcts import CollectionObjts
from View.maskRSbb import Mask
from View.msgErro import MsgErro
from View.produtosView import ProdutosView
from View.qtdFichas import QtdFichas
from View.reset import ResetBtn
from View.topper import TopMidlleFiddleStrick


class MainController:
    def __init__(self, id_user):
        self.btn_reset = ResetBtn()
        self.conection = Conexao()
        self.id_user = id_user
        self.dialog = AlertWindow()
        self.viewFichas = QtdFichas()
        self.viewCarrinho= Carrinho()
        self.viewProdutos = ProdutosView()
        self.viewVendas = VendasView()
        self.footer = CollectionObjts()
        self.footer.button.clicked.connect(lambda : self.RegistrarCompra(0))
        self.footer.campovalpago.textChanged.connect(self.CalcularTroco)
        #self.footer.btn_troca.clicked.connect(lambda : self.RegistrarCompra(1))

        self.labelOriFich = []
        self.valorlabelDriFich = []
        self.textovirgemLabelsFichas = []
        self.mask = Mask()
        self.produtos = []
        self.conti = 0

        self.venda_new = Venda(None,None,None,0,None, None, None)
        super().__init__()
        #print("TESTE")
        self.n_rows = 0
        self.n_rowsCarrinho = 0
        self.mostrarProdutos()
        #self.instantLabFichas()
        self.barraPesquisa = QLineEdit()

        self.topButtons= TopMidlleFiddleStrick()
        self.topButtons.btn_limparCarrinho.clicked.connect(self.LimparCarrinhoEoutros)
        self.topButtons.btn_atualizarVendas.clicked.connect(self.AtualizarVendas)
        self.barraPesquisa.textChanged.connect(lambda : self.PesquisarItemONVIewProduto(self.barraPesquisa.text().upper()))
        self.btn_reset.clicked.connect(self.LimparCarrinhoEoutros)
        #self.btn_reset.clicked.connect(self.mostrarProdutos)
        self.btn_reset.clicked.connect(self.AtualizarVendas)

    def PesquisarItemONVIewProduto(self, texto):
        #print("TEXTO DE PESQUISA: ", texto)
        n_rw = self.viewProdutos.rowCount()
        for ln in  range(n_rw):
            odd_obj = self.viewProdutos.cellWidget(ln, 1)
            #print(odd_obj.text())
            if texto not in odd_obj.text():
                self.viewProdutos.hideRow(ln) # setStyleSheet("background-color: lightBLUE")
            else:
                self.viewProdutos.showRow(ln)

    def mostrarProdutos(self):
        #print("ENTROU FUNCAO MOSTRAR PRODUTOS CONTTORLER")
        produtosdao = ProdutosDAO(self.conection)
        self.resultado = produtosdao.getProdutosDAO()
        #print("RESULTADO DE PRODUTOS: ", self.resultado)
        fichastipo = []
        qttLinhaas = len(self.resultado)
        self.viewProdutos.setRowCount(qttLinhaas)
        for item in self.resultado:
            obj_produto = Produto(item[0], item[1], item[2], item[3], 0)
            #self.CarregaRelatorio(item[0])
            #print("VALOR ITEM[3]", item[3])
            self.InsereProdutoNaViewProduto(obj_produto)
            val = self.formatar2casas((obj_produto.getValor()))
            #print("VAL NA FUNC MOSTRARPROD: ",val)
            if( val not in fichastipo):
                self.InstanciarFichasLabels(val)
                fichastipo.append(val)

    def CarregaRelatorio(self, id_prod):
        vv = Venda_ProdutoDAO(self.conection)
        total = vv.getQuantItensVendidos(id_prod)
        #print("QUANTIDADE TOTAL DO ITEM: ", id_prod, "TOTAL: ", total)

    def InsereProdutoNaViewProduto(self, produto_obj):
        self.btn_add = QPushButton("ADICIONAR")
        self.btn_remov = QPushButton("REMOVER")
        val_prod = [produto_obj.getId(), produto_obj.getNome(), produto_obj.getQuantidade(),produto_obj.getDescricao(),
                    self.formatar2casas(produto_obj.getValor()), self.btn_add, self.btn_remov]
        self.produtos.append(produto_obj)
        label_qantidade = QLabel(str(val_prod[2]))
        label_qantidade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_qantidade.setFont(QFont("Times", 18))
        label_valor =  QLabel(self.mask.text() +str(val_prod[4]))
        label_valor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_valor.setFont(QFont("Times", 18))
        objeto_tratados_pro_front = [
            QLabel(str(val_prod[0])),
            QLabel(str(val_prod[1])),
            label_qantidade,
            QLabel(str(val_prod[3])),
            label_valor,
            self.btn_add,
            self.btn_remov
        ]
        odj = self.produtos[self.conti]
        self.btn_add.clicked.connect(lambda: self.insereProdutoCarrinho(odj))
        self.btn_remov.clicked.connect(lambda: self.removePRodutoCarrinho(odj))
        #print(self.produtos, "Contador: ", self.conti)
        self.conti += 1
        contador = 0
        for item in objeto_tratados_pro_front:
            item.setStyleSheet("background-color: #adffed")
            self.viewProdutos.setCellWidget(self.n_rows, contador, item)
            if item == self.btn_remov:
                item.setStyleSheet("Background-color:#F56350")
            elif item ==self.btn_add:
                item.setStyleSheet("background-color: #B5FC12")
            contador += 1
        self.n_rows += 1

    def AddValuesDeFichasLikeLabels(self, value):
        qtt_ln = self.viewFichas.rowCount()
        for j in range(qtt_ln):
            cell = self.viewFichas.cellWidget(j, 1)
            if (float(cell.text()) == value):
                cell_resul = self.viewFichas.cellWidget(j, 2)
                #print("CELL_result.TExt(): ", cell_resul.text())
                resul = int(cell_resul.text()) + 1
                cell_resul.setText(str(resul))
                cell_resul.setStyleSheet("background-color: #A5F58E")
                cell.setStyleSheet("background-color: #A5F58E")
                self.viewFichas.showRow(j)

    def InstanciarFichasLabels(self, value):
        #print("VALUEUS: ", value)
        label   = QLabel("FICHAS DE VALOR R$ ")
        val_label = QLabel(str(value))
        label.setFont(QFont("TIMES", 18))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        val_label.setFont(QFont("TIMES", 18))
        val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        qtt = QLabel("0")
        qtt.setFont(QFont("TIMES", 18))
        qtt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.textovirgemLabelsFichas.append(label.text())
        #self.valorlabelDriFich.append(int(val_label.text()))
        self.viewFichas.setRowCount(self.viewFichas.n_row +1)
        self.viewFichas.setCellWidget(self.viewFichas.n_row, 0, label)
        self.viewFichas.setCellWidget(self.viewFichas.n_row, 1, val_label)
        self.viewFichas.setCellWidget(self.viewFichas.n_row, 2, qtt)
        self.viewFichas.hideRow(self.viewFichas.n_row)
        self.viewFichas.n_row += 1
        self.viewFichas.sortItems(2,order= Qt.SortOrder.AscendingOrder)

    def insereProdutoCarrinho(self, obj):
        self.CalculaQtdFichasAseremEntregues(obj.getValor())
        self.viewCarrinho.setRowCount(self.n_rowsCarrinho +1)
        btn_remov = QPushButton("REMOVER")
        val_prod = [btn_remov, obj.getId(), obj.getNome(),  obj.getDescricao(),
                    self.formatar2casas(obj.getValor())]

        label_valor = QLabel(self.mask.text() +str(val_prod[4]))
        label_valor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_valor.setFont(QFont("TIMES", 18))

        label_id =  QLabel(str(val_prod[1]))
        label_id.setFont(QFont("TIMES", 1))
        label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        objeto_tratados_pro_front = [
            btn_remov,
            label_id,
            QLabel(str(val_prod[2])),
            QLabel(str(val_prod[3])),
            label_valor
        ]

        btn_remov.clicked.connect(lambda: self.removePRodutoCarrinho(obj))
        contador = 0
        for item in objeto_tratados_pro_front:
            self.viewCarrinho.setCellWidget(self.n_rowsCarrinho, contador, item)
            contador += 1

        self.n_rowsCarrinho += 1
        obj.addQuantidade()
        self.AtualizarQtdDeItens(obj)
        self.somarTotal(obj)
        self.AddValuesDeFichasLikeLabels(obj.getValor())

    def removePRodutoCarrinho(self, obj):
        #print("FALSE")
        #print(obj)
        if obj.getQuantidade() >  0:
            self.RMvQtdFichasAseremEntregues(obj.getValor())
        obj.rmvQuantidade()
        self.AtualizarQtdDeItens(obj)
        self.RemovePRodutoViewCarrinho(obj)
        self.subtrairTotal(obj)
        #print(self.venda_new.VetorProdutos)
        #self.rmv(obj)

    def CalcularTroco(self):

        camp = self.footer.campovalpago.text()
        if "," in camp:
            camp = camp.split(',')
            camp = camp[0]+ '.' + camp[1]

        try:
            total = self.venda_new.getTotal()
            valor_pago = float(camp)
            troco = valor_pago - total
            text  = "TROCO: R$ "+str(self.formatar2casas(troco))
            self.footer.labelTroco.setText(text)
        except:
            #print("ALGO INESPERADO ACONTECEU")
            #print("CALCULO DO TROCO NÃO PODE SER EFETUADO")
            return

    def RegistrarCompra(self, param):
        self.dialog.buttonBox.accepted.connect(lambda : self.RegistrarVendaBanco(param))
        self.dialog.exec()

    def InsereProdutoNaViewProdutoCarinhho(self, produto_obj):
        #self.CalculaQtdFichasAseremEntregues()
        btn_remov = QPushButton("REMOVER")

        id = produto_obj.getId
        id = 1
        val_prod = [id, produto_obj.getNome, produto_obj.getDescricao,
                    produto_obj.getValor, btn_remov]
        btn_remov.clicked.connect(lambda: self.RemovePRodutoViewCarrinho(id))
        contador = 0
        for item in val_prod:
            self.viewCarrinho.setItem(self.n_rows, contador, item)
            contador += 1
        self.n_rows += 1

    def RemovePRodutoViewCarrinho(self, obj):
        row_n = self.viewCarrinho.rowCount()
        id_objto = str(obj.getId())
        for i in range(row_n):
            cell_row_id = self.viewCarrinho.cellWidget(i, 1).text()
            if (id_objto == cell_row_id):
                self.n_rowsCarrinho -= 1
                self.viewCarrinho.removeRow(i)
                break

    def AtualizarQtdDeItens(self, obj):
        label = QLabel(str(obj.getQuantidade()))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("TIMES", 18))
        value = "#adffed"
        if int(label.text()) > 0:
            value = "#feffa3"
        label.setStyleSheet("background-color: " + value)
        row_cout  = self.viewProdutos.rowCount()
        for i in range(row_cout):
            odk = self.viewProdutos.cellWidget(i, 0).text()
            #print(odk)
            if obj.getId() == int(odk):
                self.viewProdutos.setCellWidget(i, 2, label)

    def somarTotal(self, obj):
        self.venda_new.AdicionarProdutos(obj)
        self.CalcularTotal()
        self.CalcularTroco()

    def subtrairTotal(self, obj):
        self.venda_new.RemoverProdutos(obj)
        self.CalcularTotal()
        self.CalcularTroco()

    def CalcularTotal(self):
        sum_total = self.venda_new.getTotal()
        self.footer.labelTotal.setText("TOTAL: R$ "+str(self.formatar2casas(sum_total)))

    def RegistrarVendaBanco(self, trocaouvenda):
        self.dialog.hide()
        vendaDao = VendaDAO(self.conection)
        total =self.venda_new.getTotal()
        val_pago = self.footer.campovalpago.text()
        if "," in val_pago:
            val_pago = val_pago.split(',')
            val_pago = val_pago[0]+ '.' + val_pago[1]
        try:
            a = float(val_pago)
            cesta = self.venda_new.VetorProdutos
            if a >= total and  len(cesta) >0 :
                val_troco = self.footer.labelTroco.text()
                troquim = val_troco.split(": ")
                troquim = troquim[1].split("R$")
                #print("VALOR DO TROCO: ", troquim)
                #print("VALOR PAGO: ", val_pago)
                #print("VALOR TOTAL: ", total)
                id_vendas_db = vendaDao.insertVendaDAO(val_pago, total, troquim[1], trocaouvenda, self.id_user)
                i = 0

                for produto in cesta:
                    vv = Venda_ProdutoDAO(self.conection)
                    vv.InsertVenda_ProdutosDAO(id_vendas_db[0][0], produto.getId())
                    #print("ENTROU NO LOOP? ", i)
                    i+= 1
                self.LimparCarrinhoEoutros()
                #print("LIMPOU CARRINHO")
                self.dialog.buttonBox.accepted.disconnect()
            else:
                erro = MsgErro()
                erro.exec()
                self.dialog.buttonBox.accepted.disconnect()
        except:
            #print("EXEÇÂO FORA DO TRY: REGISTRARVENDABANCO")
            erro = MsgErro()
            erro.exec()
            self.dialog.buttonBox.accepted.disconnect()
        self.dialog.close()
        self.AtualizarVendas()

    def LimparCarrinhoEoutros(self):
        self.venda_new = Venda(None, None, None, 0, None, None, None)
        # self.viewCarrinho.clear()
        while (self.viewCarrinho.rowCount() > 0):
            self.viewCarrinho.removeRow(0)
        self.n_rowsCarrinho = 0
        self.viewCarrinho.setHorizontalHeaderLabels(('REMOVER', 'ID', 'PRODUTO', 'DESCRICAO', 'VALOR'))
        self.ResetarQtdProdutosLista()
        self.ResetLabels()

    def ResetarQtdProdutosLista(self):
        row_b  = self.viewProdutos.rowCount()
        for prod in self.produtos:
            prod.resetQuantidade()
        for x in range(row_b):
            label = QLabel("0")
            label.setFont(QFont("Times", 18))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("background-color:  #adffed")
            self.viewProdutos.setCellWidget(x, 2, label)

    def ResetLabels(self):
        self.footer.labelTotal.setText("TOTAL R$")
        self.footer.campovalpago.setText("")
        self.footer.labelTroco.setText("TROCO: ")
        self.instantLabFichas()


    def AtualizarVendas(self):
        vendaDao = VendaDAO(self.conection)
        resultado = vendaDao.getVendasDAO()
        cp = 0
        qttLinhasviewVendas = len(resultado)
        self.viewVendas.setRowCount(qttLinhasviewVendas)
        for item in resultado:
            #print("ID VENDA: ", item[0], "DATA: ",item[4], "Total: ", item[1], "troca de ficha", item[5], "valor Pago: ", item[2], "troco", item[3], "NOME: ", item[6])
            fch = "NÃO"
            #print("VALOR ITEM: ", item)
            #print("VALOR ITEM[5]", item[5])
            if item[5] == 1:
                fch = "SIM"
            obj_venda = Venda(item[0], item[4], self.formatar2casas(item[2]), self.formatar2casas(item[1]), self.formatar2casas(item[3]), fch, item[6])
            self.InsereVendaNaViewVendas(obj_venda, cp)
            cp += 1

    def InsereVendaNaViewVendas(self, obj_venda, row):
        tm_fonte  = 10
        label_id = QLabel(str(obj_venda.getId()))
        label_id.setFont(QFont("Times", tm_fonte))
        label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_valor = QLabel(self.mask.text() +str(obj_venda.getTotal()))
        label_valor.setFont(QFont("Times", tm_fonte))
        label_valor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_Valorpago = QLabel(self.mask.text() +str(obj_venda.getValorPago()))
        label_Valorpago.setFont(QFont("Times", tm_fonte))
        label_Valorpago.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_Troco = QLabel(self.mask.text() +str(obj_venda.getTroco()))
        label_Troco.setFont(QFont("Times", tm_fonte))
        label_Troco.setAlignment(Qt.AlignmentFlag.AlignCenter)

        data = QLabel(str(obj_venda.getData()))
        data.setFont(QFont("Times", tm_fonte))
        data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #ficha = QLabel(str(obj_venda.getFicha()))
        #ficha.setFont(QFont("Times", tm_fonte))
        #ficha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        id_vendedor = QLabel(str(obj_venda.getIdVendedor()))
        id_vendedor.setFont(QFont("Times", tm_fonte))
        id_vendedor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        objeto_tratados_pro_front = [
            label_id, label_valor,
            label_Valorpago, label_Troco,
            data,
            #ficha,
            id_vendedor
        ]

        contador = 0
        for item in objeto_tratados_pro_front:
            venda_dao = VendaDAO(self.conection)
            resultado = venda_dao.getLastVendaPerID(self.id_user)
            if obj_venda.getId() == resultado:
                item.setStyleSheet("background-color: orange")
            self.viewVendas.setCellWidget(row, contador, item)
            contador += 1

    def instantLabFichas(self):
        cont = self.viewFichas.rowCount()
        for ct in range(cont):
            obj = self.viewFichas.cellWidget(ct, 2)
            ant_obj = self.viewFichas.cellWidget(ct, 1)
            resul = 0
            obj.setText(str(resul))
            ant_obj.setStyleSheet("background-coler: #ffffff")
            obj.setStyleSheet("background-coler: #ffffff")
            self.viewFichas.hideRow(ct)
    def RMvQtdFichasAseremEntregues(self, valor):
        cont = self.viewFichas.rowCount()
        for ct in range(cont):
            lb = self.viewFichas.cellWidget(ct, 1)
            if str(valor) in lb.text():
                #print("VALOR LB DE COMPARE: ", lb.text())
                obj = self.viewFichas.cellWidget(ct,2).text()
                #print("OBJETO QT WIDGET: ", obj)
                vl = int(obj)
                if ( vl> 0):
                    resul = vl -1
                    self.viewFichas.cellWidget(ct, 2).setText(str(resul))
                    m = self.viewFichas.cellWidget(ct, 2).text()
                    if m == '0':
                        self.viewFichas.cellWidget(ct, 2).setStyleSheet("background-color: #ffffff")
                        self.viewFichas.cellWidget(ct,1).setStyleSheet("background-color: #ffffff")
                        self.viewFichas.hideRow(ct)
    def CalculaQtdFichasAseremEntregues(self, valor):
        cont = 0
        for lb in self.labelOriFich:
            #print(lb.text())
            texto  = self.textovirgemLabelsFichas[cont]
            if str(valor) in lb.text():
                self.valorlabelDriFich[cont] += 1
                lb.setText(str(texto +"  " + str(self.valorlabelDriFich[cont])))
            cont += 1

    def formatar2casas(self, value):
        r = "{:.2f}".format(value)
        return r