from Coord_NEU import Coord_NEU
from Angulos import Angulos
from Calc_radios import Radios
from Coords_xyz import Coords_xyz
from Inverso_Coords import Inverso_Coords

miCoord_ENU = Coord_NEU()
miAngulo = Angulos()
miRadio = Radios()
miXYZ = Coords_xyz()
miInversoCoorde = Inverso_Coords()
class Interactuador:

    def menu_principal (self):
        
        print("Bienvenido a esta Calculadora Geodesica. ")
        print("1. Coordenadas X,Y,Z")
        print("2. Coordenadas Cartesianas")
        print("3. Coordenadas Cartográficas")
        print("4. Coordenadas ENU")
        
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
                
                miAngulo.ang_decimales()
                miXYZ.fi = miAngulo.decimal
                miAngulo.ang_decimales()
                miXYZ.lon = miAngulo.decimal
                miXYZ.h = float(input("Ingrese la altura del punto: "))
                miXYZ.calc_2D()
                print(f"La coordenada Y es: {miXYZ.y}")
                print(f"La coordenada Z es: {miXYZ.z}")
                
            elif opcion2 == 2:
                
                miAngulo.ang_decimales()
                miXYZ.fi = miAngulo.decimal
                miAngulo.ang_decimales()
                miXYZ.lon = miAngulo.decimal
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
                miInversoCoorde.coord_x = miCoord_ENU.x2
                miInversoCoorde.coord_y = miCoord_ENU.y2
                miInversoCoorde.coord_z = miCoord_ENU.z2
                miInversoCoorde.a = miRadio.a
                miInversoCoorde.e_cuad = miRadio.e_cuad
                miInversoCoorde.calc_lambda()
                miInversoCoorde.calc_fi()
                
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

miInteractuador = Interactuador()
miInteractuador.programa()