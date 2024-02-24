import math as mh
from pusdir import Directo

miDirecto = Directo()

#Codigo puissant Inverso
class Inverso:
    
    def __init__(self) :
    
        #Definiendo las variables del codigo
        self.lat1 = 0
        self.lon1 = 0
        self.lat2 = 0 #Latitud 2
        self.lon2 = 0 #Longitud 2
        self.az12 = 0 #Azimut 1 - 2
        self.az21 = 0 #Azimut 2 - 1
        self.h = 0 #Altura
        self.s = 0 #Distancia
        self.ro1 = 0
        self.N1 = 0
        self.N2 = 0
        self.e = 0

    def const(self):

        #Calcula las constantes necesarias para hacer el método de puissante directo
        sen1 = mh.sin(mh.radians(self.lat1))
        cos1 = mh.cos(mh.radians(self.lat1))
        arco = mh.sin(mh.radians(1/3600))

        B = 1/(self.ro1 * arco)
        C = ((sen1 / cos1))/ (2 * (self.ro1 * self.N1 * arco))
        D = (3 * self.e * sen1 * cos1 * arco) / (2 * (1 - (self.e * (sen1) ** 2)))
        E = (1 + (3 * (sen1 / cos1)**2)) / (6 * (self.N1**2))

        return B,C,D,E,arco
    
    def fnd_azs(self):

        #Calculos para hallar el azimut 1 - 2
        B,C,D,E,arco = self.const()
        delfi = (self.lat2 - self.lat1) * 3600
        dellam = (self.lon2 - self.lon1) 
        sendiflon = mh.sin(mh.radians(dellam))
        cos2 = mh.cos(mh.radians(self.lat2))

        x = self.N2 * sendiflon * cos2
        y = (delfi + (C * (x**2)) + (D * (delfi**2))) / (B * (1 - E * (x**2)))
        self.az12 = mh.degrees(mh.atan(x / y))

        if dellam > 0 and delfi > 0:
            self.az12 = self.az12 
        elif dellam > 0 and delfi < 0:
            self.az12 = 180 - self.az12 
        elif dellam < 0 and delfi < 0:
            self.az12 = 180 + self.az12 
        elif dellam < 0 and delfi > 0:
            self.az12 = 360 - self.az12 
            
        if self.az12 > 360:
            self.az12 = self.az12 - 360
        elif self.az12 < 0:
            self.az12 = self.az12 + 360
        
        senaz12 = mh.sin(mh.radians(self.az12))
        self.s = abs (x / senaz12)

        #Calculos para hallar el azimut 2 - 1
        mid = (self.lat2 + self.lat1) / 2
        senmid = mh.sin(mh.radians(mid))
        cosmid = mh.cos(mh.radians(mid))
        secla = mh.cos(mh.radians(delfi / 7200))
        delal = ((dellam) * senmid * (secla ** -1)) + ((dellam ** 3 / 12) * senmid * (cosmid ** 2) * arco ** 2)
        self.az21 = self.az12 + 180 + delal

        if self.az21 > 360:
            self.az21 = self.az21 - 360
        elif self.az21 < 0:
            self.az21 = self.az21 + 360
