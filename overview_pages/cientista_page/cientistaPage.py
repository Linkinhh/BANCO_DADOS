# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cientista.ui'
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
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label = QtWidgets.QLabel(self.tab_7)
        self.label.setGeometry(QtCore.QRect(330, 60, 151, 17))
        self.label.setObjectName("label")
        self.buttonAlterarNome = QtWidgets.QPushButton(self.tab_7)
        self.buttonAlterarNome.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonAlterarNome.setObjectName("buttonAlterarNome")
        self.textAlterarNome = QtWidgets.QLineEdit(self.tab_7)
        self.textAlterarNome.setGeometry(QtCore.QRect(490, 50, 261, 31))
        self.textAlterarNome.setObjectName("textAlterarNome")
        self.panelLiderFaccao.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_3 = QtWidgets.QLabel(self.tab_8)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 121, 17))
        self.label_3.setObjectName("label_3")
        self.buttonNovoLider = QtWidgets.QPushButton(self.tab_8)
        self.buttonNovoLider.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonNovoLider.setObjectName("buttonNovoLider")
        self.textNovoLider = QtWidgets.QLineEdit(self.tab_8)
        self.textNovoLider.setGeometry(QtCore.QRect(470, 50, 261, 31))
        self.textNovoLider.setObjectName("textNovoLider")
        self.panelLiderFaccao.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_12 = QtWidgets.QLabel(self.tab_9)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 171, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_9)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 171, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_9)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 181, 17))
        self.label_14.setObjectName("label_14")
        self.buttonCredenciarComunidade = QtWidgets.QPushButton(self.tab_9)
        self.buttonCredenciarComunidade.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.buttonCredenciarComunidade.setObjectName("buttonCredenciarComunidade")
        self.label_15 = QtWidgets.QLabel(self.tab_9)
        self.label_15.setGeometry(QtCore.QRect(500, 20, 221, 17))
        self.label_15.setObjectName("label_15")
        self.textEspecieComunidade = QtWidgets.QLineEdit(self.tab_9)
        self.textEspecieComunidade.setGeometry(QtCore.QRect(200, 10, 261, 31))
        self.textEspecieComunidade.setObjectName("textEspecieComunidade")
        self.textQuantidadeComunidade = QtWidgets.QLineEdit(self.tab_9)
        self.textQuantidadeComunidade.setGeometry(QtCore.QRect(200, 90, 261, 31))
        self.textQuantidadeComunidade.setObjectName("textQuantidadeComunidade")
        self.textPlanetaComunidade = QtWidgets.QLineEdit(self.tab_9)
        self.textPlanetaComunidade.setGeometry(QtCore.QRect(720, 10, 261, 31))
        self.textPlanetaComunidade.setObjectName("textPlanetaComunidade")
        self.textNomeComunidade = QtWidgets.QLineEdit(self.tab_9)
        self.textNomeComunidade.setGeometry(QtCore.QRect(200, 50, 261, 31))
        self.textNomeComunidade.setObjectName("textNomeComunidade")
        self.panelLiderFaccao.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.buttonRemoverFaccao = QtWidgets.QPushButton(self.tab_10)
        self.buttonRemoverFaccao.setGeometry(QtCore.QRect(430, 50, 151, 25))
        self.buttonRemoverFaccao.setObjectName("buttonRemoverFaccao")
        self.panelLiderFaccao.addTab(self.tab_10, "")
        self.tabNaoLider = QtWidgets.QWidget()
        self.tabNaoLider.setObjectName("tabNaoLider")
        self.label_5 = QtWidgets.QLabel(self.tabNaoLider)
        self.label_5.setGeometry(QtCore.QRect(390, 50, 291, 31))
        self.label_5.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.panelLiderFaccao.addTab(self.tabNaoLider, "")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(30, 150, 201, 101))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonEstrelas = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonEstrelas.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.radioButtonEstrelas.setObjectName("radioButtonEstrelas")
        self.radioButtonPlanetas = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonPlanetas.setGeometry(QtCore.QRect(10, 50, 112, 23))
        self.radioButtonPlanetas.setObjectName("radioButtonPlanetas")
        self.radioButtonSistemas = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonSistemas.setGeometry(QtCore.QRect(10, 70, 112, 23))
        self.radioButtonSistemas.setObjectName("radioButtonSistemas")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setGeometry(QtCore.QRect(250, 150, 775, 480))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(720, 0, 301, 31))
        self.label_4.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 1021, 121))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.buttonInserirEstrela = QtWidgets.QPushButton(self.tab_21)
        self.buttonInserirEstrela.setGeometry(QtCore.QRect(920, 60, 89, 25))
        self.buttonInserirEstrela.setObjectName("buttonInserirEstrela")
        self.label_10 = QtWidgets.QLabel(self.tab_21)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.label_10.setObjectName("label_10")
        self.label_16 = QtWidgets.QLabel(self.tab_21)
        self.label_16.setGeometry(QtCore.QRect(20, 60, 151, 17))
        self.label_16.setObjectName("label_16")
        self.label_24 = QtWidgets.QLabel(self.tab_21)
        self.label_24.setGeometry(QtCore.QRect(330, 20, 91, 17))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_21)
        self.label_25.setGeometry(QtCore.QRect(330, 60, 51, 17))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_21)
        self.label_26.setGeometry(QtCore.QRect(580, 20, 111, 17))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_21)
        self.label_27.setGeometry(QtCore.QRect(580, 60, 111, 17))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_21)
        self.label_28.setGeometry(QtCore.QRect(810, 20, 111, 17))
        self.label_28.setObjectName("label_28")
        self.textIDEstrela = QtWidgets.QLineEdit(self.tab_21)
        self.textIDEstrela.setGeometry(QtCore.QRect(180, 10, 141, 31))
        self.textIDEstrela.setObjectName("textIDEstrela")
        self.textNomeEstrela = QtWidgets.QLineEdit(self.tab_21)
        self.textNomeEstrela.setGeometry(QtCore.QRect(180, 50, 141, 31))
        self.textNomeEstrela.setObjectName("textNomeEstrela")
        self.textClassificacaoEstrela = QtWidgets.QLineEdit(self.tab_21)
        self.textClassificacaoEstrela.setGeometry(QtCore.QRect(420, 10, 141, 31))
        self.textClassificacaoEstrela.setObjectName("textClassificacaoEstrela")
        self.textMassaEstrela = QtWidgets.QLineEdit(self.tab_21)
        self.textMassaEstrela.setGeometry(QtCore.QRect(420, 50, 141, 31))
        self.textMassaEstrela.setObjectName("textMassaEstrela")
        self.textCoordY = QtWidgets.QLineEdit(self.tab_21)
        self.textCoordY.setGeometry(QtCore.QRect(690, 50, 91, 31))
        self.textCoordY.setObjectName("textCoordY")
        self.textCoordX = QtWidgets.QLineEdit(self.tab_21)
        self.textCoordX.setGeometry(QtCore.QRect(690, 10, 91, 31))
        self.textCoordX.setObjectName("textCoordX")
        self.textCoordZ = QtWidgets.QLineEdit(self.tab_21)
        self.textCoordZ.setGeometry(QtCore.QRect(920, 10, 91, 31))
        self.textCoordZ.setObjectName("textCoordZ")
        self.tabWidget_2.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.label_11 = QtWidgets.QLabel(self.tab_22)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 171, 17))
        self.label_11.setObjectName("label_11")
        self.buttonPesquisarEstrela = QtWidgets.QPushButton(self.tab_22)
        self.buttonPesquisarEstrela.setGeometry(QtCore.QRect(920, 60, 89, 25))
        self.buttonPesquisarEstrela.setObjectName("buttonPesquisarEstrela")
        self.textPesquisarEstrela = QtWidgets.QLineEdit(self.tab_22)
        self.textPesquisarEstrela.setGeometry(QtCore.QRect(110, 10, 231, 31))
        self.textPesquisarEstrela.setObjectName("textPesquisarEstrela")
        self.label_19 = QtWidgets.QLabel(self.tab_22)
        self.label_19.setGeometry(QtCore.QRect(10, 60, 91, 17))
        self.label_19.setObjectName("label_19")
        self.textResultadoPesquisa = QtWidgets.QLabel(self.tab_22)
        self.textResultadoPesquisa.setGeometry(QtCore.QRect(100, 50, 561, 21))
        self.textResultadoPesquisa.setObjectName("textResultadoPesquisa")
        self.textResultadoPesquisa_2 = QtWidgets.QLabel(self.tab_22)
        self.textResultadoPesquisa_2.setGeometry(QtCore.QRect(100, 70, 561, 21))
        self.textResultadoPesquisa_2.setObjectName("textResultadoPesquisa_2")
        self.tabWidget_2.addTab(self.tab_22, "")
        self.tab_27 = QtWidgets.QWidget()
        self.tab_27.setObjectName("tab_27")
        self.label_29 = QtWidgets.QLabel(self.tab_27)
        self.label_29.setGeometry(QtCore.QRect(550, 20, 111, 17))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_27)
        self.label_30.setGeometry(QtCore.QRect(780, 20, 111, 17))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_27)
        self.label_31.setGeometry(QtCore.QRect(290, 60, 51, 17))
        self.label_31.setObjectName("label_31")
        self.buttonAtualizarEstrela = QtWidgets.QPushButton(self.tab_27)
        self.buttonAtualizarEstrela.setGeometry(QtCore.QRect(910, 60, 89, 25))
        self.buttonAtualizarEstrela.setObjectName("buttonAtualizarEstrela")
        self.label_32 = QtWidgets.QLabel(self.tab_27)
        self.label_32.setGeometry(QtCore.QRect(10, 20, 141, 17))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_27)
        self.label_33.setGeometry(QtCore.QRect(10, 60, 151, 17))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_27)
        self.label_34.setGeometry(QtCore.QRect(290, 20, 91, 17))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_27)
        self.label_35.setGeometry(QtCore.QRect(550, 60, 111, 17))
        self.label_35.setObjectName("label_35")
        self.textMassaEstrelaAtuailizar = QtWidgets.QLineEdit(self.tab_27)
        self.textMassaEstrelaAtuailizar.setGeometry(QtCore.QRect(390, 50, 141, 31))
        self.textMassaEstrelaAtuailizar.setObjectName("textMassaEstrelaAtuailizar")
        self.textCoordYAtuailizar = QtWidgets.QLineEdit(self.tab_27)
        self.textCoordYAtuailizar.setGeometry(QtCore.QRect(670, 50, 91, 31))
        self.textCoordYAtuailizar.setObjectName("textCoordYAtuailizar")
        self.textIDEstrelaAtualizar = QtWidgets.QLineEdit(self.tab_27)
        self.textIDEstrelaAtualizar.setGeometry(QtCore.QRect(130, 10, 141, 31))
        self.textIDEstrelaAtualizar.setObjectName("textIDEstrelaAtualizar")
        self.textNomeEstrelaAtualizar = QtWidgets.QLineEdit(self.tab_27)
        self.textNomeEstrelaAtualizar.setGeometry(QtCore.QRect(130, 50, 141, 31))
        self.textNomeEstrelaAtualizar.setObjectName("textNomeEstrelaAtualizar")
        self.textClassificacaoEstrelaAtualizar = QtWidgets.QLineEdit(self.tab_27)
        self.textClassificacaoEstrelaAtualizar.setGeometry(QtCore.QRect(390, 10, 141, 31))
        self.textClassificacaoEstrelaAtualizar.setObjectName("textClassificacaoEstrelaAtualizar")
        self.textCoordZAtuailizar = QtWidgets.QLineEdit(self.tab_27)
        self.textCoordZAtuailizar.setGeometry(QtCore.QRect(910, 10, 91, 31))
        self.textCoordZAtuailizar.setObjectName("textCoordZAtuailizar")
        self.textCoordXAtuailizar = QtWidgets.QLineEdit(self.tab_27)
        self.textCoordXAtuailizar.setGeometry(QtCore.QRect(670, 10, 91, 31))
        self.textCoordXAtuailizar.setObjectName("textCoordXAtuailizar")
        self.tabWidget_2.addTab(self.tab_27, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.label_17 = QtWidgets.QLabel(self.tab_23)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.label_17.setObjectName("label_17")
        self.plainTextEdit_18 = QtWidgets.QPlainTextEdit(self.tab_23)
        self.plainTextEdit_18.setGeometry(QtCore.QRect(200, 90, 261, 31))
        self.plainTextEdit_18.setObjectName("plainTextEdit_18")
        self.label_18 = QtWidgets.QLabel(self.tab_23)
        self.label_18.setGeometry(QtCore.QRect(10, 100, 181, 17))
        self.label_18.setObjectName("label_18")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_7.setGeometry(QtCore.QRect(920, 110, 89, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonExcluirEstrela = QtWidgets.QPushButton(self.tab_23)
        self.buttonExcluirEstrela.setGeometry(QtCore.QRect(920, 60, 89, 25))
        self.buttonExcluirEstrela.setObjectName("buttonExcluirEstrela")
        self.textExcluirEstrela = QtWidgets.QLineEdit(self.tab_23)
        self.textExcluirEstrela.setGeometry(QtCore.QRect(110, 10, 231, 31))
        self.textExcluirEstrela.setObjectName("textExcluirEstrela")
        self.tabWidget_2.addTab(self.tab_23, "")
        self.contador = QtWidgets.QLabel(self.tab_5)
        self.contador.setGeometry(QtCore.QRect(40, 260, 191, 31))
        self.contador.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.contador.setText("")
        self.contador.setObjectName("contador")
        self.oficialTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableRelatorio = QtWidgets.QTableWidget(self.tab_6)
        self.tableRelatorio.setGeometry(QtCore.QRect(10, 170, 1021, 591))
        self.tableRelatorio.setObjectName("tableRelatorio")
        self.tableRelatorio.setColumnCount(0)
        self.tableRelatorio.setRowCount(0)
        self.tabWidgetRelatorio = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidgetRelatorio.setGeometry(QtCore.QRect(10, 30, 1021, 121))
        self.tabWidgetRelatorio.setObjectName("tabWidgetRelatorio")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.buttonGerarCientista = QtWidgets.QPushButton(self.tab_24)
        self.buttonGerarCientista.setGeometry(QtCore.QRect(920, 50, 89, 25))
        self.buttonGerarCientista.setObjectName("buttonGerarCientista")
        self.label_7 = QtWidgets.QLabel(self.tab_24)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.label_7.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.textEstrelaCentral = QtWidgets.QLineEdit(self.tab_24)
        self.textEstrelaCentral.setGeometry(QtCore.QRect(170, 50, 141, 31))
        self.textEstrelaCentral.setObjectName("textEstrelaCentral")
        self.label_20 = QtWidgets.QLabel(self.tab_24)
        self.label_20.setGeometry(QtCore.QRect(20, 60, 141, 17))
        self.label_20.setObjectName("label_20")
        self.textDistanciaMinima = QtWidgets.QLineEdit(self.tab_24)
        self.textDistanciaMinima.setGeometry(QtCore.QRect(450, 50, 141, 31))
        self.textDistanciaMinima.setObjectName("textDistanciaMinima")
        self.label_21 = QtWidgets.QLabel(self.tab_24)
        self.label_21.setGeometry(QtCore.QRect(330, 60, 141, 17))
        self.label_21.setObjectName("label_21")
        self.textDistanciaMaxima = QtWidgets.QLineEdit(self.tab_24)
        self.textDistanciaMaxima.setGeometry(QtCore.QRect(740, 50, 141, 31))
        self.textDistanciaMaxima.setObjectName("textDistanciaMaxima")
        self.label_22 = QtWidgets.QLabel(self.tab_24)
        self.label_22.setGeometry(QtCore.QRect(610, 60, 121, 17))
        self.label_22.setObjectName("label_22")
        self.tabWidgetRelatorio.addTab(self.tab_24, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.buttonGerarLider = QtWidgets.QPushButton(self.tab_25)
        self.buttonGerarLider.setGeometry(QtCore.QRect(920, 50, 89, 25))
        self.buttonGerarLider.setObjectName("buttonGerarLider")
        self.radioButtonRelatorioEspecie = QtWidgets.QRadioButton(self.tab_25)
        self.radioButtonRelatorioEspecie.setGeometry(QtCore.QRect(210, 50, 71, 23))
        self.radioButtonRelatorioEspecie.setObjectName("radioButtonRelatorioEspecie")
        self.radioButtonRelatorioNacao = QtWidgets.QRadioButton(self.tab_25)
        self.radioButtonRelatorioNacao.setGeometry(QtCore.QRect(10, 50, 112, 23))
        self.radioButtonRelatorioNacao.setObjectName("radioButtonRelatorioNacao")
        self.label_6 = QtWidgets.QLabel(self.tab_25)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.label_6.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_6.setObjectName("label_6")
        self.radioButtonRelatorioPlaneta = QtWidgets.QRadioButton(self.tab_25)
        self.radioButtonRelatorioPlaneta.setGeometry(QtCore.QRect(420, 50, 71, 23))
        self.radioButtonRelatorioPlaneta.setObjectName("radioButtonRelatorioPlaneta")
        self.radioButtonRelatorioSistema = QtWidgets.QRadioButton(self.tab_25)
        self.radioButtonRelatorioSistema.setGeometry(QtCore.QRect(610, 50, 81, 23))
        self.radioButtonRelatorioSistema.setObjectName("radioButtonRelatorioSistema")
        self.tabWidgetRelatorio.addTab(self.tab_25, "")
        self.oficialTab.addTab(self.tab_6, "")

        self.retranslateUi(Form)
        self.oficialTab.setCurrentIndex(0)
        self.panelLiderFaccao.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidgetRelatorio.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CIENTISTA"))
        self.label.setText(_translate("Form", "Novo nome da Facção"))
        self.buttonAlterarNome.setText(_translate("Form", "ENVIAR"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tab_7), _translate("Form", "Alterar nome Facção"))
        self.label_3.setText(_translate("Form", "Novo CPI do Líder"))
        self.buttonNovoLider.setText(_translate("Form", "ENVIAR"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tab_8), _translate("Form", "Indicar novo líder"))
        self.label_12.setText(_translate("Form", "Nome da Comunidade"))
        self.label_13.setText(_translate("Form", "Especia da Comunidade"))
        self.label_14.setText(_translate("Form", "Quantidade de habitantes"))
        self.buttonCredenciarComunidade.setText(_translate("Form", "ENVIAR"))
        self.label_15.setText(_translate("Form", "Planeta que habita comunidade"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tab_9), _translate("Form", "Credenciar comunidades novas"))
        self.buttonRemoverFaccao.setText(_translate("Form", "REMOVER FACÇÃO"))
        self.panelLiderFaccao.setTabText(self.panelLiderFaccao.indexOf(self.tab_10), _translate("Form", "Remover Facção de Nacção"))
        self.label_5.setText(_translate("Form", "Voce não é líder de Facção"))
        self.groupBox.setTitle(_translate("Form", "Pesquisar"))
        self.radioButtonEstrelas.setText(_translate("Form", "Estrelas"))
        self.radioButtonPlanetas.setText(_translate("Form", "Planetas"))
        self.radioButtonSistemas.setText(_translate("Form", "Sistemas"))
        self.label_4.setText(_translate("Form", "Bem-vindo, USER"))
        self.buttonInserirEstrela.setText(_translate("Form", "ENVIAR"))
        self.label_10.setText(_translate("Form", "ID da nova estrela"))
        self.label_16.setText(_translate("Form", "Nome da nova estrela"))
        self.label_24.setText(_translate("Form", "Classificação"))
        self.label_25.setText(_translate("Form", "Massa"))
        self.label_26.setText(_translate("Form", "Coordenadas X"))
        self.label_27.setText(_translate("Form", "Coordenadas Y"))
        self.label_28.setText(_translate("Form", "Coordenadas Z"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_21), _translate("Form", "Inserir estrela"))
        self.label_11.setText(_translate("Form", "ID da estrela"))
        self.buttonPesquisarEstrela.setText(_translate("Form", "PESQUISAR"))
        self.label_19.setText(_translate("Form", "Resultado"))
        self.textResultadoPesquisa.setText(_translate("Form", "TextLabel"))
        self.textResultadoPesquisa_2.setText(_translate("Form", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_22), _translate("Form", "Pesquisar estrela"))
        self.label_29.setText(_translate("Form", "Coordenadas X"))
        self.label_30.setText(_translate("Form", "Coordenadas Z"))
        self.label_31.setText(_translate("Form", "Massa"))
        self.buttonAtualizarEstrela.setText(_translate("Form", "ENVIAR"))
        self.label_32.setText(_translate("Form", "ID da estrela"))
        self.label_33.setText(_translate("Form", "Nome da estrela"))
        self.label_34.setText(_translate("Form", "Classificação"))
        self.label_35.setText(_translate("Form", "Coordenadas Y"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_27), _translate("Form", "Atualizar estrela"))
        self.label_17.setText(_translate("Form", "ID da estrela"))
        self.label_18.setText(_translate("Form", "Quantidade de habitantes"))
        self.pushButton_7.setText(_translate("Form", "ENVIAR"))
        self.buttonExcluirEstrela.setText(_translate("Form", "EXCLUIR"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_23), _translate("Form", "Excluir estrela"))
        self.oficialTab.setTabText(self.oficialTab.indexOf(self.tab_5), _translate("Form", "NOME_DO_CARGO"))
        self.buttonGerarCientista.setText(_translate("Form", "GERAR"))
        self.label_7.setText(_translate("Form", "Gerar relatório seguindo:"))
        self.label_20.setText(_translate("Form", "ID da estrela central"))
        self.label_21.setText(_translate("Form", "Distância mínima"))
        self.label_22.setText(_translate("Form", "Distância máxima"))
        self.tabWidgetRelatorio.setTabText(self.tabWidgetRelatorio.indexOf(self.tab_24), _translate("Form", "Cientista"))
        self.buttonGerarLider.setText(_translate("Form", "GERAR"))
        self.radioButtonRelatorioEspecie.setText(_translate("Form", "Especie"))
        self.radioButtonRelatorioNacao.setText(_translate("Form", "Nação"))
        self.label_6.setText(_translate("Form", "Gerar relatório seguindo:"))
        self.radioButtonRelatorioPlaneta.setText(_translate("Form", "Planeta"))
        self.radioButtonRelatorioSistema.setText(_translate("Form", "Sistema"))
        self.tabWidgetRelatorio.setTabText(self.tabWidgetRelatorio.indexOf(self.tab_25), _translate("Form", "Lider de Facção"))
        self.oficialTab.setTabText(self.oficialTab.indexOf(self.tab_6), _translate("Form", "RELATÓRIOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
