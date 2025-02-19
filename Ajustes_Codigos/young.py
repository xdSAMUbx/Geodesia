from angulos import Angulos
import sympy as sp
import math as mh

miAngulo = Angulos()

class MetYoung:

    def __init__(self):

        self.xp = 0
        self.yp = 0


    def young (self):
            
        print('Para este programa se necesitan los valores xa(Este a),ya(Norte a),xb(Este b),yb (Este b),α,β')
        xa = float(input("Ingrese el valor de xa (Este a): "))
        ya = float(input("Ingrese el valor de ya (Norte a): "))
        xb = float(input("Ingrese el valor de xb (Este b): "))
        yb = float(input("Ingrese el valor de yb (Norte b): "))
        print("Ingrese el valor de α")
        miAngulo.grad()
        alfa = miAngulo.decimal*(mh.pi/180)
        print("Ingrese el valor de β (Angulo a corregir)")
        miAngulo.grad()
        beta = miAngulo.decimal*(mh.pi/180)

        cota = (sp.cot(alfa))
        cotb = (sp.cot(beta))

        #calculando coordenadas del punto desconocido
        a = (xa*cotb) + (xb*cota) + (yb - ya)
        b = cota + cotb
        self.xp = a/b # El valor Este del parametro aproximado

        c = (ya*cotb) + (yb*cota) + (xa - xb)
        d = cota + cotb
        self.yp = c/d #El valor Norte del parametro aproximado  