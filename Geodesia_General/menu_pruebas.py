from gradiente import Escalares
from angulos import Angulos

miAngulo = Angulos()
miEscalar = Escalares()
class MenuPruebas:

    def menu(self):

        print("Probando Gradiente")
        print("Definiendo r,theta,lon")
        print("En este caso, fi se refiere a theta")
        miAngulo.lat()
        miEscalar.teta = miAngulo.decimal
        miAngulo.lon()
        miEscalar.lon = miAngulo.decimallon
        miEscalar.dist()
        miEscalar.escalar()

miInteractuador = MenuPruebas()
miInteractuador.menu()