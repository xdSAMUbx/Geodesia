import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QLabel, QMenu,
    QVBoxLayout, QWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from parametrico import ParametricoOp1, ParametricoOp2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajustadora Geodésica")
        self.setGeometry(300, 300, 1000, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.paginas = {}

        self.crear_menu()
        self.crear_pagina_inicio()

    def crear_menu(self):
        menubar = self.menuBar()
        ajuste_menu = menubar.addMenu("Ajuste")

        param_menu = QMenu("Paramétrico", self)
        param_menu.addAction("Red de Nivel", lambda: self.mostrar_pagina("nivel", ParametricoOp1))
        param_menu.addAction("Poligonal", lambda: self.mostrar_pagina("poligonal", ParametricoOp2))
        ajuste_menu.addMenu(param_menu)

    def crear_pagina_inicio(self):
        self.pagina = QWidget()
        self.layout = QVBoxLayout(self.pagina)

        # Título
        self.titulo = QLabel("Ajustadora Geodésica")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet("font-weight: bold; margin-top: 20px;")
        self.layout.addWidget(self.titulo)

        # Párrafo introductorio
        self.parrafo = QLabel("""
            <p align="justify">
            Bienvenido al programa de ajustes geodésicos desarrollado por el <b>Instituto Geográfico Agustín Codazzi</b>.<br><br>
            El programa está dirigido a toda la comunidad geodésica colombiana con la finalidad de proporcionar 
            modelos de ajuste estandarizados según la necesidad de cada proyecto.<br><br>
            Los métodos de ajuste implementados en esta aplicación se basan principalmente en soluciones de 
            <b>Mínimos Cuadrados Ponderados</b>.<br><br>
            Los algoritmos provienen de los siguientes textos:
            <ul>
                <li>Cómputos para el Ajuste – Lecciones Prácticas de Mínimos Cuadrados para Agrimensores</li>
                <li>Ajuste Computacional – Notas tomadas para la Maestría en Ciencias Geodésicas de la Universidad Estatal de Ohio</li>
                <li>Teoría Matemática para el Ajuste</li>
            </ul>
            Para obtener más información sobre la bibliografía utilizada, diríjase al <b>README</b> incluido en los documentos de instalación.
            </p>
        """)
        self.parrafo.setWordWrap(True)
        self.parrafo.setAlignment(Qt.AlignJustify)
        self.parrafo.setStyleSheet("""
            font-size: 14px;
            padding: 20px;
            margin-left: 40px;
            margin-right: 40px;
        """)
        self.layout.addWidget(self.parrafo)

        # Texto "En colaboración con"
        colaboracion = QLabel("En colaboración con")
        colaboracion.setAlignment(Qt.AlignCenter)
        colaboracion.setStyleSheet("""
            font-size: 10px;
            color: gray;
            margin-top: 10px;
        """)
        self.layout.addWidget(colaboracion)

        # Logos
        self.logo1 = QLabel()
        self.logo2 = QLabel()
        self.pixmap1 = QPixmap("assets/logo-igac-colorhorizontal.png")
        self.pixmap2 = QPixmap("assets/Escudo_UD.svg.png")

        logos_layout = QHBoxLayout()
        logos_layout.setAlignment(Qt.AlignCenter)
        logos_layout.setSpacing(30)
        self.logo1.setAlignment(Qt.AlignCenter)
        self.logo2.setAlignment(Qt.AlignCenter)

        logos_layout.addWidget(self.logo1)
        logos_layout.addWidget(self.logo2)

        logo_widget = QWidget()
        logo_widget.setLayout(logos_layout)
        self.layout.addWidget(logo_widget)

        # Footer
        footer = QLabel("© 2025 Instituto Geográfico Agustín Codazzi - Todos los derechos reservados")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            font-size: 10px;
            color: gray;
            margin-top: 15px;
            padding-bottom: 10px;
        """)
        self.layout.addWidget(footer)

        self.stack.addWidget(self.pagina)
        self.stack.setCurrentWidget(self.pagina)

        self.resize_logos_y_titulo()  # Inicial

    def mostrar_pagina(self, key, clase_pagina):
        if key not in self.paginas:
            pagina = clase_pagina()
            self.stack.addWidget(pagina)
            self.paginas[key] = pagina
        self.stack.setCurrentWidget(self.paginas[key])

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_logos_y_titulo()

    def resize_logos_y_titulo(self):
        ancho = self.width()

        # Escalar logos proporcionalmente
        logo_width = max(60, int(ancho * 0.12))
        self.logo1.setPixmap(self.pixmap1.scaledToWidth(logo_width, Qt.SmoothTransformation))
        self.logo2.setPixmap(self.pixmap2.scaledToWidth(logo_width, Qt.SmoothTransformation))

        # Ajustar tamaño del título
        font_size = max(16, int(ancho * 0.025))
        self.titulo.setStyleSheet(f"""
            font-size: {font_size}px;
            font-weight: bold;
            margin-top: 20px;
        """)

        # Ajustar tamaño del párrafo
        parrafo_font_size = max(12, int(ancho * 0.014))
        self.parrafo.setStyleSheet(f"""
            font-size: {parrafo_font_size}px;
            padding: 20px;
            margin-left: 40px;
            margin-right: 40px;
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
