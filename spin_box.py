import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VENTANA")

        self.setLayout(qtw.QVBoxLayout())
        """
        layout1 = qtw.QVBoxLayout()

        other = qtw.QPushButton(
            "XD"
        )
        layout1.layout().addWidget(other)
        """

        # label

        my_label = qtw.QLabel("Pick something from the box!")
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)
        #self.addChildLayout(layout1)
        
        # spin box

        my_spin = qtw.QSpinBox(
            self,
            value=2,
            maximum=100,
            minimum=0,
            singleStep=2,
            prefix = 'Hay ',
            suffix= ' naranjas'
        )

        my_spin.setFont(qtg.QFont("Helvetica", 24))


        # Put spinbox on screen
        self.layout().addWidget(my_spin)
        
        # button
        my_button = qtw.QPushButton("PRESS ME!", clicked= lambda:press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f'You picked {my_spin.value()}')
        

        my_box_text = qtw.QTextEdit(self,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Hello",
            readOnly=False,
            
        )
            

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()