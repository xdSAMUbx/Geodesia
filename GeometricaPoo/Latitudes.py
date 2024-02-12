import math as mh

class Latitudes:

    def __init__(self):
        
        self.geodesica = 0
        self.geocentrica = 0
        self.reducida = 0
        self.e = 0


    def geodes(self):

        self.geocentrica = mh.degrees(mh.atan((1-self.e)*(mh.tan(mh.radians(self.geodesica)))))
        self.reducida = mh.degrees(mh.atan((mh.sqrt(1-self.e))*(mh.tan(mh.radians(self.geodesica)))))
        print(f"La latitud geocentrica es: {self.geocentrica}")
        print(f"La latitud reducida es: {self.reducida}")

    def geocen(self):
        pass

    def reduc(self):
        pass