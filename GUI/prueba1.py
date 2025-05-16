import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel, QAction, QMessageBox, QMenu
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #----------------Titulo del Programa-----------
        self.setWindowTitle("Ajustadora Geodésica")
        self.setGeometry(300, 300, 800, 600)

        self.label = QLabel("Bienvenido a la Ajustadora Geodésica", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.crear_menu()

    def crear_menu(self):
        menubar = self.menuBar()

        # Menú principal
        ajuste_menu = menubar.addMenu("Ajuste")

        # Crear submenús con "Opción 1" y "Opción 2"
        modelos = ["Paramétrico", "Correlativo", "Colocación", "GMM", "GHM"]

        for nombre_modelo in modelos:
            submenu = QMenu(nombre_modelo, self)

            opcion1 = QAction("Nivelación", self)
            opcion1.triggered.connect(lambda _, n=nombre_modelo: self.opcion_seleccionada(n, "Nivelación"))

            opcion2 = QAction("Poligonal", self)
            opcion2.triggered.connect(lambda _, n=nombre_modelo: self.opcion_seleccionada(n, "Poligonal"))

            submenu.addAction(opcion1)
            submenu.addAction(opcion2)

            ajuste_menu.addMenu(submenu)

        # Menú Ayuda
        ayuda_menu = menubar.addMenu("Ayuda")
        acerca_accion = QAction("Acerca de", self)
        acerca_accion.triggered.connect(self.mostrar_acerca)
        ayuda_menu.addAction(acerca_accion)

    def mostrar_acerca(self):
        QMessageBox.information(self, "Acerca de", "Este menú es modular.")

    def opcion_seleccionada(self, modelo, opcion):
        QMessageBox.information(self, "Selección", f"Seleccionaste '{opcion}' en '{modelo}'")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())