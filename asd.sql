--Funcionalidades de Gerenciamento
/*1. Líder de facção:
a. Gerenciar aspectos da própria facção da qual é líder:
i. Alterar nome da facção*/

/*ii. Indicar novo líder (Dica: quando um novo líder assume a facção, o líder
anterior deve perder o acesso à funcionalidade)*/

/*iii. Credenciar comunidades novas (Participa), que habitem planetas
dominados por nações onde a facção está presente/credenciada*/

CREATE OR REPLACE PACKAGE pacoteLiderf AS
    -- Declaração de exceções personalizadas
    e_liderNaoEncontrado EXCEPTION;
    e_FaccaoNaoEncontrado EXCEPTION;
    -- Declaração do procedimento para remover facção de uma nação
    PROCEDURE remover_faccao_nacao(p_cpi LIDER.cpi%TYPE);
    -- Declaração da função para obter o nome da facção de um líder
    FUNCTION obter_faccao(p_cpi LIDER.cpi%TYPE) RETURN FACCAO.nome%TYPE;
    PROCEDURE update_nome_faccao(p_old_name FACCAO.nome%TYPE, p_new_name FACCAO.nome%TYPE);
    PROCEDURE actualizar_lider_por_cpi(p_cpi_lider_actual IN LIDER.CPI%TYPE,p_cpi_nuevo_lider IN LIDER.CPI%TYPE);
    PROCEDURE credenciar_comunidades_novas (p_cpi_lider IN LIDER.CPI%TYPE);
    PROCEDURE inserir_nova_comunidade (p_especie IN COMUNIDADE.ESPECIE%TYPE,p_nome_comunidade IN COMUNIDADE.NOME%TYPE,
    p_qtd_habitantes IN COMUNIDADE.QTD_HABITANTES%TYPE, p_cpi_lider IN LIDER.CPI%TYPE, p_planeta IN PLANETA.ID_ASTRO%TYPE);
