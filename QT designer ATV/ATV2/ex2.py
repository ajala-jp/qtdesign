# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 801, 111))
        self.label.setStyleSheet("color:white;\n"
"border-left:2px solid red;\n"
"border-bottom:2px solid red;\n"
"border-right:2px solid red;\n"
"font-size:30px;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 210, 113, 20))
        self.lineEdit.setStyleSheet("color:white;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 210, 113, 20))
        self.lineEdit_2.setStyleSheet("color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 180, 41, 61))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:60px;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 101, 41))
        self.pushButton.setStyleSheet("color:white;\n"
"border:2px solid green;\n"
"font-size:20px;\n"
"border-radius:6px;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 420, 791, 61))
        self.label_3.setStyleSheet("color:white;\n"
"font-size:30px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 100, 461, 71))
        self.label_4.setStyleSheet("color:red;\n"
"font-size:40px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "                                   Insira 2 numeros:"))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setToolTip(_translate("MainWindow", ""))
        self.label_3.setWhatsThis(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))


    def somar(self):
        try:
                num1 = float(self.lineEdit.text())
                num2 = float(self.lineEdit_2.text())
                soma = num1 + num2
                self.label_3.setText(f"<html><head/><body><p align=\"center\">{soma}</p></body></html>")
                self.label_4.setText("")

        except ValueError:
             self.label_4.setText("Simbolo ou letra inserido!")

                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(ui.somar)
    MainWindow.show()
    sys.exit(app.exec_())
