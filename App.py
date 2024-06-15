# TODO : Secciones 
# TODO : Corregir quinta tabla del panel de lider de faccao
# TODO : Excepciones en credenciar
# TODO : 
import sys
import oracledb
import PyQt5.QtWidgets as qtw
from DataBaseConection import DataBaseConnection
from enum import Enum
from window import Window
from login.loginPage import Ui_Form as login
from overview_pages.cientista_page.cientistaPage import Ui_Form as cientista
from overview_pages.comandante_page.comandantePage import Ui_Form as comandante
from overview_pages.oficial_page.oficialPage import Ui_Form as oficial

class WindowsEnum(Enum):
    LOGIN = 0
    OFICIAL = 1
    CIENTISTA = 2
    COMANDANTE = 3

class App:
    def __init__(self):
        self.application = qtw.QApplication(sys.argv) 
        loginWindow = Window(login())
        cientistaWindow = Window(cientista())
        comandanteWindow = Window(comandante())
        oficialWindow = Window(oficial())
        self.usuario = "placeholder"
        self.VentanasIndex = WindowsEnum
        self.Ventanas = [loginWindow, oficialWindow, cientistaWindow, comandanteWindow]
        self.__inicializarLogin()
        
        
    def showWindow(self, ventana):        
        self.Ventanas[ventana].show()
        
    def stopApp(self):
        sys.exit(self.application.exec_())
        self.connection.close_connection()

    def startDataBaseConnection(self):
        self.connection = DataBaseConnection()
        self.connection.established_connection()
    
    def __inicializarLogin(self):
        self.Ventanas[self.VentanasIndex.LOGIN.value].ui.pushButton.clicked.connect(lambda: self.__verificarUsuario())

    def __inicializarOficial(self):
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.radioButtonFaccao.clicked.connect(lambda:self.query_filter("FACCAO", self.VentanasIndex.OFICIAL.value))
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.radioButtonLider.clicked.connect(lambda:self.query_filter("LIDER", self.VentanasIndex.OFICIAL.value))
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.radioButtonComunidade.clicked.connect(lambda:self.query_filter("COMUNIDADE", self.VentanasIndex.OFICIAL.value))
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.radioButtonNacao.clicked.connect(lambda:self.query_filter("NACAO", self.VentanasIndex.OFICIAL.value))
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.radioButtonHabitacao.clicked.connect(lambda:self.query_filter("HABITACAO",self.VentanasIndex.OFICIAL.value))
        self.Ventanas[self.VentanasIndex.OFICIAL.value].ui.label_4.setText(f"Bem-vindo, {self.usuario.NOME}")
        

    def __inicializarCientista(self):
        self.Ventanas[self.VentanasIndex.CIENTISTA.value].ui.radioButtonEstrelas.clicked.connect(lambda:self.query_filter("ESTRELA", self.VentanasIndex.CIENTISTA.value))
        self.Ventanas[self.VentanasIndex.CIENTISTA.value].ui.radioButtonPlanetas.clicked.connect(lambda:self.query_filter("PLANETA", self.VentanasIndex.CIENTISTA.value))
        self.Ventanas[self.VentanasIndex.CIENTISTA.value].ui.radioButtonSistemas.clicked.connect(lambda:self.query_filter("SISTEMA", self.VentanasIndex.CIENTISTA.value))
        self.Ventanas[self.VentanasIndex.CIENTISTA.value].ui.label_4.setText(f"Bem-vindo, {self.usuario.NOME}")

    def __inicializarComandante(self):
        self.Ventanas[self.VentanasIndex.COMANDANTE.value].ui.radioButtonPlaneta.clicked.connect(lambda:self.query_filter("PLANETA", self.VentanasIndex.COMANDANTE.value))
        self.Ventanas[self.VentanasIndex.COMANDANTE.value].ui.radioButtonNacao.clicked.connect(lambda:self.query_filter("NACAO", self.VentanasIndex.COMANDANTE.value))
        self.Ventanas[self.VentanasIndex.COMANDANTE.value].ui.radioButtonDominancia.clicked.connect(lambda:self.query_filter("DOMINANCIA", self.VentanasIndex.COMANDANTE.value))
        self.Ventanas[self.VentanasIndex.COMANDANTE.value].ui.label_4.setText(f"Bem-vindo, {self.usuario.NOME}")
        
    def __verificarUsuario(self):
        
        try:
            typeObject = self.connection.connection.gettype("LIDER_INFO")
            cursor = self.connection.connection.cursor()
            #result = cursor.callfunc("verificar_usuario", asd, [loginWindow.ui.CPI_text_box.text(), loginWindow.ui.senha_text_box.text()])

            # 111.222.393-44 OFICIAL
            # 123.456.789-00 COMANDANTE
            # 555.666.797-88 CIENTISTA

            """
            set serveroutput on;
            -- Actualización del líder de la facção
            BEGIN
                pacoteLiderf.actualizar_lider_por_cpi('333.444.555-66', '987.654.321-00');
            END;
            /

            -- Intento de actualización con un líder actual no existente
            BEGIN
                pacoteLiderf.actualizar_lider_por_cpi('000.000.000-00', '987.654.321-00');
            END;
            /

            -- Intento de actualización con un nuevo líder no existente
            BEGIN
                pacoteLiderf.actualizar_lider_por_cpi('222.333.444-55', '000.000.000-00');
            END;
            """

            self.usuario = cursor.callfunc("verificar_usuario", typeObject, ["555.444.393-22", "Papu+na"])
            
            self.Ventanas[self.VentanasIndex.LOGIN.value].close()

            if self.usuario.CARGO == "OFICIAL   ":
                self.__inicializarOficial()   
                self.Ventanas[self.VentanasIndex.OFICIAL.value].show()
                self.funcionalidadLiderFaccao(self.VentanasIndex.OFICIAL.value)
                if(self.usuario.EH_LIDER_FACCAO == 'N'):
                    self.hideIfNotLider(self.VentanasIndex.OFICIAL.value)
            
            if self.usuario.CARGO == "CIENTISTA ":
                self.__inicializarCientista()
                self.Ventanas[self.VentanasIndex.CIENTISTA.value].show()
                self.funcionalidadCientista(self.VentanasIndex.CIENTISTA.value)
                self.funcionalidadLiderFaccao(self.VentanasIndex.CIENTISTA.value)
                if(self.usuario.EH_LIDER_FACCAO == 'N'):
                    self.hideIfNotLider(self.VentanasIndex.CIENTISTA.value)

            if self.usuario.CARGO == "COMANDANTE":
                self.__inicializarComandante() 
                self.Ventanas[self.VentanasIndex.COMANDANTE.value].show()
                self.funcionalidadLiderFaccao(self.VentanasIndex.COMANDANTE.value)
                if(self.usuario.EH_LIDER_FACCAO == 'N'):
                    self.hideIfNotLider(self.VentanasIndex.COMANDANTE.value)

            #print(f'Login exitoso\nCPI: {self.usuario.CPI}\nNome: {self.usuario.NOME}\nCargo: {self.usuario.CARGO}\nNacao: {self.usuario.NACAO}\nEspecie: {self.usuario.ESPECIE}\nEh Lider Faccao: {self.usuario.EH_LIDER_FACCAO}')
        
        except oracledb.Error as e:
            errorObject,=e.args
            if errorObject.code == 20001:
                self.Ventanas[self.VentanasIndex.LOGIN].popupMessage("Usuário não encontrado.")
            if errorObject.code == 20002:
                self.Ventanas[self.VentanasIndex.LOGIN].popupMessage("Senha incorreta.")
            if errorObject.code == 20003:
                self.Ventanas[self.VentanasIndex.LOGIN].popupMessage("Líder não encontrado")
            if errorObject.code == 20004:
                self.Ventanas[self.VentanasIndex.LOGIN].popupMessage("Error desconocido: error code ORA-20004")  
        
