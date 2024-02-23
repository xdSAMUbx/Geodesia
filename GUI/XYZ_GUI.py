import os
import sys

actual = os.path.dirname(os.path.abspath(__file__))
general = os.path.join(actual,'..','CODIGOS_GEODESIA')
geodesia_general_path = os.path.join(general,'Geodesia_General')
sys.path.append(geodesia_general_path)

from Geodesia_General.xyz import Coords_xyz
from PyQt6.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QLabel)
from PyQt6.QtCore import Qt

ruta_geodesia = os.path.join('CODIGOS_GEODESIA', 'Geodesia_General', 'xyz.py')

from Geodesia_General.xyz import Coords_xyz

class XYZ(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle("Coordenadas XYZ")
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