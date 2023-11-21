import math

class Radios:
    
    def __init__(self):
        
        self.fi = 0
        self.lon = 0
        self.az = 0
        self.normal = 0
        self.R = 0
        self.ro = 0
        self.ro_az = 0
        self.rad_med_curv = 0
        self.a = 0
        self.e_cuad = 0
        
    def calc_radios(self):
        
        sinfi = math.sin(math.radians(self.fi))
        sinaz = math.sin(math.radians(self.az))
        cosaz = math.cos(math.radians(self.az))
        self.normal = (self.a/math.sqrt((1-(self.e_cuad*((sinfi)**2)))))
        self.R= (self.a*(1-self.e_cuad))/(1-(self.e_cuad*((sinfi)**2)))**(3/2)
        self.ro_az = (self.ro*self.normal)/((self.R*(cosaz**2))+(self.normal*(sinaz**2)))
        self.rad_med_curv = math.sqrt(self.R*self.normal)
        
    def elipsoides (self):
        
        print("Con que elipsoide desea trabajar: ")
        print("1) GRS - 80")
        print("2) Internacional")
        opcion = int(input("Seleccione el elipsoide: "))
        if opcion == 1:
            self.a = 6378137
            self.e_cuad = 0.00669438
        elif opcion == 2:
            self.a = 6378388
            self.e_cuad = 0.00672267