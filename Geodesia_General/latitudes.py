import math as mh

class Latitudes:

    def __init__(self):
        
        self.geodesica = 0
        self.geocentrica = 0
        self.reducida = 0
        self.e = 0
        self.a = 0


    def geodes(self):

        self.geocentrica = mh.degrees(mh.atan((1-self.e)*(mh.tan(mh.radians(self.geodesica)))))
        self.reducida = mh.degrees(mh.atan((mh.sqrt(1-self.e))*(mh.tan(mh.radians(self.geodesica)))))

        print(f'La coordenada geocentrica es: {self.geocentrica}')
        print(f'La coordenada reducida es: {self.geocentrica}')

    def geocen(self):

        b = self.a*mh.sqrt(1-self.e)
        self.geodesica = mh.degrees(mh.atan((mh.tan(mh.radians(self.geocentrica)))/1-self.e))
        self.reducida = mh.degrees((self.a/b)*(mh.tan(self.geocentrica)))

        print(f'La coordenada geodesica es: {self.geodesica}')
        print(f'La coordenada reducida es: {self.geocentrica}')

    def reduc(self):
        
        b = self.a*mh.sqrt(1-self.e)
        self.geodesica = mh.degrees(mh.atan((mh.tan(mh.radians(self.reducida)))/mh.sqrt(1-self.e)))
        self.geocentrica = mh.degrees(mh.atan((b/self.a)*(mh.tan(mh.radians(self.reducida)))))

        print(f'La coordenada geocentrica es: {self.geocentrica}')
        print(f'La coordenada geodesica es: {self.geodesica}')