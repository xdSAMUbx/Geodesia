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
        miAngulo.lat()
        miAngulo.lon()
        miXYZ.fi= miAngulo.decimal
        miXYZ.lon = miAngulo.decimallon
        miXYZ.h = float(input("Ingrese la altura prueba: "))
        miXYZ.calc_3D()
        miInversa.x = miXYZ.x
        miInversa.y = miXYZ.y
        miInversa.z = miXYZ.z
        miInversa.latitud()
        print(f"La longitud es: {miInversa.lon}")
        print(f"La latitud es: {miInversa.lat}")
        print(f"La altura es: {miInversa.h}")

miInteractuador = MenuPruebas()
miInteractuador.menu()