END pacoteLiderf;
/
CREATE OR REPLACE PACKAGE BODY pacoteLiderf AS
    -- Variável para armazenar o nome da facção
    v_faccao FACCAO.nome%TYPE;
    -- Implementação da função obter_faccao
    FUNCTION obter_faccao(p_cpi LIDER.cpi%TYPE) RETURN FACCAO.nome%TYPE IS    
    BEGIN
        -- Seleciona o nome da facção onde o líder é igual ao p_cpi fornecido
        SELECT nome INTO v_faccao FROM FACCAO WHERE lider = p_cpi;
        -- Se nenhum dado for encontrado, levanta a exceção e_liderNaoEncontrado
        IF SQL%NOTFOUND THEN RAISE e_liderNaoEncontrado;
        END IF;
        -- Retorna o nome da facção
    RETURN v_faccao;
    END obter_faccao;
    ---------------------------------------------------------------------------------
     -- Implementação do procedimento remover_faccao_nacao
    PROCEDURE remover_faccao_nacao(p_cpi LIDER.cpi%TYPE) AS
        BEGIN
            -- Obtém o nome da facção utilizando a função obter_faccao
            v_faccao := obter_faccao(p_cpi);
            -- Remove da tabela NACAO_FACCAO onde a facção é igual a v_faccao
            DELETE FROM NACAO_FACCAO WHERE faccao = v_faccao;
            -- Se nenhum dado for encontrado, levanta a exceção e_FaccaoNaoEncontrado
            IF SQL%NOTFOUND THEN RAISE e_FaccaoNaoEncontrado;
            END IF;
        END remover_faccao_nacao;
    ------------------------------------------------------------------------------------------------------
    PROCEDURE update_nome_faccao(p_old_name FACCAO.nome%TYPE, p_new_name FACCAO.nome%TYPE) IS
        -- Definición de excepciones personalizadas
        ex_nombre_no_encontrado EXCEPTION;
        ex_nombre_duplicado EXCEPTION;
        PRAGMA EXCEPTION_INIT(ex_nombre_duplicado, -00001); -- Unique Constraint Violated
    BEGIN
      -- Desactivar las restricciones de clave externa
      EXECUTE IMMEDIATE 'ALTER TABLE NACAO_FACCAO DISABLE CONSTRAINT FK_NF_FACCAO';
      EXECUTE IMMEDIATE 'ALTER TABLE PARTICIPA DISABLE CONSTRAINT FK_PARTICIPA_FACCAO';
    
      -- Actualizar el nombre en la tabla FACCAO
      EXECUTE IMMEDIATE 'UPDATE FACCAO SET NOME = :1 WHERE NOME = :2'
      USING p_new_name, p_old_name;    
     
      -- Actualizar el nombre en la tabla NACAO_FACCAO
      EXECUTE IMMEDIATE 'UPDATE NACAO_FACCAO SET FACCAO = :1 WHERE FACCAO = :2'
      USING p_new_name, p_old_name;
      
      EXECUTE IMMEDIATE 'UPDATE PARTICIPA SET FACCAO = :1 WHERE FACCAO = :2'
      USING p_new_name, p_old_name;
    
      -- Reactivar las restricciones de clave externa
      EXECUTE IMMEDIATE 'ALTER TABLE NACAO_FACCAO ENABLE CONSTRAINT FK_NF_FACCAO';
      EXECUTE IMMEDIATE 'ALTER TABLE PARTICIPA ENABLE CONSTRAINT FK_PARTICIPA_FACCAO';
    
    EXCEPTION
      WHEN ex_nombre_duplicado THEN
        -- Manejo de la excepción cuando se intenta insertar un nombre duplicado
        DBMS_OUTPUT.PUT_LINE('Error: El nuevo nombre ya existe en la tabla FACCAO.');
        ROLLBACK;
      WHEN OTHERS THEN
        -- Manejo de otras excepciones no previstas
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        ROLLBACK;
        -- Reactivar las restricciones en caso de cualquier error
        EXECUTE IMMEDIATE 'ALTER TABLE NACAO_FACCAO ENABLE CONSTRAINT FK_NF_FACCAO';
    END update_nome_faccao;
    -----------------------------------------------------------------------------------------------------------------
    PROCEDURE actualizar_lider_por_cpi (p_cpi_lider_actual IN LIDER.CPI%TYPE, p_cpi_nuevo_lider IN LIDER.CPI%TYPE) IS
        -- Excepciones personalizadas
        ex_lider_no_existe EXCEPTION;
        ex_faccao_no_existe EXCEPTION;
    
        -- Variable para almacenar el nombre de la facção y verificar la existencia
        v_nome_faccao FACCAO.NOME%TYPE;
        v_count INTEGER;
    BEGIN
        -- Verificar si el líder actual existe en la tabla LIDER
        SELECT COUNT(*) INTO v_count FROM LIDER WHERE CPI = p_cpi_lider_actual;
        IF v_count = 0 THEN
            RAISE ex_lider_no_existe;
        END IF;
    
        -- Verificar si el nuevo líder existe en la tabla LIDER
        SELECT COUNT(*) INTO v_count FROM LIDER WHERE CPI = p_cpi_nuevo_lider;
        IF v_count = 0 THEN
            RAISE ex_lider_no_existe;
        END IF;
    
        -- Buscar la facção asociada al líder actual
        SELECT NOME INTO v_nome_faccao
        FROM FACCAO
        WHERE LIDER = p_cpi_lider_actual;
    
        -- Actualizar el líder de la facção
        UPDATE FACCAO
        SET LIDER = p_cpi_nuevo_lider
        WHERE NOME = v_nome_faccao;
    
        -- Confirmar la transacción
        COMMIT;
    EXCEPTION
        WHEN ex_lider_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El líder especificado no existe.');
        WHEN NO_DATA_FOUND THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: No se encontró una facção asociada al líder especificado.');
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
    END actualizar_lider_por_cpi;
    -----------------------------------------------------------------------------------------------
    PROCEDURE credenciar_comunidades_novas (p_cpi_lider IN LIDER.CPI%TYPE) IS
        -- Excepciones personalizadas
        ex_lider_no_existe EXCEPTION;
        ex_comunidade_no_encontrada EXCEPTION;
    
        -- Variables para almacenar datos
        v_faccao FACCAO.NOME%TYPE;
        v_especie COMUNIDADE.ESPECIE%TYPE;
        v_comunidade COMUNIDADE.NOME%TYPE;
        v_planeta PLANETA.ID_ASTRO%TYPE;
        
        -- Cursor para seleccionar las comunidades que cumplen con los criterios
        CURSOR c_comunidades IS SELECT DISTINCT C.ESPECIE, C.NOME, H.PLANETA FROM LIDER L
            JOIN FACCAO F ON L.CPI = F.LIDER
            JOIN NACAO_FACCAO NF ON F.NOME = NF.FACCAO
            JOIN DOMINANCIA D ON NF.NACAO = D.NACAO
            JOIN HABITACAO H ON D.PLANETA = H.PLANETA
            JOIN COMUNIDADE C ON H.ESPECIE = C.ESPECIE AND H.COMUNIDADE = C.NOME
            WHERE L.CPI = p_cpi_lider AND D.DATA_FIM IS NULL AND (H.DATA_FIM IS NULL OR H.DATA_FIM > SYSDATE)
            AND NOT EXISTS (SELECT 1 FROM PARTICIPA P WHERE P.FACCAO = F.NOME AND P.ESPECIE = C.ESPECIE AND P.COMUNIDADE = C.NOME);
    
    BEGIN
        -- Verificar si el líder existe
        SELECT COUNT(*) INTO v_faccao FROM LIDER WHERE CPI = p_cpi_lider;
        IF v_faccao = 0 THEN
            RAISE ex_lider_no_existe;
        END IF;
    
        -- Obtener la facção del líder
        SELECT F.NOME INTO v_faccao FROM LIDER L JOIN FACCAO F ON L.CPI = F.LIDER WHERE L.CPI = p_cpi_lider;
    
        -- Procesar cada comunidad del cursor
        FOR rec IN c_comunidades LOOP
            -- Insertar la comunidad en la tabla PARTICIPA
            INSERT INTO PARTICIPA (FACCAO, ESPECIE, COMUNIDADE) VALUES (v_faccao, rec.ESPECIE, rec.NOME);
        END LOOP;
    
        -- Confirmar la transacción
        COMMIT;
    
    EXCEPTION
        WHEN ex_lider_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El líder especificado no existe.');
        WHEN ex_comunidade_no_encontrada THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: No se encontraron comunidades para credenciar.');
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
    END credenciar_comunidades_novas;
    --------------------------------------------------------------------------------------------------
    PROCEDURE inserir_nova_comunidade (p_especie IN COMUNIDADE.ESPECIE%TYPE, p_nome_comunidade IN COMUNIDADE.NOME%TYPE,
    p_qtd_habitantes IN COMUNIDADE.QTD_HABITANTES%TYPE, p_cpi_lider IN LIDER.CPI%TYPE, p_planeta IN PLANETA.ID_ASTRO%TYPE) IS
        -- Excepciones personalizadas
        ex_lider_no_existe EXCEPTION;
        ex_planeta_no_existe EXCEPTION;
        ex_comunidade_existente EXCEPTION;
        ex_nacao_nao_dominante EXCEPTION;
    
        -- Variables para almacenar datos
        v_faccao FACCAO.NOME%TYPE;
        v_nacao NACAO.NOME%TYPE;
        v_exists INTEGER;
    BEGIN
        -- Verificar si el líder existe
        SELECT COUNT(*) INTO v_exists FROM LIDER WHERE CPI = p_cpi_lider;
        IF v_exists = 0 THEN
            RAISE ex_lider_no_existe;
        END IF;
    
        -- Verificar si el planeta existe
        SELECT COUNT(*) INTO v_exists FROM PLANETA WHERE ID_ASTRO = p_planeta;
        IF v_exists = 0 THEN
            RAISE ex_planeta_no_existe;
        END IF;
    
        -- Verificar si la comunidad ya existe
        SELECT COUNT(*) INTO v_exists FROM COMUNIDADE WHERE ESPECIE = p_especie AND NOME = p_nome_comunidade;
        IF v_exists > 0 THEN
            RAISE ex_comunidade_existente;
        END IF;
    
        -- Obtener la facção del líder
        SELECT F.NOME INTO v_faccao
        FROM LIDER L
        JOIN FACCAO F ON L.CPI = F.LIDER
        WHERE L.CPI = p_cpi_lider;
    
        -- Verificar si el planeta está dominado por una nación que pertenece a la facción del líder
        SELECT COUNT(*)
        INTO v_exists
        FROM DOMINANCIA D
        JOIN NACAO N ON D.NACAO = N.NOME
        JOIN NACAO_FACCAO NF ON N.NOME = NF.NACAO
        WHERE D.PLANETA = p_planeta
          AND NF.FACCAO = v_faccao
          AND D.DATA_FIM IS NULL;
    
        IF v_exists = 0 THEN
            RAISE ex_nacao_nao_dominante;
        END IF;
    
        -- Insertar nueva comunidad
        INSERT INTO COMUNIDADE (ESPECIE, NOME, QTD_HABITANTES)
        VALUES (p_especie, p_nome_comunidade, p_qtd_habitantes);
    
        -- Insertar nueva habitacão
        INSERT INTO HABITACAO (PLANETA, ESPECIE, COMUNIDADE, DATA_INI, DATA_FIM)
        VALUES (p_planeta, p_especie, p_nome_comunidade, SYSDATE, NULL);
    
        -- Llamar al procedimiento para credenciar comunidades por líder
        credenciar_comunidades_novas(p_cpi_lider);
    
        -- Confirmar la transacción
        COMMIT;
    
    EXCEPTION
        WHEN ex_lider_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El líder especificado no existe.');
        WHEN ex_planeta_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El planeta especificado no existe.');
        WHEN ex_comunidade_existente THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: La comunidad especificada ya existe.');
        WHEN ex_nacao_nao_dominante THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El planeta especificado no está dominado por una nación que pertenece a la facción del líder.');
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
    END inserir_nova_comunidade;
