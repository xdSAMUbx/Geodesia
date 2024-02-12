from Coord_NEU import Coord_NEU
from Angulos import Angulos
from Calc_radios import Radios
from Coords_xyz import Coords_xyz
from Inverso_Coords import Inverso_Coords
from Latitudes import Latitudes

miCoord_ENU = Coord_NEU()
miAngulo = Angulos()
miRadio = Radios()
miXYZ = Coords_xyz()
miInversoCoorde = Inverso_Coords()
miLat = Latitudes()

class Interactuador:

    def menu_principal (self):
        
        print("Bienvenido a esta Calculadora Geodesica. ")
        print("1. Coordenadas X,Y,Z")
        print("2. Coordenadas Cartesianas")
        print("3. Coordenadas Cartográficas")
        print("4. Coordenadas ENU")
        print("5. Relación de latitudes")

        
        entrada = int(input("Ingrese la opción: "))
        return entrada
    
    def programa (self):
        
        opcion = self.menu_principal()
        miRadio.elipsoides()
        miRadio.calc_radios()
        miXYZ.a = miRadio.a
        miXYZ.e_cuad = miRadio.e_cuad
        miXYZ.N = miRadio.normal
        
        if opcion == 1:
            print("Bienvenido en que espacio desea calcular las coordenadas")
            print("1) Y,Z")
            print("2) X,Y,Z")
            opcion2 = int(input("Seleccione una opción: "))
            
            if opcion2 == 1:
                
                miAngulo.lat()
                miXYZ.fi = miAngulo.decimal
                miXYZ.h = float(input("Ingrese la altura del punto: "))
                miXYZ.calc_2D()
                print(f"La coordenada Y es: {miXYZ.y}")
                print(f"La coordenada Z es: {miXYZ.z}")
                
            elif opcion2 == 2:
                
                miAngulo.lat()
                miRadio.fi = miAngulo.decimal
                miXYZ.fi = miAngulo.decimal
                miRadio.calc_radios()
                miXYZ.N = miRadio.normal
                miAngulo.lon()
                miXYZ.lon = miAngulo.decimallon
                miXYZ.h = float(input("Ingrese la altura del punto: "))
                miXYZ.calc_3D()
                print(f"La coordenada X es: {miXYZ.x}")
                print(f"La coordenada Y es: {miXYZ.y}")
                print(f"La coordenada Z es: {miXYZ.z}")
                
        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:

            print("¿Qué datos le estan dando?")
            print("1. φ, λ, h, α, i y la dist")
            print("2. Δx, Δy, Δz")
            opcion2 = int(input("Ingrese la opción: "))
            if opcion2 == 1:
                miCoord_ENU.pto_inicial()
                miRadio.fi = miCoord_ENU.fi1
                miXYZ.fi = miCoord_ENU.fi1
                miXYZ.lon = miCoord_ENU.lambda1
                miRadio.lon = miCoord_ENU.lambda1
                miRadio.calc_radios()
                miCoord_ENU.h1 = float(input("Ingrese la Altura del Punto (h): "))
                miCoord_ENU.c = float(input("Ingrese la distancia entre los puntos: "))
                miXYZ.N = miRadio.normal
                miXYZ.h = miCoord_ENU.h1
                miXYZ.calc_3D()
                miCoord_ENU.x = miXYZ.x
                miCoord_ENU.y = miXYZ.y
                miCoord_ENU.z = miXYZ.z
                print("Angulo α")
                miAngulo.ang_decimales()
                miCoord_ENU.az_12 = miAngulo.decimal
                print("Angulo Zenital (i)")
                miAngulo.ang_decimales()
                miCoord_ENU.vert = miAngulo.decimal
                miCoord_ENU.enu()
                miCoord_ENU.coords_diferenciales()
                miInversoCoorde.x = miCoord_ENU.x2
                miInversoCoorde.y = miCoord_ENU.y2
                miInversoCoorde.z = miCoord_ENU.z2
                miInversoCoorde.a = miRadio.a
                miInversoCoorde.e_cuad = miRadio.e_cuad
                miInversoCoorde.calc_fi()
                miInversoCoorde.calc_lambda()
                
            elif opcion2 == 2:
                
                print("Angulo φ")
                miAngulo.ang_decimales()
                miCoord_ENU.fi1 = miAngulo.decimal
                print("Angulo λ")
                miAngulo.ang_decimales()
                miCoord_ENU.lambda1 = miAngulo.decimal
                miCoord_ENU.delta_x = float(input("Ingrese el delta x entre los puntos: "))
                miCoord_ENU.delta_y = float(input("Ingrese el delta y entre los puntos: "))
                miCoord_ENU.delta_z = float(input("Ingrese el delta z entre los puntos: "))
                miCoord_ENU.coords_ENU()
                print(f"E = {miCoord_ENU.E}")
                print(f"N = {miCoord_ENU.N}")
                print(f"U = {miCoord_ENU.U}")

        elif opcion == 5:

            miRadio.elipsoides()
            miAngulo.lat()
            miRadio.fi = miAngulo.decimal
            miLat.e = miRadio.e_cuad
            print("¿Qué latitud es la principal?")
            print("1) Geodésica")
            print("2) Geocéntrica")
            print("3) Reducida")
            opcion3 = int(input("Seleccione una opción: "))
            if opcion3 == 1:
                miLat.geodesica = miAngulo.decimal
                miLat.geodes()
            elif opcion3 == 2:
                miLat.geocentrica = miAngulo.decimal
                miLat.geocen()
            elif opcion3 == 3:
                miLat.reducida = miAngulo.decimal
                miLat.reduc()
            else:
                print("Error, inicie de nuevo")
                miInteractuador.programa()

        else:
            print("Error, digito un número mal.")
            miInteractuador.programa()

miInteractuador = Interactuador()
miInteractuador.programa()