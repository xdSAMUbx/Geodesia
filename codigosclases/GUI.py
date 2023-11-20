import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout, QLineEdit

from Coord_NEU import Coord_NEU
from Angulos import Angulos

class Interactuador(QWidget):
    
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle('Calculadora Geodésica')
        self.setGeometry(100, 100, 400, 200)

        # Crear widgets
        self.label1 = QLabel('¿Qué datos le están dando?')
        self.combo1 = QComboBox()
        self.combo1.addItem('φ,λ,h,α,i y la dist')
        self.combo1.addItem('Δx, Δy, Δz')
        self.label2 = QLabel('Angulo φ')
        self.edit1 = QLineEdit()
        self.label3 = QLabel('Angulo λ')
        self.edit2 = QLineEdit()
        self.label4 = QLabel('Altura del Punto (h)')
        self.edit3 = QLineEdit()
        self.label5 = QLabel('Distancia entre los puntos')
        self.edit4 = QLineEdit()
        self.label6 = QLabel('Angulo α')
        self.edit5 = QLineEdit()
        self.label7 = QLabel('Angulo Zenital (i)')
        self.edit6 = QLineEdit()
        self.button1 = QPushButton('Calcular')
        self.label8 = QLabel('E = ')
        self.label9 = QLabel('N = ')
        self.label10 = QLabel('U = ')
        self.label11 = QLabel('delta_x = ')
        self.label12 = QLabel('delta_y = ')
        self.label13 = QLabel('delta_z = ')

        # Crear diseño
        layout1 = QVBoxLayout()
        layout1.addWidget(self.label1)
        layout1.addWidget(self.combo1)
        layout1.addWidget(self.label2)
        layout1.addWidget(self.edit1)
        layout1.addWidget(self.label3)
        layout1.addWidget(self.edit2)
        layout1.addWidget(self.label4)
        layout1.addWidget(self.edit3)
        layout1.addWidget(self.label5)
        layout1.addWidget(self.edit4)
        layout1.addWidget(self.label6)
        layout1.addWidget(self.edit5)
        layout1.addWidget(self.label7)
        layout1.addWidget(self.edit6)
        layout1.addWidget(self.button1)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.label8)
        layout2.addWidget(self.label9)
        layout2.addWidget(self.label10)

        layout3 = QHBoxLayout()
        layout3.addWidget(self.label11)
        layout3.addWidget(self.label12)
        layout3.addWidget(self.label13)

        layout4 = QVBoxLayout()
        layout4.addLayout(layout2)
        layout4.addLayout(layout3)

        layout5 = QHBoxLayout()
        layout5.addLayout(layout1)
        layout5.addLayout(layout4)

        # Establecer el diseño en la ventana
        self.setLayout(layout5)

        # Conectar el botón a la función de cálculo
        self.button1.clicked.connect(self.calcular)

    def calcular(self):
        miCoord_ENU = Coord_NEU()
        miAngulo = Angulos()

        if self.combo1.currentIndex() == 0:
            miAngulo.decimal = float(self.edit1.text())
            miCoord_ENU.fi1 = miAngulo.decimal
            miAngulo.decimal = float(self.edit2.text())
            miCoord_ENU.lambda1 = miAngulo.decimal
            miCoord_ENU.h1 = float(self.edit3.text())
            miCoord_ENU.c = float(self.edit4.text())
            miAngulo.decimal = float(self.edit5.text())
            miCoord_ENU.az_12 = miAngulo.decimal
            miAngulo.decimal = float(self.edit6.text())
            miCoord_ENU.vert = miAngulo.decimal

            miCoord_ENU.enu()
            miCoord_ENU.coords_diferenciales()

            self.label8.setText(f'E = {miCoord_ENU.E}')
            self.label9.setText(f'N = {miCoord_ENU.N}')
            self.label10.setText(f'U = {miCoord_ENU.U}')

            self.label11.setText(f'delta_x = {miCoord_ENU.delta_x}')
            self.label12.setText(f'delta_y = {miCoord_ENU.delta_y}')
            self.label13.setText(f'delta_z = {miCoord_ENU.delta_z}')

        elif self.combo1.currentIndex() == 1:
            miCoord_ENU.delta_x = float(self.edit1.text())
            miCoord_ENU.delta_y = float(self.edit2.text())
            miCoord_ENU.delta_z = float(self.edit3.text())

            miCoord_ENU.coords_cartesianas()
            miCoord_ENU.enu()
            miCoord_ENU.coords_diferenciales()

            self.label8.setText(f'E = {miCoord_ENU.E}')
            self.label9.setText(f'N = {miCoord_ENU.N}')
            self.label10.setText(f'U = {miCoord_ENU.U}')

            self.label11.setText(f'delta_x = {miCoord_ENU.delta_x}')
            self.label12.setText(f'delta_y = {miCoord_ENU.delta_y}')
            self.label13.setText(f'delta_z = {miCoord_ENU.delta_z}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interactuador()
    ventana.show()
    sys.exit(app.exec())