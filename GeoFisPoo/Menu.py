from Angulos import Angulos
from Radios import Radios
from Trans_LA import Trans_LA
from Trans_MO import Trans_MO
#from Trans_HE import Trans_HE
from Coords_xyz import Coords_xyz

miAngulo = Angulos()
miRadio =  Radios()
miXYZ = Coords_xyz()
miTransformadorLA = Trans_LA()
miTransformadorMO = Trans_MO()
#miTransformadorHE = Trans_HE()

class Interactuador:

    def menu(self):
        print("Bienvenido a la Calculadora Básica, por favor seleccione una opción: ")
        print("1) Transformación de Datum I.G.A.C")
        print("2) Transformación de Datum Molodeusky para Colombia")
        print("3) Transformación de Datum Helmert para Colombia")
        val = int(input("Seleccione una opción: "))
        if val == 1: #METODO LAURA SANCHEZ
            print("¿A que datum desea transformar las coordenadas?")
            print("1) Magna Sirgas")
            print("2) Datum Bogota")
            val2 = int(input("Ingrese su respuesta: "))
            if val2 == 1:
                a = 6378388
                e = 0.006672267
                miRadio.a = a
                miRadio.e_cuad = e
                miAngulo.lat()
                miRadio.fi = miAngulo.decimal
                miRadio.calc_radios()
                miTransformadorLA.lat = miAngulo.decimal
                miAngulo.lon()
                miRadio.lon = miAngulo.decimallon
                miTransformadorLA.lon = -miAngulo.gradlon
                h = int(input("Ingrese la Altura: "))
                miXYZ.N = miRadio.normal
                miXYZ.a = miRadio.a
                miXYZ.e_cuad = miRadio.e_cuad
                miXYZ.fi = miRadio.fi
                miXYZ.lon = miRadio.lon
                miXYZ.h = h
                miXYZ.calc_3D()
                miTransformadorLA.xbog = miXYZ.x
                miTransformadorLA.ybog = miXYZ.y
                miTransformadorLA.zbog = miXYZ.z
                miTransformadorLA.h = h
                miTransformadorLA.ts_LA()
                miTransformadorLA.mtz_LA_sir()

                print(f"Las coordenadas en el antiguo sistema eran X: {miTransformadorLA.xbog}, Y: {miTransformadorLA.ybog}, Z: {miTransformadorLA.zbog}")
                print(f"Las coordenadas del nuevo sistema son X: {miTransformadorLA.xsir}, Y: {miTransformadorLA.ysir}, Z: {miTransformadorLA.zsir}")

            elif val2 == 2:
                pass

            else:
                print("Error")

        elif val == 2: #METODO MOLODENZKY
                
            print("¿A que datum desea transformar las coordenadas?")
            print("1) Magna Sirgas")
            print("2) Datum Bogota")
            val2 = int(input("Ingrese su respuesta: "))
            if val2 == 1:

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
                miTransformadorMO.h = h
                miTransformadorMO.ts_MO()
                miTransformadorMO.mtz_MO_sir()

                print(f"Las coordenadas en el antiguo sistema eran X: {miTransformadorMO.xbog}, Y: {miTransformadorMO.ybog}, Z: {miTransformadorMO.zbog}")
                print(f"Las coordenadas del nuevo sistema son X: {miTransformadorMO.xsir}, Y: {miTransformadorMO.ysir}, Z: {miTransformadorMO.zsir}")


        elif val == 3: #METODO HELMERT
            pass
        
        else:
            print("Error, no es una opcion")
            miInteractuador = Interactuador()
            miInteractuador.menu()

miInteractuador = Interactuador()
miInteractuador.menu()
