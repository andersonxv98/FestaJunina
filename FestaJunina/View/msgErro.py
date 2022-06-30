from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox


class MsgErro(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ERRO AO REGISTRAR")

        QBtn = QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        #self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("FAVOR INSERIR UM VALOR DE PAGAMENTO VÁLIDO")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
