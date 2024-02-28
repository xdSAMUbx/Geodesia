from calc_inv import Inversas
from calc_xyz import Coords_xyz
from angulos import Angulos
from radios import Radios

miAngulo = Angulos()
miInversa = Inversas()
miXYZ = Coords_xyz()
miRadio = Radios()

class MenuPruebas:

    def menu(self):

        miRadio.elipsoides()
        miInversa.e = miRadio.e_cuad
        miInversa.a = miRadio.a
        miRadio.calc_radios()
        miAngulo.lat()
        miAngulo.lon()
        miXYZ.fi= miAngulo.decimal
        miXYZ.lon = miAngulo.decimallon
        miXYZ.N = miRadio.normal
        miXYZ.e_cuad = miRadio.e_cuad
        miXYZ.h = float(input("Ingrese la altura prueba: "))
        miXYZ.calc_3D()
        miInversa.x = miXYZ.x
        miInversa.y = miXYZ.y
        miInversa.z = miXYZ.z
        miInversa.latitud()
        miAngulo.decimal = miInversa.lat
        miAngulo.ang_sexagesimales()
        print(f"La latitud es: {miAngulo.grados}º {miAngulo.min}' {miAngulo.seg:.4f}''")
        miAngulo.decimal = miInversa.lon
        miAngulo.ang_sexagesimales()
        print(f"La Longitud es: {miAngulo.grados}º {miAngulo.min}' {miAngulo.seg:.4f}''")
        print(f"La altura es: {miInversa.h:.4f}")

miInteractuador = MenuPruebas()
miInteractuador.menu()