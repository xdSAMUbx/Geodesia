import math as mh

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
        D = (3 * self.e * sen1 * cos1 * arco) / (2*(1-(self.e*(sen1)**2)))
        E = (1 + (3 * (sen1 / cos1)**2)) / (6 * (self.N1**2))

        return B,C,D,E,arco
    
    def fnd_azs(self):

        dellam = self.lon2 - self.lon1
        delfi = (self.lat2 - self.lat1) * 3600
        sendiflon = mh.sin(mh.radians(dellam))

        

