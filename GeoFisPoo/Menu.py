from Angulos import Angulos
from Radios import Radios
from Trans_IGAC import Trans_IGAC
from Coords_xyz import Coords_xyz

miAngulo = Angulos()
miRadio =  Radios()
miXYZ = Coords_xyz()
miTransformador = Trans_IGAC()

class Interactuador:

    def menu(self):
        print("Bienvenido a la Calculadora Básica, por favor seleccione una opción: ")
        print("1) Transformación de Datum I.G.A.C")
        print("2) Transformación de Datum Molodeusky para Colombia")
        print("3) Transformación de Datum Helmert para Colombia")
        val = int(input("Seleccione una opción: "))
        if val == 1:
            print("¿A que datum desea transformar las coordenadas?")
            print("1) Magna Sirgas")
            print("2) Datum Bogota")
            val2 = int(input("Ingrese su respuesta: "))
            if val2 == 1:
                a = 6378388
                e = 0.006672267
                miRadio.a = a
                miRadio.e_cuad = e
                print("Ingrese la Latitud ()")
                miAngulo.ang_decimales()
                miRadio.fi = miAngulo.decimal
                miRadio.calc_radios()
                miTransformador.lat = miAngulo.decimal
                print("Ingrese la Longitud (λ)")
                miAngulo.ang_decimales()
                miRadio.lon = miAngulo.decimal
                miTransformador.lon = miAngulo.decimal
                h = int(input("Ingrese la Altura: "))
                miXYZ.N = miRadio.normal
                miXYZ.a = miRadio.a
                miXYZ.e_cuad = miRadio.e_cuad
                miXYZ.fi = miRadio.fi
                miXYZ.lon = miRadio.lon
                miXYZ.h = h
                miXYZ.calc_3D()
                miTransformador.xbog = miXYZ.x
                miTransformador.ybog = miXYZ.y
                miTransformador.zbog = miXYZ.z
                miTransformador.h = h
                miTransformador.trans_sir()

                print(f"Las coordenadas en el antiguo sistema eran X: {miTransformador.xbog}, Y: {miTransformador.ybog}, Z: {miTransformador.zbog}")
                print(f"Las coordenadas del nuevo sistema son X: {miTransformador.xsir}, Y: {miTransformador.ysir}, Z: {miTransformador.zsir}")

            elif val2 == 2:
                pass

            else:
                print("Error")

        elif val == 2:
            pass

        elif val == 3:
            pass
        
        else:
            print("Error, no es una opcion")
            miInteractuador = Interactuador()
            miInteractuador.menu()

miInteractuador = Interactuador()
miInteractuador.menu()
