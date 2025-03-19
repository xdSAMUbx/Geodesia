import math as mh
"""Este codigo permite calcular el problema directo geodésico"""

#Código puissant directo
class Puiss_dir:

    def __init__(self):

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
    
#Calcula la latitud del punto 2   
    def fnd_lat(self):
        

        B,C,D,E,arco = self.const()
        #Calcula el sen y cos del azimut de 1 a 2 
        senaz12 = mh.sin(mh.radians(self.az12))
        cosaz12 = mh.cos(mh.radians(self.az12))

        delfi = (B * self.s * cosaz12) - (C * (self.s**2) * (senaz12**2)) - (B * E * (self.s**2) * cosaz12 * (senaz12 ** 2)) 
        cor = D * (delfi ** 2)

        diffi = (B * self.s * cosaz12) - (C * (self.s**2) * (senaz12**2)) - (B * E * (self.s**2) * cosaz12 * (senaz12 ** 2)) - cor
        diffi = diffi / 3600
        self.lat2 = self.lat1 + diffi
        if self.lat2 < 0:
            self.lat2 *= -1 
        else:
            self.lat2

        return senaz12
        
    def fnd_lon(self):
        
        senaz12 = self.fnd_lat()
        coslat2 = mh.cos(mh.radians(self.lat2))
        x = mh.sin(mh.radians(self.s / self.N2)) 
        della = mh.degrees(mh.asin(x * senaz12 * (coslat2**-1)))
        della = della * (180 / mh.pi)
        self.lon2 = self.lon1 + della

        if self.lon2 >= 0 and self.lon2 <= 180:
            self.lon2
        elif self.lon2 > 180 and self.lon2 < 360:
            self.lon2 = 360 - self.lon2
        elif self.lon2 < 0 and self.lon2 >= -360:
            self.lon2 = 360 + self.lon2
        else:
            print("Algo fallo")

        return della

    def fnd_az(self):

        B,C,D,E,arco = self.const()
        della = self.fnd_lon()
        med = (self.lat1 + self.lat2) / 2
        senmed = mh.sin(mh.radians(med))
        cosmed = mh.cos(mh.radians(med))
        cosmed_2 = mh.cos(mh.radians(med/2))
        delaz = (della * senmed * (cosmed_2**-1)) + ((della**3 / 12) * (senmed * (cosmed**2) * (arco**2)))
        self.az21 = self.az12 + delaz + 180

        if self.az21 >= 0 and self.az21 <= 360:
            self.az21
        elif self.az21 > 360:
            self.az21 -= 360
        elif self.az21 < 0 and self.az21 > -360:
            self.az21 += 360
        else:
            print("Error")
