# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.frame.setStyleSheet("background-color: rgb(1, 0, 5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 380, 51, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(90, 430, 81, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(110, 30, 261, 261))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("login/images/GALAXIA.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(190, 300, 121, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 32pt \"Ubuntu\";")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 530, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 50 18pt \"Ubuntu\";")
        self.pushButton.setObjectName("pushButton")
        self.senha_text_box = QtWidgets.QLineEdit(self.frame)
        self.senha_text_box.setGeometry(QtCore.QRect(190, 430, 211, 31))
        self.senha_text_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.senha_text_box.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_text_box.setObjectName("senha_text_box")
        self.CPI_text_box = QtWidgets.QLineEdit(self.frame)
        self.CPI_text_box.setGeometry(QtCore.QRect(190, 380, 211, 31))
        self.CPI_text_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CPI_text_box.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.CPI_text_box.setObjectName("CPI_text_box")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.frame.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("Form", "CPI"))
        self.label_6.setText(_translate("Form", "SENHA"))
        self.label_8.setText(_translate("Form", "LOGIN"))
        self.pushButton.setText(_translate("Form", "FAZER LOGIN"))
        self.senha_text_box.setPlaceholderText(_translate("Form", "Digite sua senha"))
        self.CPI_text_box.setPlaceholderText(_translate("Form", "Digite seu CPI"))
