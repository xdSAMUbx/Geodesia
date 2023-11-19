from Coord_NEU import Coord_NEU
from Angulos import Angulos

class Interactuador:
    
    def menu_principal ():
        
        print("Bienvenido a esta Calculadora Geodesica. ")
        print("1. Coordenadas X,Y,Z")
        print("2. Coordenadas Cartesianas")
        print("3. Coordenadas Cartográficas")
        print("4. Coordenadas ENU")
        print("5. Puissant Directo")
        print("6. Puissant Inverso")
        print("7. Inverso Coordenadas")
        
        entrada = int(input("Ingrese la opción: "))
        return entrada
    
    def programa (self):
        
        opcion = self.menu_principal
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            
            miCoord_ENU = Coord_NEU() 
            miAngulo = Angulos()
            print("¿Qué datos le estan dando?")
            print("1. fi,lambda,h,alfa,i y la distancia")
            print("2. Delta x,y,z")
            opcion2 = int(input("Ingrese la opción: "))
            if opcion2 == 1:
                miCoord_ENU.fi1 = miAngulo.
                miCoord_ENU.lambda1 = miAngulo.
                miCoord_ENU.h1 = float(input("Ingrese la Altura del Punto 1: "))
                miCoord_ENU.c = float(input("Ingrese la distanacia entre los puntos: "))
                miCoord_ENU.az_12 = miAngulo
                miCoord_ENU.vert = 0
            
            elif opcion2 == 2:
                
                miCoord_ENU.delta_x = float(input("Ingrese el delta x entre los puntos: "))
                miCoord_ENU.delta_y = float(input("Ingrese el delta y entre los puntos: "))
                miCoord_ENU.delta_z = float(input("Ingrese el delta z entre los puntos: "))
            