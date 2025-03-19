from calc_inv import Inversas
from calc_xyz import Coords_xyz
from angulos import Angulos
from radios import Radios
from trans_mo import Trans_MO

miAngulo = Angulos()
miInversa = Inversas()
miXYZ = Coords_xyz()
miRadio = Radios()
miTransMO = Trans_MO()

class MenuPruebas:

    def menu(self) -> None:

        # Calculando la transformación a fin de Molondensky
        miTransMO.transformacion_final()

if  __name__ == "__main__":
    miInteractuador = MenuPruebas()
    miInteractuador.menu()