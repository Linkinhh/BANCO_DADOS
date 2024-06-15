import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class Window:

    def __init__(self, ui):
        
        self.ventana = qtw.QWidget()
        self.ui = ui
        self.ui.setupUi(self.ventana)

    def show(self):
        self.ventana.show()

    def close(self):
        self.ventana.close()
    
    def popupMessage(self, message, title="Notificação"):
        popup = qtw.QMessageBox() 
        popup.setWindowTitle(title)
        popup.setText(message)
        popup.exec()
