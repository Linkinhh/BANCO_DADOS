import oracledb
import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QApplication
from login.loginPage import Ui_Form as login

# Supongamos que la dirección IP del servidor es 123.456.789.10
ip_address = "143.107.183.216"
service_name = "pdb_elaine.icmc.usp.br"

# Creando el pool de sesiones con la dirección IP
pool = oracledb.SessionPool(user="a15390310", password="a15390310",
                            dsn=f"{ip_address}/{service_name}",
                            min=1, max=1, increment=1, encoding="UTF-8")

# Adquiriendo una conexión del pool
connection = pool.acquire()

print("Feita a conexão.")

app = QApplication(sys.argv)
window = qtw.QWidget()
ui = login()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())

# Liberando la conexión de vuelta al pool
pool.release(connection)

# Cerrando el pool de sesiones
pool.close()
