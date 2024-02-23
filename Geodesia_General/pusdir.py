import math as mh

class Directo:

    def __init__(self):

        self.lat1 = 0
        self.lon1 = 0
        self.lat2 = 0
        self.lon2 = 0
        self.az12 = 0
        self.az21 = 0
        self.h = 0
        self.ro1 = 0
        self.N1 = 0
        
    def const(self):
        
        arco = mh.sin(mh.radians())
        B = 1/(self.ro1 * arco)