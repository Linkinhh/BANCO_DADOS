# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oficial.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 850)
        self.oficialTab = QtWidgets.QTabWidget(Form)
        self.oficialTab.setGeometry(QtCore.QRect(0, 0, 1051, 851))
        self.oficialTab.setObjectName("oficialTab")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.panelLiderFaccao = QtWidgets.QTabWidget(self.tab_5)
        self.panelLiderFaccao.setGeometry(QtCore.QRect(20, 640, 1021, 171))
        self.panelLiderFaccao.setObjectName("panelLiderFaccao")
        self.tabAlterarNome = QtWidgets.QWidget()
        self.tabAlterarNome.setObjectName("tabAlterarNome")
        self.label = QtWidgets.QLabel(self.tabAlterarNome)
        self.label.setGeometry(QtCore.QRect(330, 60, 151, 17))
        self.label.setObjectName("label")
        self.buttonAlterarNome = QtWidgets.QPushButton(self.tabAlterarNome)
        self.buttonAlterarNome.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonAlterarNome.setObjectName("buttonAlterarNome")
        self.textAlterarNome = QtWidgets.QLineEdit(self.tabAlterarNome)
        self.textAlterarNome.setGeometry(QtCore.QRect(490, 50, 261, 31))
        self.textAlterarNome.setObjectName("textAlterarNome")
        self.panelLiderFaccao.addTab(self.tabAlterarNome, "")
        self.tabNovoLider = QtWidgets.QWidget()
        self.tabNovoLider.setObjectName("tabNovoLider")
        self.label_3 = QtWidgets.QLabel(self.tabNovoLider)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 121, 17))
        self.label_3.setObjectName("label_3")
        self.buttonNovoLider = QtWidgets.QPushButton(self.tabNovoLider)
        self.buttonNovoLider.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonNovoLider.setObjectName("buttonNovoLider")
        self.textNovoLider = QtWidgets.QLineEdit(self.tabNovoLider)
        self.textNovoLider.setGeometry(QtCore.QRect(470, 50, 261, 31))
        self.textNovoLider.setObjectName("textNovoLider")
        self.panelLiderFaccao.addTab(self.tabNovoLider, "")
        self.tabCredenciaComunidade = QtWidgets.QWidget()
        self.tabCredenciaComunidade.setObjectName("tabCredenciaComunidade")
        self.label_12 = QtWidgets.QLabel(self.tabCredenciaComunidade)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 171, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabCredenciaComunidade)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 171, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabCredenciaComunidade)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 181, 17))
        self.label_14.setObjectName("label_14")
        self.buttonCredenciarComunidade = QtWidgets.QPushButton(self.tabCredenciaComunidade)
        self.buttonCredenciarComunidade.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonCredenciarComunidade.setObjectName("buttonCredenciarComunidade")
        self.label_15 = QtWidgets.QLabel(self.tabCredenciaComunidade)
        self.label_15.setGeometry(QtCore.QRect(500, 20, 221, 17))
        self.label_15.setObjectName("label_15")
        self.textEspecieComunidade = QtWidgets.QLineEdit(self.tabCredenciaComunidade)
        self.textEspecieComunidade.setGeometry(QtCore.QRect(200, 10, 261, 31))
        self.textEspecieComunidade.setObjectName("textEspecieComunidade")
        self.textNomeComunidade = QtWidgets.QLineEdit(self.tabCredenciaComunidade)
        self.textNomeComunidade.setGeometry(QtCore.QRect(200, 50, 261, 31))
        self.textNomeComunidade.setObjectName("textNomeComunidade")
        self.textQuantidadeComunidade = QtWidgets.QLineEdit(self.tabCredenciaComunidade)
        self.textQuantidadeComunidade.setGeometry(QtCore.QRect(200, 90, 261, 31))
        self.textQuantidadeComunidade.setObjectName("textQuantidadeComunidade")
        self.textPlanetaComunidade = QtWidgets.QLineEdit(self.tabCredenciaComunidade)
        self.textPlanetaComunidade.setGeometry(QtCore.QRect(720, 10, 261, 31))
        self.textPlanetaComunidade.setObjectName("textPlanetaComunidade")
        self.panelLiderFaccao.addTab(self.tabCredenciaComunidade, "")
        self.tabRemoverFaccao = QtWidgets.QWidget()
        self.tabRemoverFaccao.setObjectName("tabRemoverFaccao")
        self.buttonRemoverFaccao = QtWidgets.QPushButton(self.tabRemoverFaccao)
        self.buttonRemoverFaccao.setGeometry(QtCore.QRect(430, 50, 151, 25))
        self.buttonRemoverFaccao.setObjectName("buttonRemoverFaccao")
        self.panelLiderFaccao.addTab(self.tabRemoverFaccao, "")
        self.tabNaoLider = QtWidgets.QWidget()
        self.tabNaoLider.setObjectName("tabNaoLider")
        self.label_5 = QtWidgets.QLabel(self.tabNaoLider)
        self.label_5.setGeometry(QtCore.QRect(380, 50, 291, 31))
        self.label_5.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.panelLiderFaccao.addTab(self.tabNaoLider, "")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(30, 150, 201, 141))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonFaccao = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonFaccao.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.radioButtonFaccao.setObjectName("radioButtonFaccao")
        self.radioButtonLider = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonLider.setGeometry(QtCore.QRect(10, 50, 112, 23))
        self.radioButtonLider.setObjectName("radioButtonLider")
        self.radioButtonComunidade = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonComunidade.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.radioButtonComunidade.setObjectName("radioButtonComunidade")
        self.radioButtonNacao = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonNacao.setGeometry(QtCore.QRect(10, 90, 141, 23))
        self.radioButtonNacao.setObjectName("radioButtonNacao")
        self.radioButtonHabitacao = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonHabitacao.setGeometry(QtCore.QRect(10, 110, 112, 23))
        self.radioButtonHabitacao.setObjectName("radioButtonHabitacao")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setGeometry(QtCore.QRect(250, 150, 775, 480))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(780, 10, 241, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.contador = QtWidgets.QLabel(self.tab_5)
        self.contador.setGeometry(QtCore.QRect(30, 300, 191, 31))
        self.contador.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.contador.setText("")
        self.contador.setObjectName("contador")
        self.oficialTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.oficialTab.addTab(self.tab_6, "")

        self.retranslateUi(Form)
        self.oficialTab.setCurrentIndex(0)
        self.panelLiderFaccao.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Novo nome da Facção"))
        self.buttonAlterarNome.setText(_translate("Form", "ENVIAR"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tabAlterarNome), _translate("Form", "Alterar nome Facção"))
        self.label_3.setText(_translate("Form", "Novo CPI do Líder"))
        self.buttonNovoLider.setText(_translate("Form", "ENVIAR"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tabNovoLider), _translate("Form", "Indicar novo líder"))
        self.label_12.setText(_translate("Form", "Nome da Comunidade"))
        self.label_13.setText(_translate("Form", "Especia da Comunidade"))
        self.label_14.setText(_translate("Form", "Quantidade de habitantes"))
        self.buttonCredenciarComunidade.setText(_translate("Form", "ENVIAR"))
        self.label_15.setText(_translate("Form", "Planeta que habita comunidade"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tabCredenciaComunidade), _translate("Form", "Credenciar comunidades novas"))
        self.buttonRemoverFaccao.setText(_translate("Form", "REMOVER FACÇÃO"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tabRemoverFaccao), _translate("Form", "Remover Facção de Nacção"))
        self.label_5.setText(_translate("Form", "Voce não é líder de Facção"))
        self.groupBox.setTitle(_translate("Form", "Pesquisar"))
        self.radioButtonFaccao.setText(_translate("Form", "Facções"))
        self.radioButtonLider.setText(_translate("Form", "Líderes"))
        self.radioButtonComunidade.setText(_translate("Form", "Comunidades"))
        self.radioButtonNacao.setText(_translate("Form", "Nações"))
        self.radioButtonHabitacao.setText(_translate("Form", "Habitações"))
        self.label_4.setText(_translate("Form", "Bem-vindo, USER"))
        self.oficialTab.setTabText(self.oficialTab.indexOf(self.tab_5), _translate("Form", "NOME_DO_CARGO"))
        self.oficialTab.setTabText(self.oficialTab.indexOf(self.tab_6), _translate("Form", "RELATÓRIOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
