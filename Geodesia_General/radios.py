import math
"""Este código se usa para hallar los radios del elipsoide mostrados en Geodesia Geométrica y que hacen parte de la conexión
entre los modelos teóricos y los reales"""
class Radios:

    def __init__(self):
        
        self.fi:float = 0
        self.lon:float = 0
        self.az:float = 0
        self.normal:float = 0
        self.R:float = 0
        self.ro_az:float = 0
        self.rad_med_curv:float = 0
        self.a:int = 0
        self.e_cuad:float = 0
        
    def calc_radios(self) -> None:
        
        sinfi = math.sin(math.radians(self.fi))
        sinaz = math.sin(math.radians(self.az))
        cosaz = math.cos(math.radians(self.az))
        self.normal = round((self.a/math.sqrt((1-(self.e_cuad*(sinfi**2))))),4)
        self.R= round((self.a*(1-self.e_cuad))/(1-(self.e_cuad*(sinfi**2)))**(3/2),4)
        self.ro_az = round((self.R*self.normal)/((self.R*(cosaz**2))+(self.normal*(sinaz**2))),4)
        self.rad_med_curv = round(math.sqrt(self.R*self.normal),4)
        
    def elipsoides (self, opcion:int = None) -> None:
        if opcion is None:
            print("Con que elipsoide desea trabajar: ")
            print("1) GRS - 80")
            print("2) Internacional")
            opcion = int(input("Seleccione el elipsoide: "))

        if opcion == 1:
            self.a = 6378137
            self.e_cuad = 0.00669438
        elif opcion == 2:
            self.a = 6378388
            self.e_cuad = 0.006672267