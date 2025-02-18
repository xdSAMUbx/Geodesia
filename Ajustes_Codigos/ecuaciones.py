from angulos import Angulos
from young import MetYoung

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
        self.A = []
        self.dx = []
        self.v = []

    def parametros (self):

        self.n = int(input("Ingrese el valor de n: "))
        self.k = int(input("Ingrese el valor de k: "))
        self.tk = symbols(f't1:{self.k+1}')

    def matrices (self):

        self.lb = np.zeros((self.n,1))
        print("¿Las mediciones son distancias o angulos?")
        print("""1. Distancias
2. Angulos""")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            for i in range(0,self.n):
                self.lb[i] = float(input(f"Ingrese el valor de la X{i}: "))
        elif op == 2:
            for i in range(0,self.n):
                print(f'Ingrese el valor del X{i+1}')
                miAngulo.grad()
                self.lb[i] = miAngulo.decimal

        elif op == 3:
            for i in range(self.n):
                expr = input(f"Ingrese la expresión simbólica para X{i} en términos de t1, t2, ..., t{self.k}: ")
                try:
                    # Convertir la cadena de texto a expresión simbólica
                    expr_simb = sympify(expr)
                    self.l0.append(expr_simb)
                except Exception as e:
                    print(f"Error al interpretar la expresión: {e}")
    
    def evaluar_funciones(self):
        valores_reales = {self.tk[i]: float(self.tk[i]) for i in range(self.k)}

        resultados = []
        for i in range(self.n):
            if isinstance(self.l0[i], (int, float)):  # Si es numérico, lo dejas igual
                resultados.append(self.l0[i])
            else:  # Si es simbólico, lo evalúas
                resultado_eval = self.l0[i].evalf(subs=valores_reales)
                resultados.append(resultado_eval)

        print("Resultados evaluados:", resultados)
        return resultados

        
    def val_aprox_parametros (self):
        
         print("¿Desea hallar los valores aproximados mediante el metodo de Young?(Usar solo en caso de querer hallar coordenadas de 2 puntos en específico)")
         print("""1. Si
2. No""")
         op = int(input("Ingrese una opcion: "))

         if op == 1:
            miYoung.young()
            self.tk = np.array([miYoung.yp,miYoung.xp])
         else:
            print("¿Los valores aproximados son distancias o angulos?")
            print("""1. Distancias
 2. Angulos""")
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                self.tk0 = np.array([float(input(f"Ingrese el valor aproximado inicial de t{i}: ")) for i in range(1,self.k+1)])
            elif op == 2:
                for i in range(1,(self.k+1)):
                    print(f'Ingrese el valor aproximado inicial de t{i}')
                    miAngulo.grad()
                    self.tk0.append(miAngulo.decimal)
            else:
                print("Opción no válida")