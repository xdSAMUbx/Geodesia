from Coord_NEU import Coord_NEU
from Angulos import Angulos
from Calc_radios import Radios
from Coords_xyz import Coords_xyz

miCoord_ENU = Coord_NEU()
miAngulo = Angulos()
miRadio = Radios()
miXYZ = Coords_xyz()
class Interactuador:

    def menu_principal (self):
        
        print("Bienvenido a esta Calculadora Geodesica. ")
        print("1. Coordenadas X,Y,Z")
        print("2. Coordenadas Cartesianas")
        print("3. Coordenadas Cartográficas")
        print("4. Coordenadas ENU")
        print("5. Inverso Coordenadas")
        
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
            pass

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
                print("Angulo φ")
                miAngulo.ang_decimales()
                miCoord_ENU.fi1 = miAngulo.decimal
                print("Angulo λ")
                miAngulo.ang_decimales()
                miCoord_ENU.lambda1 = miAngulo.decimal
                miCoord_ENU.h1 = float(input("Ingrese la Altura del Punto (h): "))
                miCoord_ENU.c = float(input("Ingrese la distanacia entre los puntos: "))
                miXYZ.fi = miCoord_ENU.fi1
                miXYZ.lon = miCoord_ENU.lambda1
                miXYZ.h = miCoord_ENU.h1
                miXYZ.calc_3D()
                miCoord_ENU.x = miXYZ.x
                miXYZ.calc_3D()
                miCoord_ENU.y = miXYZ.y
                miXYZ.calc_3D()
                miCoord_ENU.z = miXYZ.z
                print("Angulo α")
                miAngulo.ang_decimales()
                miCoord_ENU.az_12 = miAngulo.decimal
                print("Angulo Zenital (i)")
                miAngulo.ang_decimales()
                miCoord_ENU.vert = miAngulo.decimal
                miCoord_ENU.enu()
                miCoord_ENU.coords_diferenciales()
                print(f"E = {miCoord_ENU.E}")
                print(f"N = {miCoord_ENU.N}")
                print(f"U = {miCoord_ENU.U}")
                print(f"delta_x = {miCoord_ENU.delta_x}")
                print(f"delta_y = {miCoord_ENU.delta_y}")
                print(f"delta_x = {miCoord_ENU.delta_z}")
                print(f"La cordenada x del punto 2 es: {miCoord_ENU.x2}")
                print(f"La cordenada y del punto 2 es: {miCoord_ENU.y2}")
                print(f"La cordenada z del punto 2 es: {miCoord_ENU.z2}")
                
            elif opcion2 == 2:
                
                miCoord_ENU.delta_x = float(input("Ingrese el delta x entre los puntos: "))
                miCoord_ENU.delta_y = float(input("Ingrese el delta y entre los puntos: "))
                miCoord_ENU.delta_z = float(input("Ingrese el delta z entre los puntos: "))
                print(f"E = {miCoord_ENU.E}")
                print(f"N = {miCoord_ENU.N}")
                print(f"U = {miCoord_ENU.U}")

        elif opcion == 5:
            pass
        
miInteractuador = Interactuador()
miInteractuador.programa()