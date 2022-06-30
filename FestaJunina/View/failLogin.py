from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class FailLogin(QDialog):
    def __init__(self):
        super(FailLogin, self).__init__()
        self.setWindowTitle("ERRO AO REGISTRAR")

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.culoser)

        self.layout = QVBoxLayout()
        message = QLabel("FALHA AO LOGAR, VERIFIQUE USUARIO E SENHA")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def culoser(self):
        self.buttonBox.disconnect()
        self.close()
        print(self.parent())