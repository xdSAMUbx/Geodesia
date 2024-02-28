import math as mh
from radios import Radios

miRadio = Radios()


class Inversas:

    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.lat = 0
        self.lon = 0
        self.h = 0
        self.e = 0
        self.a = 0
        self.N = 0

    def latitud(self):
        
        self.lon = mh.degrees(mh.atan(self.y / self.x))
        self.lat = mh.degrees(mh.atan(((1 / (1 - self.e)) * (self.z / mh.sqrt(self.x ** 2 + self.y ** 2)))))
        miRadio.fi = self.lat
        miRadio.a = self.a
        miRadio.e_cuad = self.e
        miRadio.calc_radios()
        self.h = ((mh.sqrt(self.x ** 2 + self.y ** 2))) / (mh.cos(mh.radians(self.lat))) 
        self.N = miRadio.normal
        for i in range(0,10):
            self.lat = mh.degrees(mh.atan(((self.z + (self.e * self.N * mh.sin(mh.radians(self.lat))))) / mh.sqrt(self.x ** 2 + self.y ** 2)))
            miRadio.fi = self.lat
            miRadio.calc_radios()
            self.N = miRadio.normal
            self.h = ((mh.sqrt(self.x ** 2 + self.y ** 2) / mh.cos(mh.radians(self.lat))))

