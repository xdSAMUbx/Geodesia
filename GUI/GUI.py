
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QDialog, QLineEdit, QHBoxLayout, QComboBox
from GUI_XYZ import SegundaVentana

class Menu_Principal(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculadora Coordenadas Geodésicas")
        self.menu()
        self.show()
        
    def menu(self):
        user_label = QLabel("Bienvenido a la Calculadora de Coordenadas", self)
        
        Tri_button = QPushButton("Cordenadas Tridimensionales", self)
        Tri_button.clicked.connect(self.coords_xyz)
        
        Carto_button = QPushButton("Cordenadas Cartográficas", self)
        Carto_button.clicked.connect(self.coords_carto)
        
        Carte_button = QPushButton("Cordenadas Cartesianas", self)
        Carte_button.clicked.connect(self.coords_carte)
        
        ENU_button = QPushButton("Cordenadas Locales (ENU) ", self)
        ENU_button.clicked.connect(self.coords_ENU)
        
        layout = QVBoxLayout(self)
        layout.addWidget(user_label)
        layout.addWidget(Tri_button) 
        layout.addWidget(Carto_button) 
        layout.addWidget(Carte_button) 
        layout.addWidget(ENU_button) 

        self.adjustSize()  # Ajustar automáticamente el tamaño de la ventana

    def coords_xyz(self):
        
        segunda_ventana = SegundaVentana()
        segunda_ventana.exec()
        
    def coords_carto(self):
        pass
    def coords_carte(self):
        pass
    def coords_ENU(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu_Principal()
    sys.exit(app.exec())