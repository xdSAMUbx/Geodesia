import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QDesktopWidget,
                             QGridLayout, QGroupBox, QLabel, QRadioButton)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Texto Dinámico en el Grupo de Cálculos")
        self.setGeometry(100, 100, 700, 700)

        # -------------------------------Grupos de la Interfaz-------------------------------
        self.grid = QGridLayout()

        # Primer grupo ocupará 2 filas y 1 columna
        self.grid.addWidget(self.primerGrupo(), 0, 0, 1, 2)  # (fila, columna, filas ocupadas, columnas ocupadas)

        # Segundo grupo ocupará 1 fila y 2 columnas
        self.grid.addWidget(self.segundoGrupo(), 1, 0, 1, 2)  # Calculos

        # Tercer grupo ocupará 2 filas y 1 columna
        self.grid.addWidget(self.tercerGrupo(), 0, 2, 1, 1)  # Opciones

        # Cuarto grupo ocupará 1 fila y 1 columna
        self.grid.addWidget(self.quintoGrupo(), 2, 0, 1, 2)  # Resultados

        # Asignamos el layout a la ventana
        central_widget = QWidget(self)  # Crear un widget central
        central_widget.setLayout(self.grid)
        self.setCentralWidget(central_widget)

    def primerGrupo(self):
        group_box = QGroupBox("Constantes")

        # Crear una fuente de tamaño 20 para los QLabel
        font = QFont('Arial', 14)
        font2 = QFont('Arial', 12)

        # Layout vertical para los labels
        layout = QVBoxLayout()

        label1 = QLabel("""En esta sección se presentan las constantes con las cuales se va a trabajar \npara el elipsoide WGS84, se presentan en el siguiente listado:""")
        label2 = QLabel("Semiejes")
        label3 = QLabel("Semieje Mayor (a) = 6378137 m\nSemieje Menor (b) = 6356752.314 m")
        label4 = QLabel("Momentos Principales de Inercia")
        label5 = QLabel("A = 8.0091029x10^37 Kg m^2\nB = 8.0092559x10^37 Kg m^2\nC = 8.0354872x10^37\n")
        label6 = QLabel("Masa")
        label7 = QLabel("M = 5.9733x10^24 Kg")

        # Aplicar la fuente a cada QLabel individualmente
        label2.setFont(font)
        label4.setFont(font)
        label6.setFont(font)

        # Aplicar la fuente a los Qlabel de Parrafo
        label1.setFont(font2)
        label3.setFont(font2)
        label5.setFont(font2)

        # Añadir los QLabel al layout
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(label6)
        layout.addWidget(label7)

        # Asignamos el layout al groupbox
        group_box.setLayout(layout)

        return group_box

    def segundoGrupo(self):
        group_box = QGroupBox("Calculos")
        self.result_label = QLabel("Selecciona una opción en 'Opciones'")  # Default message
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)  # QLabel que se actualizará
        group_box.setLayout(layout)
        return group_box

    def tercerGrupo(self):
        group_box = QGroupBox("Opciones")
        layout = QVBoxLayout()

        # Creamos los radio buttons
        radio1 = QRadioButton("Polinomios de Legendre")
        radio2 = QRadioButton("Coeficiente de Bessel")
        radio3 = QRadioButton("Coeficientes Dinámicos")

        # Setear el primer botón como seleccionado
        radio1.setChecked(True)

        # Conectar los radio buttons con el método que actualizará el texto
        radio1.toggled.connect(lambda: self.actualizar_texto(radio1))
        radio2.toggled.connect(lambda: self.actualizar_texto(radio2))
        radio3.toggled.connect(lambda: self.actualizar_texto(radio3))

        # Añadir los radio buttons al layout
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)

        # Asignamos el layout al groupbox
        group_box.setLayout(layout)
        return group_box

    def quintoGrupo(self):
        group_box = QGroupBox("Salida Consola")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Botón 4"))
        group_box.setLayout(layout)
        return group_box

    def actualizar_texto(self, radio_button):
        # Cambiar el texto según el radio button seleccionado
        if radio_button.text() == "Polinomios de Legendre" and radio_button.isChecked():
            self.result_label.setText("Hola, Polinomios de Legendre seleccionados.")
        elif radio_button.text() == "Coeficiente de Bessel" and radio_button.isChecked():
            self.result_label.setText("¡Hola, Coeficientes de Bessel seleccionados!")
        else:
            self.result_label.setText("Selecciona una opción en 'Opciones'.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
