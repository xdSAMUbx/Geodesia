import math

class Coords_xyz:
    
    def __init__(self):
        
        self.fi = 0
        self.lon = 0
        self.h = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.a = 0
        self.N = 0
        self.e_cuad = 0 
        
    def calc_2D (self):
        
        cos_fi = math.cos(math.radians(self.fi))
        sin_fi = math.sin(math.radians(self.fi))
        
        self.y = (self.N+self.h)*cos_fi
        self.z = (self.N*(1-self.e_cuad)+self.h)*sin_fi
        
    def calc_3D(self):
        
        cos_fi = math.cos(math.radians(self.fi))
        sin_fi = math.sin(math.radians(self.fi))
        cos_lon = math.cos(math.radians(self.lon))
        sin_lon = math.sin(math.radians(self.lon))
        
        self.x = (self.N+self.h)*cos_fi*cos_lon
        self.y = (self.N+self.h)*cos_fi*sin_lon
        self.z = (self.N*(1-self.e_cuad)+self.h)*sin_fi
