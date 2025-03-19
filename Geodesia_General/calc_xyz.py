import math

class Coords_xyz:
    
    def __init__(self):
        
        self.fi = 0
        self.lon = 0
        self.h = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.N = 0
        self.e_cuad = 0 
        
    def calc_2D (self):
        
        cos_fi = math.cos(math.radians(self.fi))
        sin_fi = math.sin(math.radians(self.fi))
        
        self.y = round((self.N+self.h)*cos_fi,4)
        self.z = round((self.N*(1-self.e_cuad)+self.h)*sin_fi,4)
        
    def calc_3D(self):
        
        cos_fi = math.cos(math.radians(self.fi))
        sin_fi = math.sin(math.radians(self.fi))
        cos_lon = math.cos(math.radians(self.lon))
        sin_lon = math.sin(math.radians(self.lon))
        
        self.x = round((self.N+self.h)*cos_fi*cos_lon,4)
        self.y = round((self.N+self.h)*cos_fi*sin_lon,4)
        k = self.N*(1-self.e_cuad)
        c = self.h
        self.z = round((k+c)*sin_fi,4)
