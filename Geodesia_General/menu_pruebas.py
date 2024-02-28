from area_elipsoide import Area
from angulos import Angulos
from radios import Radios

miAngulo = Angulos()
miArea = Area()
miRadio = Radios()

class MenuPruebas:

    def menu(self):

        miRadio.elipsoides()
        #Ingresando datos del punto 1
        miAngulo.lat()
        miArea.lat1 = miAngulo.decimal
        miAngulo.lon()
        miArea.lon1 = miAngulo.decimallon
        #Ingresando datos del punto 2
        miAngulo.lat()
        miArea.lat2 = miAngulo.decimal
        miAngulo.lon()
        miArea.lon2 = miAngulo.decimallon

        #Ingresando los valores para el calculo
        miArea.e = miRadio.e_cuad
        miArea.a = miRadio.a
        miArea.integral()
        print(f"EL area dentro del elipsoide es: {miArea.area} m²")




miInteractuador = MenuPruebas()
miInteractuador.menu()