END pacoteLiderf;

set serveroutput on;
DECLARE
v_new_nome FACCAO.nome%TYPE;
v_old_nome FACCAO.nome%TYPE;
BEGIN
    v_old_nome := 'CallaGil';
    v_new_nome := 'Faccao1';
    pacoteLiderf.update_nome_faccao(v_old_nome,v_new_nome);
    dbms_output.put_line('nome de faccao atualizado!');    
END;


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
/
BEGIN
    pacoteLiderf.inserir_nova_comunidade('Especie1', 'Comunidade3', 500, '123.456.789-00', 'Planeta1');
END;

/*3. Comandante:
a. Pode alterar aspectos da própria nação:
i. Incluir/excluir a própria nação de uma federação existente
ii. Criar nova federação, com a própria nação
b. Insere nova dominância de um planeta que não está sendo dominado por ninguém*/

CREATE OR REPLACE PACKAGE pacote_comandante IS
  PROCEDURE criar_federacao(p_federacao_nome IN VARCHAR2, p_lider_cpi IN CHAR);
  
  PROCEDURE modificar_federacao_nacao(p_cpi_lider IN LIDER.CPI%TYPE,
    p_nome_federacao IN FEDERACAO.NOME%TYPE, p_operacao IN VARCHAR2);  -- 'INCLUIR' o 'EXCLUIR'

  PROCEDURE insertar_dominancia(p_cpi_lider IN LIDER.CPI%TYPE, p_planeta IN PLANETA.ID_ASTRO%TYPE,
    p_data_ini IN DATE, p_data_fim IN DATE);
