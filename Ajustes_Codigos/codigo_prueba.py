import sympy as sp
from sympy import sqrt
def distancias():

        coords = []
        while True:
            try:
                num = int(input("\nIngrese la cantidad de puntos de observados: "))
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        for i in range(num):
            norte = float(input(f'Norte {i+1}:'))
            este = float(input(f"Este {i+1}: "))
            coords.append([norte, este])
        print(coords)

        dist =[]
        for i in range(num):
            m = sp.sqrt((coords[i+1][1] - coords[i][1])**2 + (coords[i+1][0] - coords[i][0])**2)
            dist.append(m)
        print(dist)

distancias()