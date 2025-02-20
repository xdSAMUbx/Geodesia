import sympy as sp
from sympy import symbols, sympify

class Adjust_Niv:

    def __init__(self):
        self.n = 0
        self.k = 0
        self.tk = []
        self.lb = []
        self.l0 = []
        self.L = []
        self.A = []
        self.R = []
        self.dx = []
        self.V = []
        self.ee = []

    def mediciones(self):
        
        print("\nAcontinuación va a ingresar los valores de las mediciones:")
        for i in range (self.n):
            valor = float(input(f"X{i+1}: "))
            self.lb.append([valor])
        
        self.lb = sp.Matrix(self.lb)
        print("\nMatriz de mediciones:")
        sp.pprint(self.lb)

    def enlace(self):
        
        print("\nAcontinuación va a ingresar las ecuaciones de enlace")
        for i in range(self.n):
            expr = input(f"X{i+1} =  ")
            try:
                expr = sympify(expr)
                self.ee.append([expr])
            except:
                print("Error en la expresión")
                break
        self.ee = sp.Matrix(self.ee)
        print("\nEcuaciones de enlace: ")
        sp.pprint(self.ee)

    def val_prox(self):
        
        tk0_valores = []
        self.tk = symbols(f't1:{self.k+1}')
        print('\nAcontinuación va a ingresar los valores aproximados de los parametros')
        for i in range(self.k):
            val = float(input(f"t{i+1}: "))
            tk0_valores.append(val)
        self.l0 = sp.Matrix(self.ee.subs(dict(zip(self.tk, tk0_valores))))
        print("\nValores iniciales de las mediciones:")
        sp.pprint(self.l0)

    def ajuste(self):
        
        self.L = self.l0 - self.lb
        L = self.ee - self.lb
        self.A = L.jacobian(self.tk)
        self.R = self.A.T * self.A
        self.dx = -(self.R.inv() * self.A.T * self.L)
        self.V = self.A * self.dx + self.L

        print("\nL:")
        sp.pprint(L)
        print("\nMatriz de las derivadas (A):")
        sp.pprint(self.A)
        print("\nMatriz R: ")
        sp.pprint(self.R)
        print("\nMatriz delta x:")
        sp.pprint(self.dx)
        print("\nMatriz de las correciones (V):")
        sp.pprint(self.V)