END pacote_comandante;
/
CREATE OR REPLACE PACKAGE BODY pacote_comandante IS

  PROCEDURE criar_federacao(
    p_federacao_nome IN VARCHAR2,
    p_lider_cpi IN CHAR
  ) IS
    v_nacao_nome NACAO.NOME%TYPE;
    e_federacao_ja_existe EXCEPTION;
    e_lider_nao_encontrado EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_federacao_ja_existe, -00001);
  BEGIN
    -- Obter a nação do líder
    SELECT NACAO INTO v_nacao_nome FROM LIDER
                        WHERE CPI = p_lider_cpi AND CARGO = 'COMANDANTE';
    
    -- Verificar se encontrou o líder
    IF SQL%NOTFOUND THEN
      RAISE e_lider_nao_encontrado;
    END IF;
    
    -- Inserir nova federação
    INSERT INTO FEDERACAO (NOME, DATA_FUND)
    VALUES (p_federacao_nome, SYSDATE);
    
    -- Associar a nação à nova federação
    UPDATE NACAO
    SET FEDERACAO = p_federacao_nome
    WHERE NOME = v_nacao_nome;
    
    -- Verificar se a nação foi atualizada
    IF SQL%ROWCOUNT = 0 THEN
      RAISE_APPLICATION_ERROR(-20001, 'Nação não encontrada.');
    END IF;

    DBMS_OUTPUT.PUT_LINE('Federação ' || p_federacao_nome || ' criada com sucesso e associada à nação ' || v_nacao_nome);

  EXCEPTION
    WHEN e_lider_nao_encontrado THEN
      DBMS_OUTPUT.PUT_LINE('Erro: Líder não encontrado ou não é Comandante.');
    WHEN e_federacao_ja_existe THEN
      DBMS_OUTPUT.PUT_LINE('Erro: Federação já existe.');
    WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('Erro ao criar federação: ' || SQLERRM);
  END criar_federacao;
  
  PROCEDURE modificar_federacao_nacao(p_cpi_lider IN LIDER.CPI%TYPE,
    p_nome_federacao IN FEDERACAO.NOME%TYPE, p_operacao IN VARCHAR2) IS -- 'INCLUIR' o 'EXCLUIR'
        -- Excepciones personalizadas
        ex_lider_no_existe EXCEPTION;
        ex_federacao_no_existe EXCEPTION;
        ex_operacao_invalida EXCEPTION;
    
        -- Variables para almacenar datos
        v_nacao NACAO.NOME%TYPE;
        v_exists NUMBER;
    BEGIN
        -- Verificar si el líder existe y obtener la nación
        BEGIN
            SELECT NACAO INTO v_nacao FROM LIDER WHERE CPI = p_cpi_lider;
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                RAISE ex_lider_no_existe;
        END;
    
        -- Verificar si la federación existe
        IF p_operacao = 'INCLUIR' THEN
            SELECT COUNT(*) INTO v_exists FROM FEDERACAO WHERE NOME = p_nome_federacao;
            IF v_exists = 0 THEN
                RAISE ex_federacao_no_existe;
            END IF;
        END IF;
    
        -- Realizar la operación solicitada
        IF p_operacao = 'INCLUIR' THEN
            UPDATE NACAO SET FEDERACAO = p_nome_federacao WHERE NOME = v_nacao;
        ELSIF p_operacao = 'EXCLUIR' THEN
            UPDATE NACAO SET FEDERACAO = NULL WHERE NOME = v_nacao;
        ELSE
            RAISE ex_operacao_invalida;
        END IF;
    
        -- Confirmar la transacción
        COMMIT;
    
    EXCEPTION
        WHEN ex_lider_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El líder especificado no existe.');
        WHEN ex_federacao_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: La federación especificada no existe.');
        WHEN ex_operacao_invalida THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: Operación inválida. Use "INCLUIR" o "EXCLUIR".');
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
    END modificar_federacao_nacao;
    
    -----------------------------------------------------------------------------------------
    PROCEDURE insertar_dominancia (p_cpi_lider IN LIDER.CPI%TYPE, p_planeta IN PLANETA.ID_ASTRO%TYPE,
        p_data_ini IN DATE, p_data_fim IN DATE) IS
        -- Excepciones personalizadas
        ex_lider_no_existe EXCEPTION;
        ex_planeta_dominado EXCEPTION;
        ex_fecha_invalida EXCEPTION;
    
        -- Variables para almacenar datos
        v_nacao NACAO.NOME%TYPE;
        v_count NUMBER;
    BEGIN
        -- Verificar si el líder existe y obtener la nación
        BEGIN
            SELECT NACAO INTO v_nacao FROM LIDER WHERE CPI = p_cpi_lider;
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                RAISE ex_lider_no_existe;
        END;
    
        -- Verificar si el planeta ya está siendo dominado
        SELECT COUNT(*) INTO v_count FROM DOMINANCIA WHERE PLANETA = p_planeta 
          AND (DATA_FIM IS NULL OR DATA_FIM > SYSDATE);
    
        IF v_count > 0 THEN
            RAISE ex_planeta_dominado;
        END IF;
    
        -- Verificar la validez de las fechas
        IF p_data_fim IS NOT NULL AND p_data_fim <= p_data_ini THEN
            RAISE ex_fecha_invalida;
        END IF;
    
        -- Insertar nueva dominancia
        INSERT INTO DOMINANCIA (PLANETA, NACAO, DATA_INI, DATA_FIM)
        VALUES (p_planeta, v_nacao, p_data_ini, p_data_fim);
    
        -- Confirmar la transacción
        COMMIT;
    
    EXCEPTION
        WHEN ex_lider_no_existe THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El líder especificado no existe.');
        WHEN ex_planeta_dominado THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: El planeta ya está siendo dominado por otra nación.');
        WHEN ex_fecha_invalida THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: La fecha de fin debe ser mayor que la fecha de inicio.');
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
    END insertar_dominancia;
