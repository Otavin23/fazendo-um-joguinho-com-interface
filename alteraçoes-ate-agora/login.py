import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

from placar import Ui_Dialog
from chutar import Ui_MainWindow
from random import randint


class TelaPrimeira(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.botao)


    def botao(self):
        self.tela = Chutar()
        self.tela.show()
        self.close()


    def tempo_label(self):
        import time
        for a in range(0,10):

            tempo = time.localtime()
            texto = self.ui.label.text()
            horas = str(tempo[3])
            segundos = str(tempo[5])
            print(tempo)
            texto = self.ui.label.setText("        {}:{}".format(horas,segundos))
            time.sleep(0.3)

class Chutar(QMainWindow):
    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.chutar)

    def chutar(self):
        return self.numeros() + self.tempo_label()

    def numeros(self):

        texto = self.ui.lineEdit.text()
        chutar = randint(1,1)
        convertor = int(texto)
        if convertor == chutar:
            msg = QMessageBox()
            msg.setWindowTitle("ACERTOU")
            msg.setText("Parabens Acertou")
            msg.setStyleSheet("color: black;\n"
                              "border: none;\n"
                              "font-family:Arial,Helvetica,sans-serif;\n"
                              "background-color: white\n"
                              "font-size: 30px;\n")

            iniciar = msg.exec_()

        elif convertor != texto:
            msg = QMessageBox()
            msg.setWindowTitle("Errou")
            msg.setText("Vc errou tente novamente")
            iniciar = msg.exec_()
            msg.setObjectName("msg")
            return self.tentar_novamente()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Tente Novamente")
            msg.setText("Tente Novamente")


if __name__ == "__main__":
    import os,sys
    app = QApplication(sys.argv)
    window = TelaPrimeira()
    window.show()
    sys.exit(app.exec_())