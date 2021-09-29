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
        return self.numeros()

    def numeros(self):
        from random import randint

        chute = randint(1,2)
        print(chute)
        texto = self.ui.lineEdit.text()
        if chute == texto:
            msg = QMessageBox()
            msg.setWindowTitle("Acertou")
            msg.setText("ACERTOUU PARABENSS")

            iniciar = msg.exec_()
        elif texto == "" or texto == " ":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Digite Um numero")
            iniciar = msg.exec_()



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



if __name__ == "__main__":
    import os,sys
    app = QApplication(sys.argv)
    window = TelaPrimeira()
    window.show()
    sys.exit(app.exec_())