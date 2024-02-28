import math as mh
from sympy import symbols, series, integrate, sin, cos, tan, sqrt, evalf


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

        # Definir la constante que va por fuera de la integral
        x = self.a ** 2
        y = (1 - self.e)
        z = (mh.pi / 180) * (self.lat2 - self.lat1)
        const = x * y * z

        # Definir la variable
        lat = symbols("lat")

        # Definir la función a integrar
        func = sqrt(1 - (self.e * (sin(lat)) ** 2))

        # Serie de Taylor hasta 4 términos
        serie =  cos(lat) * (series(func, lat, 0, n=4).removeO())

        # Definir los límites
        limsup = self.lat2
        liminf = self.lat1

        # Realizar la integral
        inte = integrate(serie, (lat, limsup, liminf))
        self.area = const * inte.evalf()

