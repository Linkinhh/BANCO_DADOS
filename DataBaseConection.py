import oracledb

class DataBaseConnection:
    def __init__(self):
        self.ip_address = "143.107.183.216" 
        self.service_name = "pdb_elaine.icmc.usp.br"
        self.user = "a15390310"
        self.password = "a15390310"
        # Creando el pool de sesiones con la dirección IP
    
    def established_connection(self):
        try:
            self.pool = oracledb.SessionPool(user="a15390310", password="a15390310",
                                        dsn=f"{self.ip_address}/{self.service_name}",
                                        min=1, max=1, increment=1, encoding="UTF-8")
            
            # Adquiriendo una conexión del pool
            self.connection = self.pool.acquire()
            print("Conexão exitosa")

        except oracledb.DatabaseError as e:
            error, = e.args
            print("Error al conectar a la base de datos:", error.code)
            print(error.message)

    def close_connection(self):
        # Liberando la conexión de vuelta al pool
        self.pool.release(self.connection)

        # Cerrando el pool de sesiones
        self.pool.close()