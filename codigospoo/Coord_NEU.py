import math
import numpy as np
from Angulos import Angulos

miAngulo = Angulos()
class Coord_NEU:

    def __init__(self):
        
        self.az_12 = 0 
        self.vert = 0 
        self.fi1 = 0 
        self.lambda1 = 0 
        self.h1 = 0 
        self.c = 0
        self.delta_x = 0
        self.delta_y = 0
        self.delta_z = 0
        self.E = 0
        self.U = 0
        self.N = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        
    def pto_inicial (self):
        
        print("Ingrese el Angulo ϕ de donde viso ")
        miAngulo.ang_decimales()
        self.fi1 = miAngulo.decimal
        print("Ingrese el Angulo λ de donde viso ")
        miAngulo.ang_decimales()
        self.lambda1 = miAngulo.decimal
        
    def enu (self):
        
        sin_i = math.sin(math.radians(self.vert))
        cos_i = math.cos(math.radians(self.vert))
        sin_az = math.sin(math.radians(self.az_12))
        cos_az = math.cos(math.radians(self.az_12)) 
        self.vert = 90 - self.vert
        
        self.E = self.c*cos_i*sin_az
        self.N = self.c*cos_i*cos_az
        self.U = self.c*sin_i
    
    def coords_diferenciales(self):
        
        sin_fi = math.sin(math.radians(self.fi1))
        cos_fi = math.cos(math.radians(self.fi1))
        sin_lambda = math.sin(math.radians(self.lambda1))
        cos_lambda = math.cos(math.radians(self.lambda1))
        
        mtz_sin_cos = np.array([[-sin_lambda,-sin_fi*cos_lambda,cos_fi*cos_lambda],[cos_lambda,-sin_fi*sin_lambda,cos_fi*sin_lambda],[0,cos_fi,sin_fi]])
        mtrz_ENU = np.array([[self.E],[self.N],[self.U]])
        
        print("La matriz de senos y cosenos es: ")
        print(mtz_sin_cos)
        print("La matriz E.N.U es: ")
        print(mtrz_ENU)

        mtrz_delta = mtz_sin_cos @ mtrz_ENU
        
        print("La matriz de deltas es: ")
        print(mtrz_delta)
        
        self.delta_x = mtrz_delta[0,0]
        self.delta_y = mtrz_delta[1,0]
        self.delta_z = mtrz_delta[2,0]
        
        self.x2 = self.delta_x-self.x
        self.y2 = self.delta_y-self.y
        self.z2 = self.delta_z-self.z
        
        print(f"E = {self.E}")
        print(f"N = {self.N}")
        print(f"U = {self.U}")
        print(f"delta_x = {self.delta_x}")
        print(f"delta_y = {self.delta_y}")
        print(f"delta_z = {self.delta_z}")
        print(f"La cordenada x del punto 2 es: {self.x2}")
        print(f"La cordenada y del punto 2 es: {self.y2}")
        print(f"La cordenada z del punto 2 es: {self.z2}")
        
    def coords_ENU (self):
        
        sin_fi = math.sin(math.radians(self.fi1))
        cos_fi = math.cos(math.radians(self.fi1))
        sin_lambda = math.sin(math.radians(self.lambda1))
        cos_lambda = math.cos(math.radians(self.lambda1))
        
        mtz_sin_cos = np.array([[-sin_lambda,cos_lambda,0],[-sin_fi*cos_lambda,-sin_fi*sin_lambda,cos_fi],[cos_fi*cos_lambda,cos_fi*sin_lambda,sin_fi]])
        mtrz_delta = np.array([[self.delta_x],[self.delta_y],[self.delta_z]])
        
        print("La matriz de senos y cosenos es: ")
        print(mtz_sin_cos)
        print("La matriz de deltas es: ")
        print(mtrz_delta)
        
        mtrz_ENU = mtz_sin_cos @ mtrz_delta
        print("La matriz E.N.U es: ")
        print(mtrz_ENU)
        
        self.E = mtrz_ENU[0,0]
        self.N = mtrz_ENU[1,0]
        self.U = mtrz_ENU[2,0]
        
        self.az_12 = math.atan(self.E/self.N)
        self.vert = math.atan(self.U/self.N)
        self.c = self.U/math.sin(math.radians(self.vert))