END pacote_comandante;

SELECT * FROM NACAO N, LIDER L WHERE N.nome = L.nacao AND L.cpi = '123.456.789-00';

-- Llamar al procedimiento para incluir una nación en una federación
BEGIN
    pacote_comandante.modificar_federacao_nacao('123.456.789-00', 'Non cum cum.', 'INCLUIR');
END;
/

-- Llamar al procedimiento para excluir una nación de una federación
BEGIN
    pacote_comandante.modificar_federacao_nacao('123.456.789-00', NULL, 'EXCLUIR');
END;
/

SELECT * FROM NACAO N, LIDER L WHERE N.nome = L.nacao AND L.cpi = '123.456.789-00';

--------

-- Llamar al procedimiento para insertar una nueva dominancia
BEGIN
    pacote_comandante.insertar_dominancia('222.333.444-55', 'Fugit non.', TO_DATE('2024-06-13', 'YYYY-MM-DD'), NULL);
END;
/

-- Intentar insertar una nueva dominancia en el mismo planeta (debería fallar)
BEGIN
    pacote_comandante.insertar_dominancia('222.333.444-55', 'Fugit non.', TO_DATE('2024-06-14', 'YYYY-MM-DD'), NULL);
END;
/
/*4. Cientista:
a. Gerenciar (CRUD) estrelas*/

