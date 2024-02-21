#Calculadora de operaciones vectoriales para coordenadas esféricas

from sympy import symbols, sin, cos, tan,sympify,diff, evalf
import numpy as np
import pandas as pd
import math as mh

"""
Factores de escala
h_r = 1
h_θ = r
h_λ = rsen(θ)
"""

#Creando clase para funciones Vectoriales
class Escalares:

    def __init__(self):
        
        self.scl = ""
        self.comp1 = ""
        self.comp2 = ""
        self.comp3 = ""
        self.gradi = []
        self.laplac = ""
        self.r = 0
        self.teta = 0
        self.lon = 0

#Función que nos determina si queremos hacer el laplaciano o el gradiente para la función vectorial
    def escalar(self):
        f_str = input("Ingrese la función escalar de manera lineal, para aplicar el operador Nabla y obtener su gradiente: ")
        self.scl = sympify(f_str)
        print("¿Que calculo desea realizar?")
        print("1) Gradiente ")
        print("2) Laplaciano ")
        val = int(input("Seleccione una opcion: "))
        if val == 1:
            self.gradiente()
        elif val == 2:
            self.laplaciano()
        else:
            print("No selecciono una opcion optima")

#Función que nos calcula la distancia
    def dist(self):
        print("Si no tiene la distancia, digite 0")
        self.r = float(input("Ingrese la distancia(r): "))
        if self.r == 0:
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            z = float(input("Ingrese la coordenada z: "))
            self.r = mh.sqrt( x**2 + y**2 + z**2)
            
# Función que calcula el gradiente en cooordenadas esféricas
    def gradiente(self):

        r, teta, lon = symbols("r, θ, λ") #lon hace referencia a longitud
        #Derivadas parciales sin evaluar
        comp1 = diff(self.scl, r) 
        comp2 = diff(self.scl, teta) 
        comp3 = diff(self.scl, lon) 
        vector = [comp1,comp2,comp3]
        if comp3 == 0:
            gradiente = np.reshape(vector[:2],(2,1))
        else:
            gradiente = np.reshape(vector,(3,1))
        #Derivadas parciales según la variable
        self.comp1 = diff(self.scl, r).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})
        self.comp2 = diff(self.scl, teta).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})
        self.comp3 = diff(self.scl, lon).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})
        vector1 = [self.comp1,self.comp2,self.comp3] #funcion vectorial evaluada
        if self.comp3 == 0:
            self.gradi = np.reshape(vector1[:2],(2,1))
        else:
            self.gradi = np.reshape(vector1,(3,1))

        df_grad = pd.DataFrame({'Derivada':gradiente, 'Evaluada':self.gradi})
        print(df_grad)
        
    def laplaciano(self):
        pass