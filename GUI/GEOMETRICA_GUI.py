from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from XYZ_GUI import XYZ

class VentanaGeometrica(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        
        self.setWindowTitle("Geodesia Geométrica")
        # Obtener el primer monitor disponible
        primer_monitor = QApplication.primaryScreen()
        # Obtener la geometría del primer monitor
        pantalla = primer_monitor.geometry()
        # Calcular la posición para centrar la ventana en el monitor
        posicion_x = (pantalla.width() - 640) // 2
        posicion_y = (pantalla.height() - 480) // 2
        # Establecer la posición centrada
        self.setGeometry(posicion_x, posicion_y, 640, 480)
        self.adjustSize()
        # Crear el título
        titulo = QLabel("Bienvenido a Geodesia Geométrica", self)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Configurar la fuente para hacer el título más grande y en negrita
        font = titulo.font()
        font.setPointSize(20)  # Tamaño de la fuente
        font.setBold(True)     # Negrita
        font.setItalic(True)
        titulo.setFont(font)
        # Crear el texto adicional
        texto_adicional = QLabel("Selecciona el tema que necesitas", self)
        texto_adicional.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Crear el botón
        btn1 = QPushButton('COORDENADAS XYZ', self)
        btn1.clicked.connect(self.coordxyz)
        btn2 = QPushButton('COORDENADAS GAUSS - KRUEGER', self)
        btn2.clicked.connect(self.coordgauss)
        btn3 = QPushButton('COORDENADAS CARTOGRÁFICAS', self)
        btn3.clicked.connect(self.coordcarto)
        btn4 = QPushButton('COORDENADAS ENU', self)
        btn4.clicked.connect(self.coordenu)
        btn5 = QPushButton('RELACIÓN LATITUDES', self)
        btn5.clicked.connect(self.latitudes)
        btn6 = QPushButton('RADIOS SOBRE ELIPSOIDE', self)
        btn6.clicked.connect(self.radios)
        btn7 = QPushButton('PUISSANT DIRECTO', self)
        btn7.clicked.connect(self.pusdir)
        btn8 = QPushButton('PUISSANT INVERSO', self)
        btn8.clicked.connect(self.pusinv)
        btn9 = QPushButton('COORDENADAS INVERSAS', self)
        btn9.clicked.connect(self.coordinv)
        btn10 = QPushButton('REDUCCIÓN DE DISTANCIAS', self)
        btn10.clicked.connect(self.reddistancias)
        btn11 = QPushButton('ALTIMETRIA DIRECTA', self)
        btn11.clicked.connect(self.altdir)
        btn12 = QPushButton('ALTIMETRIA INDIRECTA', self)
        btn12.clicked.connect(self.altindir)
        btn13 = QPushButton('TRANSFORMACION DE DATUM', self)
        btn13.clicked.connect(self.transdat)
        # Crear diseño vertical
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(titulo,alignment=Qt.AlignmentFlag.AlignTop)
        layout_vertical.addWidget(texto_adicional)
        layout_vertical.addWidget(btn1)
        layout_vertical.addWidget(btn2)
        layout_vertical.addWidget(btn3)
        layout_vertical.addWidget(btn4)
        layout_vertical.addWidget(btn5)
        layout_vertical.addWidget(btn6)
        layout_vertical.addWidget(btn7)
        layout_vertical.addWidget(btn8)
        layout_vertical.addWidget(btn9)
        layout_vertical.addWidget(btn10)
        layout_vertical.addWidget(btn11)
        layout_vertical.addWidget(btn12)
        layout_vertical.addWidget(btn13)
        layout_vertical.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Configurar el diseño principal de la ventana
        self.setLayout(layout_vertical)
        self.show()

    def coordxyz(self):
        self.XYZ = XYZ()
        self.XYZ.show()
        self.close()

    def coordgauss(self):
        pass

    def coordcarto(self):
        pass

    def coordenu(self):
        pass

    def latitudes(self):
        pass

    def radios(self):
        pass

    def pusdir(self):
        pass

    def pusinv(self):
        pass

    def coordinv(self):
        pass

    def reddistancias(self):
        pass

    def altdir(self):
        pass

    def altindir(self):
        pass

    def transdat(self):
        pass