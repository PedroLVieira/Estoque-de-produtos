# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pedro\OneDrive\Desktop\Engenharia de software\Estoque-de-produtos\tabela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableprod = QtWidgets.QTableWidget(self.centralwidget)
        self.tableprod.setGeometry(QtCore.QRect(140, 120, 411, 331))
        self.tableprod.setObjectName("tableprod")
        self.tableprod.setColumnCount(4)
        self.tableprod.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableprod.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableprod.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableprod.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.tableprod.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.produtos = QtWidgets.QPushButton(self.centralwidget)
        self.produtos.setGeometry(QtCore.QRect(230, 10, 75, 23))
        self.produtos.setObjectName("produtos")
        self.cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrar.setGeometry(QtCore.QRect(370, 10, 75, 23))
        self.cadastrar.setObjectName("cadastrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableprod.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableprod.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableprod.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Preço"))
        item = self.tableprod.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantidade"))
        self.label.setText(_translate("MainWindow", "Produtos"))
        self.produtos.setText(_translate("MainWindow", "produtos"))
        self.cadastrar.setText(_translate("MainWindow", "Cadastrar"))

def cdst():
    tabela.close()
    cadastro.show()



tabela=uic.loadUi("tabela.ui")
cadastro=uic.loadUi("cadastro.ui")
tabela.cadastrar.clicked.connect(cdst)
