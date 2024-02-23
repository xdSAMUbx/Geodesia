import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class VentanaAngulos(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Primera fila de cuadros de entrada, etiquetas y botón circular
        self.texto1 = QLabel('Texto 1:')
        self.edit_grados1 = QLineEdit()
        self.lbl_grados1 = QLabel('º')
        self.edit_minutos1 = QLineEdit()
        self.lbl_minutos1 = QLabel('\'')
        self.edit_segundos1 = QLineEdit()
        self.lbl_segundos1 = QLabel('\'\'')
        self.btn_interruptor1 = QPushButton('2D')
        self.btn_interruptor1.setCheckable(True)
        self.btn_interruptor1.clicked.connect(lambda: self.habilitar_deshabilitar(1))

        # Segunda fila de cuadros de entrada, etiquetas y botón circular
        self.texto2 = QLabel('Texto 2:')
        self.edit_grados2 = QLineEdit()
        self.lbl_grados2 = QLabel('º')
        self.edit_minutos2 = QLineEdit()
        self.lbl_minutos2 = QLabel('\'')
        self.edit_segundos2 = QLineEdit()
        self.lbl_segundos2 = QLabel('\'\'')
        self.btn_interruptor2 = QPushButton('3D')
        self.btn_interruptor2.setCheckable(True)
        self.btn_interruptor2.clicked.connect(lambda: self.habilitar_deshabilitar(2))

        #Espacio para escribir la altura
        self.altura = QLineEdit()

        # Botón para imprimir los valores ingresados
        btn_mostrar = QPushButton('CALCULAR')
        btn_mostrar.clicked.connect(self.mostrar_valores)

        # Diseño de la interfaz utilizando un diseño vertical
        vbox = QVBoxLayout()

        # Primera fila
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.texto1)
        hbox1.addWidget(self.edit_grados1)
        hbox1.addWidget(self.lbl_grados1)
        hbox1.addWidget(self.edit_minutos1)
        hbox1.addWidget(self.lbl_minutos1)
        hbox1.addWidget(self.edit_segundos1)
        hbox1.addWidget(self.lbl_segundos1)
        hbox1.addWidget(self.btn_interruptor1)

        # Segunda fila
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.texto2)
        hbox2.addWidget(self.edit_grados2)
        hbox2.addWidget(self.lbl_grados2)
        hbox2.addWidget(self.edit_minutos2)
        hbox2.addWidget(self.lbl_minutos2)
        hbox2.addWidget(self.edit_segundos2)
        hbox2.addWidget(self.lbl_segundos2)
        hbox2.addWidget(self.btn_interruptor2)

        # Nuevo QHBoxLayout para el recuadro blanco con texto
        hbox3 = QHBoxLayout()
        label_izquierda = QLabel('Altura: ')
        label_derecha = QLabel('m')
        hbox3.addWidget(label_izquierda)
        hbox3.addWidget(self.altura) 
        hbox3.addWidget(label_derecha)

        # Agregar filas y botón al diseño vertical
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(btn_mostrar)

        self.setLayout(vbox)

        self.setWindowTitle('Ventana de Ángulos Sexagesimales')
        self.setGeometry(100, 100, 500, 200)

    def habilitar_deshabilitar(self, fila):
        if fila == 1:
            estado = self.btn_interruptor1.isChecked()
            self.edit_grados2.setReadOnly(estado)
            self.edit_minutos2.setReadOnly(estado)
            self.edit_segundos2.setReadOnly(estado)
            if estado:
                self.btn_interruptor2.setChecked(False)  # Deseleccionar el botón 2 si el botón 1 está seleccionado
        elif fila == 2:
            estado = self.btn_interruptor2.isChecked()
            self.edit_grados2.setReadOnly(not estado)
            self.edit_minutos2.setReadOnly(not estado)
            self.edit_segundos2.setReadOnly(not estado)
            if estado:
                self.btn_interruptor1.setChecked(False) 

    def mostrar_valores(self):
        grados1 = self.edit_grados1.text()
        minutos1 = self.edit_minutos1.text()
        segundos1 = self.edit_segundos1.text()

        grados2 = self.edit_grados2.text()
        minutos2 = self.edit_minutos2.text()
        segundos2 = self.edit_segundos2.text()

        mensaje1 = f'{self.texto1.text()} {grados1}º, {minutos1}\', {segundos1}\'\''
        mensaje2 = f'{self.texto2.text()} {grados2}º, {minutos2}\', {segundos2}\'\''

        print(mensaje1)
        print(mensaje2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaAngulos()
    ventana.show()
    sys.exit(app.exec())

