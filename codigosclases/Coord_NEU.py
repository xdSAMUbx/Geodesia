import math
import numpy as np

class Coord_NEU:

    def __init__(self):
        
        self.az_12 = 0 
        self.vert = 0 
        self.fi1 = 0 
        self.lambda1 = 0 
        self.h1 = 0 
        self.fi2 = 0 
        self.lambda2 = 0
        self.h2 = 0 
        self.c = 0
        self.delta_x = 0
        self.delta_y = 0
        self.delta_z = 0
        
    def enu (self):
        
        sin_i = math.sin(math.radians(self.vert))
        cos_i = math.cos(math.radians(self.vert))
        sin_az = math.sin(math.radians(self.az_12))
        cos_az = math.cos(math.radians(self.az_12)) 
        
        E = self.c*cos_i*sin_az
        N = self.c*cos_i*cos_az
        U = self.c*sin_i
        
        return  E,N,U
    
    def coords_diferenciales(self, E, N, U):
        
        sin_fi = math.sin(math.radians(self.fi1))
        cos_fi = math.cos(math.radians(self.fi1))
        sin_lambda = math.sin(math.radians(self.lambda1))
        cos_lambda = math.cos(math.radians(self.lambda1))
        
        mtz_sin_cos = np.array([[-sin_fi*cos_lambda,-sin_fi,cos_fi*cos_lambda],[sin_fi*sin_lambda,cos_lambda,cos_fi*sin_lambda],[cos_fi,0,sin_fi]])
        mtrz_ENU = np.array([[N],[E],[U]])
        
        mtrz_delta = mtz_sin_cos @ mtrz_ENU
        
        delta_x = mtrz_delta[1,0]
        delta_y = mtrz_delta[2,0]
        delta_z = mtrz_delta[3,0]
        
        return delta_x,delta_y,delta_z
        
    def coords_ENU (self):
        
        sin_fi = math.sin(math.radians(self.fi1))
        cos_fi = math.cos(math.radians(self.fi1))
        sin_lambda = math.sin(math.radians(self.lambda1))
        cos_lambda = math.cos(math.radians(self.lambda1))
        
        mtz_sin_cos = np.array([[-sin_lambda,cos_lambda,0],[-sin_fi*cos_lambda,-sin_fi*sin_lambda,cos_fi],[cos_fi*cos_lambda,cos_fi*sin_lambda,sin_fi]])
        mtrz_delta = np.array([[self.delta_x],[self.delta_y],[self.delta_z]])
        
        mtrz_ENU = mtz_sin_cos @ mtrz_delta
        
        E = mtrz_ENU[1,0]
        N = mtrz_ENU[2,0]
        U = mtrz_ENU[3,0]
        
        self.az_12 = math.degrees(math.atan(E/N))
        self.vert = math.degrees(math.atan(U/N))
        self.c = U/math.sin(math.radians(self.vert))
        
        return E,N,U