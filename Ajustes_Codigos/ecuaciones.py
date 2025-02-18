from angulos import Angulos
import mpmath as mph
import numpy as np

miAngulo = Angulos()

class Ecuaciones:

    def __init__(self):

        self.n = 0
        self.k = 0
        self.tk = []

    def young (self):
        
        print('Para este programa se necesitan los valores xa(Este a),ya(Norte a),xb(Este b),yb (Este b),α,β')
        xa = float(input("Ingrese el valor de xa: "))
        ya = float(input("Ingrese el valor de ya: "))
        xb = float(input("Ingrese el valor de xb: "))
        yb = float(input("Ingrese el valor de yb: "))
        miAngulo.grad()
        alfa = miAngulo.decimal
        miAngulo.grad()
        beta = miAngulo.decimal

        cota = (mph.cot(alfa))
        cotb = (mph.cot(beta))

        #calculando coordenadas del punto desconocido

        a = (xa*cota) + (xb*cotb) + yb - ya
        b = cota + cotb
        self.tk[1] = a/b # El valor Este del parametro aproximado

        c = (ya*cotb) + (yb*cota) + xa - xb
        d = cotb + cota
        self.tk[0] = c/d #El valor Norte del parametro aproximado  

    def parametros (self):

        self.n = int(input("Ingrese el valor de n: "))
        self.k = int(input("Ingrese el valor de k: "))

    def val_aprox_parametros (self):
        
         print("¿Desea hallar los valores aproximados mediante el metodo de Young?(Usar solo en caso de querer hallar coordenadas de 2 puntos en específico)")
         print("""1. Si
2. No""")
         op = int(input("Ingrese una opcion: "))

         if op == 1:
             self.young()
         else:
            self.tk = np.array([float(input(f"Ingrese el valor aproximado inicial de t{i}: ")) for i in range(1,self.k+1)])
        