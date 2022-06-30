
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QWidget, QHBoxLayout


class MsgAguarde(QWidget):
    def __init__(self):
        super(MsgAguarde, self).__init__()
        lay = QHBoxLayout()
        lb = QLabel("POR FAVOR AGUARDE")

        lay.addWidget(lb)

        self.setLayout(lay)




