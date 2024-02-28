import math as mh
from sympy import symbols, integrate, sin, cos, tan, sqrt, evalf


#Calculo de un area sobre una elipse
class Area:

    def __init__(self):
        
        self.lat1 = 0
        self.lat2 = 0
        self.lon1 = 0
        self.lon2 = 0
        self.e = 0
        self.a = 0
        self.area = 0

    def integral(self):

        #Definimos la constante que va por fuera de la integral
        const = (self.a ** 2) * (1-self.e) * ((mh.pi/180)*(self.lon2-self.lon1))
        lat = symbols("lat")
        # Definir la función a integrar
        expr = cos(lat) / sqrt(1 - (self.e ** 2 * (sin(lat)) ** 2))
        #Definiendo los limites
        limsup = self.lat2
        liminf = self.lat1

        # Realizar la integral
        inte = integrate(expr, (lat,limsup,liminf))
        self.area = const * inte.evalf()

