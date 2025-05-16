import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMenu, QMessageBox,
    QLabel, QWidget, QVBoxLayout, QStackedWidget
)
from PyQt5.QtCore import Qt

class PaginaParametrico1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Interfaz: Ajuste Paramétrico - Opción 1")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajustadora Geodésica")
        self.setGeometry(300, 300, 800, 600)

        # Central widget con QStackedWidget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Página inicial
        self.pagina_inicio = QLabel("Bienvenido a la Ajustadora Geodésica")
        self.pagina_inicio.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.pagina_inicio)  # index 0

        # Otras páginas (solo una por ahora, puedes seguir agregando)
        self.pagina_param_op1 = PaginaParametrico1()
        self.stack.addWidget(self.pagina_param_op1)  # index 1

        self.crear_menu()

    def crear_menu(self):
        menubar = self.menuBar()
        ajuste_menu = menubar.addMenu("Ajuste")

        # Submenú "Paramétrico"
        param_menu = QMenu("Paramétrico", self)
        opcion1 = QAction("Opción 1", self)
        opcion1.triggered.connect(self.mostrar_parametrico_op1)

        opcion2 = QAction("Opción 2", self)
        opcion2.triggered.connect(lambda: self.mostrar_mensaje("Paramétrico", "Opción 2"))

        param_menu.addAction(opcion1)
        param_menu.addAction(opcion2)

        ajuste_menu.addMenu(param_menu)

        # Menú Ayuda
        ayuda_menu = menubar.addMenu("Ayuda")
        acerca_accion = QAction("Acerca de", self)
        acerca_accion.triggered.connect(self.mostrar_acerca)
        ayuda_menu.addAction(acerca_accion)

    def mostrar_parametrico_op1(self):
        self.stack.setCurrentWidget(self.pagina_param_op1)

    def mostrar_mensaje(self, modelo, opcion):
        QMessageBox.information(self, "Selección", f"Seleccionaste '{opcion}' en '{modelo}'")

    def mostrar_acerca(self):
        QMessageBox.information(self, "Acerca de", "Este es un ejemplo modular con vistas internas.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())