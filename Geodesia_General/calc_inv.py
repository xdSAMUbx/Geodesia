import math as mh
from radios import Radios

miRadio = Radios()


# Calculando las coordenadas inversas
class Inversas:

    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.h = 0
        self.a = 0
        self.e = 0
        self.N = 0
        self.lat = 0
        self.lon = 0

    def latitud(self):

        self.lon = mh.degrees(mh.atan( self.y / self.x))

        # Primera aproximación con h = 0
        self.lat = mh.degrees(mh.atan((1 / (1 - self.e)) * (self.z / mh.sqrt(self.x ** 2 + self.y ** 2))))
        
        #Calculando con la primera aproximación de la latitud
        miRadio.fi = self.lat
        miRadio.a = self.a
        miRadio.e_cuad =self.e
        miRadio.calc_radios()
        self.N = miRadio.normal

        #Haciendo el calculo con las iteraciones 
        for i in range(0,5):

            self.lat = mh.degrees(mh.atan((self.z + self.e * self.N * mh.sin(mh.radians(self.lat))) / (mh.sqrt(self.x ** 2 + self.y ** 2))))
            miRadio.fi = self.lat
            miRadio.calc_radios()
            self.N = miRadio.normal
            self.h = ((mh.sqrt(self.x ** 2 + self.y ** 2)) / (mh.cos(mh.radians(self.lat))) - self.N)
