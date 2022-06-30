from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget, QMainWindow
from PyQt6.uic.properties import QtWidgets


class LoginView(QMainWindow):
    def __init__(self):
        super(LoginView, self).__init__()
        self.setWindowTitle("LOGAR FESTA JUNINA ANGLO")
        self.layout =  QVBoxLayout()

        self.button = QPushButton("ENTRAR")

        self.campo_usuario = QLineEdit()
        self.campo_senha = QLineEdit()
        self.campo_senha.setEchoMode(QLineEdit.EchoMode.Password)
        label_usuario = QLabel("USUARIO")
        label_senha = QLabel("SENHA")

        self.layout.addWidget(label_usuario)
        self.layout.addWidget(self.campo_usuario)
        self.layout.addWidget(label_senha)
        self.layout.addWidget(self.campo_senha)
        self.layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
