import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QLabel)
from PyQt6.QtCore import Qt
from geometrica import VentanaGeometrica

class menu(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        
        self.setWindowTitle("Geodesia")
        # Obtener el primer monitor disponible
        primer_monitor = QApplication.primaryScreen()
        # Obtener la geometría del primer monitor
        pantalla = primer_monitor.geometry()
        # Calcular la posición para centrar la ventana en el monitor
        posicion_x = (pantalla.width() - 320) // 2
        posicion_y = (pantalla.height() - 240) // 2
        # Establecer la posición centrada
        self.setGeometry(posicion_x, posicion_y, 320, 240)
        self.adjustSize()
        # Crear el título
        titulo = QLabel("Bienvenido a Geodesia", self)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Configurar la fuente para hacer el título más grande y en negrita
        font = titulo.font()
        font.setPointSize(20)  # Tamaño de la fuente
        font.setBold(True)     # Negrita
        font.setItalic(True)
        titulo.setFont(font)
        # Crear el texto adicional
        texto_adicional = QLabel("Escoge el curso que estás cursando", self)
        texto_adicional.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Crear el botón
        btn1 = QPushButton('GEODESIA GEOMÉTRICA', self)
        btn1.clicked.connect(self.geometrica)
        btn2 = QPushButton('GEODESIA FÍSICA', self)
        btn2.clicked.connect(self.fisica)
        btn3 = QPushButton('GEODESIA SATELITAL', self)
        btn3.clicked.connect(self.satelital)
        # Crear diseño vertical
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(titulo,alignment=Qt.AlignmentFlag.AlignTop)
        layout_vertical.addWidget(texto_adicional)
        layout_vertical.addWidget(btn1)
        layout_vertical.addWidget(btn2)
        layout_vertical.addWidget(btn3)
        layout_vertical.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Configurar el diseño principal de la ventana
        self.setLayout(layout_vertical)
        self.show()

    def geometrica(self):
        self.ventana_geometrica = VentanaGeometrica()
        self.ventana_geometrica.show()
        self.close()

    def fisica(self):
        pass

    def satelital(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = menu()
    ventana.show()
    sys.exit(app.exec())