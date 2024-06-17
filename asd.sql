CREATE OR REPLACE PROCEDURE log_message(
    p_cpi IN LIDER.CPI%TYPE,
    p_message IN LOG_TABLE.MESSAGE%TYPE
) AS
    v_userid USERS.USERID%TYPE;
BEGIN
    -- Buscar el USERID correspondiente al CPI del líder
    SELECT USERID INTO v_userid
    FROM USERS
    WHERE IDLIDER = p_cpi;

    -- Insertar el log en la tabla LOG_TABLE
    INSERT INTO LOG_TABLE (USERID, TIMESTAMP, MESSAGE)
    VALUES (v_userid, CURRENT_TIMESTAMP, p_message);

    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No se encontró un usuario con el CPI proporcionado.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Ocurrió un error: ' || SQLERRM);
        ROLLBACK;
END;
/

BEGIN 
    log_message('444.555.696-77', 'Alterar Facção');
END;