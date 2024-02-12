from Angulos import Angulos
from Radios import Radios
from Trans_LA import Trans_LA
from Trans_MO import Trans_MO
from Trans_HE import Trans_HE
from Coords_xyz import Coords_xyz

miAngulo = Angulos()
miRadio =  Radios()
miXYZ = Coords_xyz()
miTransformadorLA = Trans_LA()
miTransformadorMO = Trans_MO()
miTransformadorHE = Trans_HE()

class Interactuador:

    def menu(self):
        print("Bienvenido a la Calculadora Básica, por favor seleccione una opción: ")
        print("1) Transformación de Datum Molodensky para Colombia")
        print("2) Transformación de Datum Helmert para Colombia")
        val = int(input("Seleccione una opción: "))
        if val == 2: #METODO MOLODENZKY

            a = 6378388
            e = 0.006672
            miRadio.a = a
            miRadio.e_cuad = e
            miAngulo.lat()
            miRadio.fi = miAngulo.decimal
            miRadio.calc_radios()
            miTransformadorMO.lat = miAngulo.decimal
            miAngulo.lon()
            miRadio.lon = miAngulo.decimallon
            miTransformadorMO.lon = -miAngulo.gradlon
            h = int(input("Ingrese la Altura: "))
            miXYZ.N = miRadio.normal
            miXYZ.a = miRadio.a
            miXYZ.e_cuad = miRadio.e_cuad
            miXYZ.fi = miRadio.fi
            miXYZ.lon = miRadio.lon
            miXYZ.h = h
            miXYZ.calc_3D()
            miTransformadorMO.xbog = miXYZ.x
            miTransformadorMO.ybog = miXYZ.y
            miTransformadorMO.zbog = miXYZ.z
            miTransformadorMO.ts_MO()
            miTransformadorMO.mtz_MO_sir()

            print(f"Las coordenadas Datum Bogotá eran: ")
            print(f"X: {miTransformadorMO.xbog}")
            print(f"Y: {miTransformadorMO.ybog}")
            print(f"Z: {miTransformadorMO.zbog}")    
            print(f"Las coordenadas en Magna Sirgas son: ")
            print(f"X: {miTransformadorMO.xsir}")
            print(f"Y: {miTransformadorMO.ysir}")
            print(f"Z: {miTransformadorMO.zsir}") 

        elif val == 3: #METODO HELMERT

            a = 6378388
            e = 0.006672
            miRadio.a = a
            miRadio.e_cuad = e
            miAngulo.lat()
            miRadio.fi = miAngulo.decimal
            miRadio.calc_radios()
            miTransformadorHE.lat = miAngulo.decimal
            miAngulo.lon()
            miRadio.lon = miAngulo.decimallon
            miTransformadorHE.lon = -miAngulo.gradlon
            h = int(input("Ingrese la Altura: "))
            miXYZ.N = miRadio.normal
            miXYZ.a = miRadio.a
            miXYZ.e_cuad = miRadio.e_cuad
            miXYZ.fi = miRadio.fi
            miXYZ.lon = miRadio.lon
            miXYZ.h = h
            miXYZ.calc_3D()
            miTransformadorHE.xbog = miXYZ.x
            miTransformadorHE.ybog = miXYZ.y
            miTransformadorHE.zbog = miXYZ.z
            miTransformadorHE.ts_HE()
            miTransformadorHE.mtz_HE_sir()

            print(f"Las coordenadas Datum Bogotá eran: ")
            print(f"X: {miTransformadorHE.xbog}")
            print(f"Y: {miTransformadorHE.ybog}")
            print(f"Z: {miTransformadorHE.zbog}")    
            print(f"Las coordenadas en Magna Sirgas son: ")
            print(f"X: {miTransformadorHE.xsir}")
            print(f"Y: {miTransformadorHE.ysir}")
            print(f"Z: {miTransformadorHE.zsir}")    
                 
        else:

            print("Error, no es una opcion")
            miInteractuador = Interactuador()
            miInteractuador.menu()

miInteractuador = Interactuador()
miInteractuador.menu()
