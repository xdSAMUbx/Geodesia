from pusinv import Inverso
from pusdir import Directo
from Angulos import Angulos
from radios import Radios

miAngulo = Angulos()
miInverso = Inverso()
miDirecto = Directo()
miRadio = Radios()

class MenuPruebas:

    def menu(self):

        miRadio.elipsoides()
        #Ingresando datos del punto 1
        miAngulo.lat()
        miRadio.fi = miInverso.lat1 = miAngulo.decimal
        miAngulo.lon()
        miRadio.lon = miInverso.lon1 = miAngulo.decimallon
        miRadio.calc_radios()
        miInverso.N1 = miRadio.normal
        #Ingresando datos del punto 2
        miAngulo.lat()
        miRadio.fi = miInverso.lat2 = miAngulo.decimal
        miAngulo.lon()
        miRadio.lon = miInverso.lon2 = miAngulo.decimallon
        miRadio.calc_radios()
        miInverso.N2 = miRadio.normal
        miInverso.ro1 = miRadio.R
        miInverso.e = miRadio.e_cuad
        miInverso.fnd_azs()
        miAngulo.decimal = miInverso.az12
        miAngulo.ang_sexagesimales()
        print(f"El azimut de 1 - 2 es: {miAngulo.grados}° {miAngulo.min}' {miAngulo.seg:.4f}''")
        miAngulo.decimal = miInverso.az21
        miAngulo.ang_sexagesimales()
        print(f"El azimut de 2 - 1 es: {miAngulo.grados}° {miAngulo.min}' {miAngulo.seg:.4f}''")
        print(f"La distancia entre los dos puntos es: {miInverso.s:.4f}")

miInteractuador = MenuPruebas()
miInteractuador.menu()