from op_vectorial import Vectorial
from angulos import Angulos

miAngulo = Angulos()
miVectorial= Vectorial()

class MenuPruebas:

    def menu(self):

        print("Probando Gradiente")
        print("Definiendo r,theta,lon")
        print("En este caso, fi se refiere a theta")
        miAngulo.lat()
        miVectorial.teta = miAngulo.decimal
        miAngulo.lon()
        miVectorial.lon = miAngulo.decimallon
        miVectorial.dist()
        miVectorial.vectorial()

miInteractuador = MenuPruebas()
miInteractuador.menu()