from sympy import symbols, sin, cos, tan, cot, csc, sec, sympify, diff, evalf
import numpy as np
import math as mh
import pandas as pd

class Vectorial:

    def __init__(self):
        
        self.vecto = []
        self.scl = 0
        self.r = 0
        self.teta = 0
        self.lon = 0

    def vectorial(self):

        self.vecto = []

        for i in range(3):
            i = input("Ingrese la componente de la función vectorial: ") 
            k = sympify(i)
            self.vecto.append(k)

        print("¿Que calculo desea realizar?")
        print("1) Divergencia ")
        print("2) Rotacional ")
        val = int(input("Seleccione una opcion: "))
        if val == 1:
            self.div()
        elif val == 2:
            self.rot()
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
        
    def div(self):

        #Creando el escalar sin evaluar
        self.vecto[0] = f"{self.vecto[0]} * ((r**2) * sin(θ))"
        self.vecto[1] = f"{self.vecto[1]} * (r * sin(θ))"
        self.vecto[2] = f"{self.vecto[2]} * r"
        const = sympify("((r**2)*sin(θ))")

        r, teta, lon = symbols("r, θ, λ")
        comp1 = diff(self.vecto[0], r) / const
        comp2 = diff(self.vecto[1], teta) / const
        comp3 = diff(self.vecto[2], lon) / const
        esc = f"( {str(comp1)} ) + ( {str(comp2)} ) + ( {str(comp3)})"

        #Derivadas parciales según la variable
        self.comp1 = (diff(self.vecto[0], r) / const).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})
        self.comp2 = (diff(self.vecto[1], teta) / const).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})
        self.comp3 = (diff(self.vecto[2], lon) / const).evalf(subs={r: self.r, teta: mh.radians(self.teta), lon: mh.radians(self.lon)})

        self.scl = self.comp1 + self.comp2 + self.comp3
        
        df = pd.DataFrame({"Sin Evaluar":[esc],"Evaluado":self.scl})
        print(df)

    def rot(self):
        pass
        

