from angulos import Angulos
from young import MetYoung

import sympy as sp
from sympy import symbols, sympify
import numpy as np

miAngulo = Angulos()
miYoung = MetYoung()

class Ecuaciones:

    def __init__(self):

        self.n = 0
        self.k = 0
        self.tk = []
        self.tk0 = []
        self.lb = []
        self.l0 = []
        self.med = []
        self.A = []
        self.dx = []
        self.v = []

    def parametros (self):

        self.n = int(input("Ingrese el valor de n: "))
        self.k = int(input("Ingrese el valor de k: "))
        self.tk = symbols(f't1:{self.k+1}')

    def val_aprox_parametros (self):
        
         print("¿Desea hallar los valores aproximados mediante el metodo de Young?")
         print("1. Si\n2. No")
         op = int(input("\nIngrese una opcion: "))
         if op == 1:
            miYoung.young()
            self.tk0 = np.array([miYoung.yp,miYoung.xp])
         else:
            print("\n¿Los valores aproximados son angulares o longitudinales?")
            print("1. Longitudes\n2. Angulos")
            op = int(input("\nIngrese una opcion: "))
            if op == 1:
                self.tk0 = np.array([float(input(f"\nIngrese el valor aproximado inicial de t{i}: ")) for i in range(1,self.k+1)])
            elif op == 2:
                for i in range(1,(self.k+1)):
                    print(f'\nIngrese el valor aproximado inicial de t{i}')
                    miAngulo.grad()
                    self.tk0.append(miAngulo.decimal)
            else:
                print("Opción no válida")

    def mediciones(self):
        mediciones_lista = []
        print("\n¿Las mediciones son angulares o longitudes?")
        print("1. Angulares\n2. Longitudes")
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            for i in range(self.n):
                print(f"\nIngrese el valor de la medición x{i+1}: ")
                miAngulo.grad()
                valor = miAngulo.decimal
                mediciones_lista.append([valor]) 
        elif opcion == 2:
            for i in range(self.n):
                valor = float(input(f"\nIngrese el valor de la medición x{i+1}: "))
                mediciones_lista.append([valor]) 
        else:
            print("Opción no válida")
            return
        
        self.med = sp.Matrix(mediciones_lista)
        self.lb = self.med
        
    def enlace(self):
        for i in range(self.n):
            expr = input(f"\nIngrese la expresión simbólica para x{i+1} en términos de Tk: ")
            try:
                expr_simb = sympify(expr)
                self.l0.append([expr_simb])
            except Exception as e:
                print(f"\nError al interpretar la expresión: {e}")
                break

    def linealizacion(self):

        tk0_valores = [v[0] for v in self.tk0]

        # Evaluar l0 en los valores iniciales tk0
        l0 = self.l0.subs(dict(zip(self.tk, tk0_valores)))

        # Función que define la diferencia simbólica sin evaluar
        L_simbolico = l0 - self.med  # Esta es la función simbólica completa

        # Evaluar L en t0 (solo para referencia)
        L_evaluado = l0 - self.med

        # Matriz Jacobiana
        self.A = self.l0.jacobian(self.tk)
        self.R = self.A.T * self.A
        self.dx = -(self.R.inv() * self.A.T * L_evaluado)
        self.V = self.A*self.dx + L_evaluado

        print("\n L (No evaluada):")
        sp.pprint(L_simbolico)

        print("\nEvaluación de L en valores aproximados de los parametros:")
        sp.pprint(L_evaluado)

        print("\nMatriz de las derivadas (A):")
        sp.pprint(self.A)

        print("\nMatriz R:")
        sp.pprint(self.R)

        print("\nMatriz delta x:")
        sp.pprint(self.dx)

        print("\nMatriz de las correciones:")
        sp.pprint(self.V)