CREATE OR REPLACE PACKAGE pacote_cientista IS
    -- PROCEDURE para criar estrelas, todos os parametros são de entrada
    PROCEDURE criar_estrela(p_id_estrela IN VARCHAR2, p_nome IN VARCHAR2, p_classificaccao IN VARCHAR2,
        p_massa IN NUMBER, p_x IN NUMBER, p_y IN NUMBER, p_z IN NUMBER);
    
    -- PROCEDURE para ler estrelas, só o parametro p_id_estrela é de entrada para
    -- pesquisar pela estrela e imprimir toda a informação relacionada a ela.
    PROCEDURE ler_estrela(p_id_estrela IN VARCHAR2, p_nome OUT VARCHAR2, p_classificaccao OUT VARCHAR2,
        p_massa OUT NUMBER, p_x OUT NUMBER, p_y OUT NUMBER, p_z OUT NUMBER);
    
    -- PROCEDURE para atualizar estrela, todos os parámetros são de entrada
    PROCEDURE actualizar_estrela(p_id_estrela IN VARCHAR2, p_nome IN VARCHAR2, p_classificaccao IN VARCHAR2,
        p_massa IN NUMBER, p_x IN NUMBER, p_y IN NUMBER, p_z IN NUMBER);
    
    -- PROCEDURE para excluir estrela pelo sua ID.
    PROCEDURE excluir_estrela(p_id_estrela IN VARCHAR2);

