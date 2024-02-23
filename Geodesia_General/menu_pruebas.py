from pusdir import Directo
from angulos import Angulos
from radios import Radios

miAngulo = Angulos()
miDirecto = Directo()
miRadio = Radios()

class MenuPruebas:

    def menu(self):

        miRadio.elipsoides()
        miDirecto.e = miRadio.e_cuad
        print("Ingrese la latitud 1")
        miAngulo.lat()
        miDirecto.lat1 = miAngulo.decimal
        miRadio.fi = miAngulo.decimal
        print("Ingrese la longitud 1")
        miAngulo.lon()
        miDirecto.lon1 = miAngulo.decimallon
        miRadio.lon = miAngulo.decimallon
        print("Ingrese el azimut de ida")
        miAngulo.lat()
        miDirecto.az12 = miAngulo.decimal
        miRadio.az = miAngulo.decimal
        miDirecto.h = float(input("Ingrerse la Altura: "))
        miDirecto.s = float(input("Ingrerse la distancia entre los dos puntos: "))
        miRadio.calc_radios()
        miDirecto.N1 = miRadio.normal
        miDirecto.ro1 = miRadio.R
        miDirecto.const()
        miDirecto.fnd_lat()
        miAngulo.decimal = miDirecto.lat2
        miRadio.fi = miDirecto.lat2
        miRadio.calc_radios()
        miDirecto.N2 = miRadio.normal
        miAngulo.ang_sexagesimales()
        print(f"La latitud del punto 2 es: {miAngulo.grados}° {miAngulo.min}' {miAngulo.seg:.4f}''")
        miDirecto.fnd_lon()
        miAngulo.decimallon = miDirecto.lon2
        miAngulo.decimal= miAngulo.decimallon
        miAngulo.ang_sexagesimales()
        print(f"La longitud del punto 2 es: {miAngulo.grados}° {miAngulo.min}' {miAngulo.seg:.4f}''")
        miDirecto.fnd_az()
        miAngulo.decimal = miDirecto.az21
        miAngulo.ang_sexagesimales()
        print(f"El azimut de vuelta es: {miAngulo.grados}° {miAngulo.min}' {miAngulo.seg:.4f}''")
        

miInteractuador = MenuPruebas()
miInteractuador.menu()