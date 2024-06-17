# Excepciones

- ex_nombre_duplicado : 00001

555.444.393-22

try:
            pass    
        except oracledb.Error as e:
            errorObject,=e.args
            if errorObject.code == 1:
                currentWindow.popupMessage("°Nombre duplicado.")
