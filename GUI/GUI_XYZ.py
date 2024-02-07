import sys
sys.path.append("c:\\Users\\samue\\Documents\\Universidad\\Cuarto Semestre\\Geodesia\\Geodesia\\CodigosPoo")
import sys
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QDialog, QLineEdit, QHBoxLayout, QComboBox
from PyQt6.QtGui import QDoubleValidator
import CodigosPoo.Coords_xyz

class SegundaVentana(QDialog):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        
        layout = QVBoxLayout()

        label = QLabel('Ingrese ϕ y λ:')
        layout.addWidget(label)

        # Configurar validadores para aceptar solo números
        validator = QDoubleValidator()

        # Crear un diseño vertical para las filas
        vbox = QVBoxLayout()
        
        # Lista de textos a la izquierda para cada fila
        textos_izquierda = ['ϕ', 'λ']
        
        # Lista de opciones para los QComboBox en la parte derecha de cada fila
        opciones_combo_box = [['N', 'S'], ['E', 'W']]
        
        # Crear dos filas
        for i in range(2):
            
            # Crear un diseño horizontal para cada fila
            hbox = QHBoxLayout()
            
             # Texto a la izquierda de cada fila
            label_text_left = QLabel(textos_izquierda[i], self)
            hbox.addWidget(label_text_left)
            
            # Agregar cuadros de texto al diseño horizontal
            self.num_input = QLineEdit(self)
            self.num_input.setValidator(validator)
            self.num_input.setFixedWidth(50)
            hbox.addWidget(self.num_input)
            
            # Texto "Hola" al lado derecho de cada cuadro de texto
            label_grad = QLabel('°')
            hbox.addWidget(label_grad)

            # Cuadro de texto más pequeño
            self.num2_input = QLineEdit(self)
            self.num2_input.setFixedWidth(50)  # Ancho fijo para hacerlo más pequeño
            hbox.addWidget(self.num2_input)
            
            # Texto "Hola" al lado derecho de cada cuadro de texto
            label_min = QLabel("'")
            hbox.addWidget(label_min)
            
            # Cuadro de texto más pequeño
            self.num3_input = QLineEdit(self)
            self.num3_input.setFixedWidth(50)  # Ancho fijo para hacerlo más pequeño
            hbox.addWidget(self.num3_input)

            # Texto "Hola" al lado derecho de cada cuadro de texto
            label_seg = QLabel('"')
            hbox.addWidget(label_seg)

            # Agregar el diseño horizontal al diseño vertical
            vbox.addLayout(hbox)
            
            # Agregar un combo box para seleccionar el tipo de cálculo en la parte derecha de la fila
            combo_box = QComboBox(self)
            combo_box.setFixedWidth(45)
            for opcion in opciones_combo_box[i]:
                combo_box.addItem(opcion)
            hbox.addWidget(combo_box)
            
        hbox = QHBoxLayout()

        num4_input = QLineEdit(self)
        num4_input.setFixedWidth(197)
        hbox.addWidget(num4_input)

        label_text = QLabel('h', self)
        hbox.addWidget(label_text)

        vbox.addLayout(hbox)

        # Agregar un texto antes del combo box
        texto_combobox = QLabel('¿Qué desea calcular?', self)
        vbox.addWidget(texto_combobox)

        # Agregar un combo box para seleccionar el tipo de cálculo
        combo_box = QComboBox(self)
        combo_box.addItem("Y,Z")
        combo_box.addItem("X,Y,Z")
        vbox.addWidget(combo_box)
        
        # Agregar el diseño vertical principal al diseño de la ventana
        layout.addLayout(vbox)
        
        # Agregar un botón para realizar alguna acción con los números ingresados
        calcular_button = QPushButton('Calcular', self)
        calcular_button.clicked.connect(self.realizar_calculo)
        layout.addWidget(calcular_button)

        self.setLayout(layout)

    def realizar_calculo(self):
        pass