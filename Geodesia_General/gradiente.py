import numpy as np
import sympy as sp
import math as mh   

#Solicitando la función escalar ó vectorial
f = sp.sympify(input("Ingrese la función escalar o vectorial segun corresponda en terminos de r,teta,lambda: "))

r, teta, lamda = sp.symbols('r,θ,λ')
factores = [1,r,r*mh.sin(mh.radians(teta))]

grad = [sp.diff(f,var) for var in (r,teta,lamda)]

print(f'El Gradiente de {f} es: {grad}')