
from ecuaciones import Ecuaciones
from ajuste_nivelacion import Adjust_Niv
from ajuste_angulos import Adjust_Deg
from ajuste_longitud import Adjust_Lenght

misEcuaciones = Ecuaciones()
miRed = Adjust_Niv()
miDeg = Adjust_Deg()
miLon = Adjust_Lenght()

class Parametrico:

    def __init__(self):
        
        self.n = 0
        self.k = 0
        self.r = 0
        self.tk = []

    def parametros (self):

        print("\nIngrese los valores de n y k:")
        self.n = int(input("n: "))
        self.k = int(input("k: "))
        print(f'r: {self.n-self.k}')

    def menu (self):
        
        print("Bienvenido al programa de ajuste paramétrico")
        print("\nIngrese con respecto a que parametro va a ajustar: ")
        print("1. Angulos\n2. Longitudes\n3. Coordenadas\n4. Red de Nivelación")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            self.parametros()
            miDeg.n = self.n
            miDeg.k = self.k
            miDeg.mediciones()
            miDeg.enlace()
            miDeg.val_prox()
            miDeg.ajuste()

        elif opcion == 2:
            self.parametros()
            miLon.n = self.n
            miLon.k = self.k
            miLon.mediciones()
            miLon.enlace()
            miLon.val_prox()
            miLon.ajuste()

        elif opcion == 3:
            self.coordenadas()

        elif opcion == 4:
            self.parametros()
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