# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHUTAR.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 590)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 140, 411, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    \n"
"    font-size: 15px;\n"
"    font-family:Arial,Helvetica,sans-serif;\n"
"    padding-left:10px;\n"
"    background-color: white;\n"
"    \n"
"}\n"
"QLineEdit:hover{\n"
"    font-size: 20px;\n"
"    border-bottom: 2px solid rgb(255, 255, 0);\n"
"\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 301, 61))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"\n"
"    border: none;\n"
"    \n"
"    font-size: 17px;\n"
"    color: rgb(125, 125, 125);\n"
"    background-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"    border-bottom: 2px solid yellow;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 0, 61, 61))
        self.label_3.setStyleSheet("QLabel{\n"
"    color: wite;\n"
"    font-family:sans-serif;\n"
"    font-size: 30px;\n"
"    \n"
"    border: none;\n"
"    border-left: 2px solid white;\n"
"    background-color: rgb(54, 98, 227)\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 61, 61))
        self.label_2.setStyleSheet("QLabel{\n"
"    color: wite;\n"
"    font-family:sans-serif;\n"
"    font-size: 30px;\n"
"    \n"
"    border: none;\n"
"    border-right: 2px solid white;\n"
"    background-color: rgb(234, 115, 53)\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 151, 61))
        self.label.setStyleSheet("QLabel{\n"
"    background-color: black;\n"
"    font-size: 19px;\n"
"\n"
"    color: white;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "CHUTE UM NUMERO DE 1 A 10"))
        self.pushButton.setText(_translate("MainWindow", "Chutar"))