# ---------------------------------
    
    def query_filter(self, nombre, currentWindow):
        
        cursor = self.connection.connection.cursor()
        consulta = "SELECT * FROM " + nombre

        cursor.execute(f"SELECT COUNT(*) FROM {nombre}")
        cantidad = cursor.fetchone()

        cursor.execute(consulta)
        if cantidad[0] < 1000:
            data = cursor.fetchall()
            self.Ventanas[currentWindow].ui.contador.setText(f"Há {cantidad[0]} tuplas na tabela.")
        else:
            data = cursor.fetchmany(1000)
            self.Ventanas[currentWindow].ui.contador.setText(f"Há {cantidad[0]} tuplas na tabela.")

        
        if data:
            self.Ventanas[currentWindow].ui.tableWidget.setRowCount(len(data))
            self.Ventanas[currentWindow].ui.tableWidget.setColumnCount(len(data[0]))

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.Ventanas[currentWindow].ui.tableWidget.setItem(row_idx, col_idx, qtw.QTableWidgetItem(str(col_data)))

        

# ---------------------------------

    def hideIfNotLider(self, currentWindow):
        
        for i in range(0,4):
            self.Ventanas[currentWindow].ui.panelLiderFaccao.setTabEnabled(i,False)
        
        self.Ventanas[currentWindow].ui.panelLiderFaccao.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")

    def funcionalidadLiderFaccao(self, currentWindow):
        
        # Alterar nome da faccao
        self.Ventanas[currentWindow].ui.buttonAlterarNome.clicked.connect(lambda: self.__alterarNome(currentWindow))

        # Novo lider
        self.Ventanas[currentWindow].ui.buttonNovoLider.clicked.connect(lambda: self.__novoLider(currentWindow))

        # Credenciar comunidade
        self.Ventanas[currentWindow].ui.buttonCredenciarComunidade.clicked.connect(lambda: self.__credenciarComunidade(currentWindow))

        # Remover Faccao de Naccao
        self.Ventanas[currentWindow].ui.buttonRemoverFaccao.clicked.connect(lambda: self.__removerFaccaoNaccao(currentWindow))
        

        
    def __alterarNome(self, currentWindow):
        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacoteLiderf.update_nome_faccao", [self.usuario.CPI, self.Ventanas[currentWindow].ui.textAlterarNome.text()])

        cursor.close()

    def __credenciarComunidade(self, currentWindow):
        especie = self.Ventanas[currentWindow].ui.textEspecieComunidade.text()
        comunidade = self.Ventanas[currentWindow].ui.textNomeComunidade.text()
        quantidade = int(self.Ventanas[currentWindow].ui.textQuantidadeComunidade.text())
        cpi = self.usuario.CPI
        planeta = self.Ventanas[currentWindow].ui.textPlanetaComunidade.text()

        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacoteLiderf.inserir_nova_comunidade", [especie, comunidade, quantidade, cpi, planeta])

        cursor.close()
    
    def __novoLider(self, currentWindow):
        
        # Creando cursor
        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacoteLiderf.actualizar_lider_por_cpi", [self.usuario.CPI, self.Ventanas[currentWindow].ui.textNovoLider.text()])

        # Creando ventana emergente
        self.Ventanas[currentWindow].popupMessage("Voce perdiou privilégios, voltando para o login.")

        # Volviendo a login
        self.Ventanas[currentWindow].close()
        self.Ventanas[self.VentanasIndex.LOGIN.value].show()
        
        # Cerrando cursor
        cursor.close()

    def __removerFaccaoNaccao(self, currentWindow):
        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacoteLiderf.remover_faccao_nacao", [self.usuario.CPI])
        
        self.Ventanas[currentWindow].popupMessage("Facção excluída com éxito.")
        cursor.close()
    

    def funcionalidadCientista(self, currentWindow):
        # Inserir estrela
        self.Ventanas[currentWindow].ui.buttonInserirEstrela.clicked.connect(lambda: self.__inserirEstrela(currentWindow))

        # Pesquisar estrela
        self.Ventanas[currentWindow].ui.buttonPesquisarEstrela.clicked.connect(lambda: self.__pesquisarEstrela(currentWindow))
        self.Ventanas[currentWindow].ui.textResultadoPesquisa.setText("")
        self.Ventanas[currentWindow].ui.textResultadoPesquisa_2.setText("")

        # Atualizar estrela
        self.Ventanas[currentWindow].ui.buttonAtualizarEstrela.clicked.connect(lambda: self.__atualizarEstrela(currentWindow))

        # Excluir estrela
        self.Ventanas[currentWindow].ui.buttonExcluirEstrela.clicked.connect(lambda: self.__excluirEstrela(currentWindow))

    def __inserirEstrela(self, currentWindow):
        idEstrela = self.Ventanas[currentWindow].ui.textIDEstrela.text()
        nomeEstrela = self.Ventanas[currentWindow].ui.textNomeEstrela.text()
        classificacaoEstrela = self.Ventanas[currentWindow].ui.textClassificacaoEstrela.text()
        massaEstrela = self.Ventanas[currentWindow].ui.textMassaEstrela.text()
        coordX = float(self.Ventanas[currentWindow].ui.textCoordX.text())
        coordY = float(self.Ventanas[currentWindow].ui.textCoordY.text())
        coordZ = float(self.Ventanas[currentWindow].ui.textCoordZ.text())

        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacote_cientista.criar_estrela", [idEstrela, nomeEstrela, classificacaoEstrela, massaEstrela, coordX, coordY, coordZ])
        
        self.Ventanas[currentWindow].popupMessage("Estrela inserida com sucesso.")
        cursor.close()

    def __pesquisarEstrela(self, currentWindow):
        cursor = self.connection.connection.cursor()
        
        nome = cursor.var(oracledb.STRING)
        classificacao = cursor.var(oracledb.STRING)
        massa = cursor.var(oracledb.NUMBER)
        x = cursor.var(oracledb.NUMBER)
        y = cursor.var(oracledb.NUMBER)
        z = cursor.var(oracledb.NUMBER)

        resultado = cursor.callproc("pacote_cientista.ler_estrela", [self.Ventanas[currentWindow].ui.textPesquisarEstrela.text(), nome, classificacao, massa, x, y, z])
        
        self.Ventanas[currentWindow].ui.textResultadoPesquisa.setText(f"Nombre: {nome.getvalue()}  Classificação: {classificacao.getvalue()}  Massa: {massa.getvalue()} ")

        self.Ventanas[currentWindow].ui.textResultadoPesquisa_2.setText(f"X: {x.getvalue()}  Y: {y.getvalue()}  Z: {z.getvalue()}")

    def __atualizarEstrela(self, currentWindow):
        idEstrela = self.Ventanas[currentWindow].ui.textIDEstrelaAtualizar.text()
        nomeEstrela = self.Ventanas[currentWindow].ui.textNomeEstrelaAtualizar.text()
        classificacaoEstrela = self.Ventanas[currentWindow].ui.textClassificacaoEstrelaAtualizar.text()
        massaEstrela = self.Ventanas[currentWindow].ui.textMassaEstrelaAtualizar.text()
        coordX = float(self.Ventanas[currentWindow].ui.textCoordXAtualizar.text())
        coordY = float(self.Ventanas[currentWindow].ui.textCoordYAtualizar.text())
        coordZ = float(self.Ventanas[currentWindow].ui.textCoordZAtualizar.text())

        cursor = self.connection.connection.cursor()
        resultado = cursor.callproc("pacote_cientista.actualizar_estrela", [idEstrela, nomeEstrela, classificacaoEstrela, massaEstrela, coordX, coordY, coordZ])
        
        self.Ventanas[currentWindow].popupMessage("Estrela atualizada com sucesso.")
        cursor.close()


    def __excluirEstrela(self, currentWindow):
        cursor = self.connection.connection.cursor()
        cursor.callproc("pacote_cientista.excluir_estrela", [self.Ventanas[currentWindow].ui.textExcluirEstrela.text()])
        
        self.Ventanas[currentWindow].popupMessage("Estrela excluida com sucesso.")
        cursor.close()