END pacote_cientista;
/
CREATE OR REPLACE PACKAGE BODY pacote_cientista IS

    -- PROCEDURE para criar estrelas, todos os parametros são de entrada
    PROCEDURE criar_estrela(p_id_estrela IN VARCHAR2, p_nome IN VARCHAR2, p_classificaccao IN VARCHAR2,
        p_massa IN NUMBER, p_x IN NUMBER, p_y IN NUMBER, p_z IN NUMBER) IS
        ex_estrela_existente EXCEPTION;
        ex_violacao_de_integridade EXCEPTION;
        PRAGMA EXCEPTION_INIT(ex_violacao_de_integridade, -2291); -- Violación de integridad referencial
    BEGIN 
        INSERT INTO ESTRELA (ID_ESTRELA, NOME, CLASSIFICACAO, MASSA, X, Y, Z)
        VALUES (p_id_estrela, p_nome, p_classificaccao, p_massa, p_x, p_y, p_z);
    EXCEPTION
        WHEN DUP_VAL_ON_INDEX THEN
            RAISE ex_estrela_existente;
        WHEN ex_violacao_de_integridade THEN
            DBMS_OUTPUT.PUT_LINE('Erro: Violação de integridade referencial.');
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Erro: ' || SQLERRM);
    END;

    PROCEDURE ler_estrela(p_id_estrela IN VARCHAR2, p_nome OUT VARCHAR2, p_classificaccao OUT VARCHAR2,
        p_massa OUT NUMBER, p_x OUT NUMBER, p_y OUT NUMBER, p_z OUT NUMBER) IS
        ex_estrela_nao_encontrada EXCEPTION;
    BEGIN
        SELECT NOME, CLASSIFICACAO, MASSA, X, Y, Z INTO p_nome, p_classificaccao, p_massa, p_x, p_y, p_z
        FROM ESTRELA WHERE ID_ESTRELA = p_id_estrela;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE ex_estrela_nao_encontrada;
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Erro: ' || SQLERRM);
    END;

    PROCEDURE actualizar_estrela(p_id_estrela IN VARCHAR2, p_nome IN VARCHAR2, p_classificaccao IN VARCHAR2,
        p_massa IN NUMBER, p_x IN NUMBER, p_y IN NUMBER, p_z IN NUMBER) IS
        ex_estrela_nao_encontrada EXCEPTION;
    BEGIN
        UPDATE ESTRELA SET NOME = p_nome, CLASSIFICACAO = p_classificaccao, MASSA = p_massa, X = p_x, Y = p_y, Z = p_z
        WHERE ID_ESTRELA = p_id_estrela;

        IF SQL%ROWCOUNT = 0 THEN
            RAISE ex_estrela_nao_encontrada;
        END IF;
    EXCEPTION
        WHEN ex_estrela_nao_encontrada THEN
            DBMS_OUTPUT.PUT_LINE('Erro: Estrela não encontrada.');
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Erro: ' || SQLERRM);
    END;

    PROCEDURE excluir_estrela(p_id_estrela IN VARCHAR2) IS
        ex_estrela_nao_encontrada EXCEPTION;
    BEGIN
        DELETE FROM ESTRELA WHERE ID_ESTRELA = p_id_estrela;

        IF SQL%ROWCOUNT = 0 THEN
            RAISE ex_estrela_nao_encontrada;
        END IF;
    EXCEPTION
        WHEN ex_estrela_nao_encontrada THEN
            DBMS_OUTPUT.PUT_LINE('Erro: Estrela não encontrada.');
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Erro: ' || SQLERRM);
    END;

END pacote_cientista;
/
