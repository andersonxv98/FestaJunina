from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel, QLineEdit

from View.alertWindow import AlertWindow


class CollectionObjts(QHBoxLayout):
    def __init__(self):
        super(CollectionObjts, self).__init__()
        self.button = QPushButton("REGISTRAR")
        self.button.setStyleSheet("background-color: LightGreen")
        #self.btn_troca = QPushButton("TROCA DE FICHA")
        #self.btn_troca.setStyleSheet("Background-color: yellow")



        self.campovalpago= QLineEdit()


        self.campovalpago.setMaximumWidth(150)
        self.campovalpago.setMinimumWidth(100)
        self.campovalpago.setFont(QFont("TIMES", 28))
        self.labelTotal = QLabel("TOTAL: TESTER")
        self.labelTotal.setFont(QFont("Helvetica", 28))
        #self.labelTotal.setMaximumWidth(200)
        self.labelTroco = QLabel("TROCO: ")
        self.labelTroco.setFont(QFont("TIMES", 28))
        self.labelTroco.setMaximumWidth(400)
        self.campovalpago.setMaxLength(6)
        #self.labelTroco.setMaximumWidth(200)







        self.addWidget(self.button)


        self.addWidget(self.campovalpago)
        self.addWidget(self.labelTotal)
        self.addWidget(self.labelTroco)
        #self.addWidget(self.btn_troca)




