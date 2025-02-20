from ecuaciones import Ecuaciones
from ajuste_nivelacion import Adjust_Niv


misEcuaciones = Ecuaciones()
miRed = Adjust_Niv()

class Parametrico:

    def __init__(self):
        
        self.n = 0
        self.k = 0
        self.r = 0
        self.tk = []

    def menu (self):
        
        print("Bienvenido al programa de ajuste paramétrico")
        print("\nIngrese los valores de n y k:")
        self.n = int(input("n: "))
        self.k = int(input("k: "))
        print(f'r: {self.n-self.k}')
        print("\nIngrese con respecto a que parametro va a ajustar: ")
        print("1. Angulos\n2. Longitudes\n3. Coordenadas\n4. Red de Nivelación")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            self.angulos()
        elif opcion == 2:
            self.longitudes()
        elif opcion == 3:
            self.coordenadas()
        elif opcion == 4:
            miRed.n = self.n
            miRed.k = self.k
            miRed.mediciones()
            miRed.enlace()
            miRed.val_prox()
            miRed.ajuste()

        else:
            print("Opción no válida")
            return
 

        pass

miInteractuador = Parametrico()
miInteractuador.menu()