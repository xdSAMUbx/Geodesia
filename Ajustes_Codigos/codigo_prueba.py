import sympy as sp
from sympy import symbols, sympify, atan2

matriz_l0 = []

n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))

def mediciones(n):

    mediciones_lista = []
    print("¿Las mediciones son angulares o longitudes?")
    print("1. Angulares\n2. Longitudes")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        for i in range(n):
            print(f"Ingrese el valor de la medición x{i+1}: ")
            valor = grad()
            mediciones_lista.append([valor])
    elif opcion == 2:
        for i in range(n):
            valor = float(input(f"Ingrese el valor de la medición x{i+1}: "))
            mediciones_lista.append([valor])
    else:
        print("Opción no válida")
        return

    matriz_columna = sp.Matrix(mediciones_lista)
    print("\nMatriz  de mediciones:")
    sp.pprint(matriz_columna)

    return matriz_columna

def grad():
    grados = float(input("Grados: "))
    minutos = float(input("Minutos: "))
    segundos = float(input("Segundos: "))
    decimal = grados + (minutos / 60) + (segundos / 3600)

    return decimal

def val_prox():

    print("¿Los valores aproximados estan en medidas angulares o longitudinales?")
    print("1. Angulares\n2. Longitudes")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print(f"Ingrese los valores aproximados del parametro t{k+1}:")
        tk0_valores = [grad() for i in range(k)]
        tk0_valores=sp.Matrix(tk0_valores)
    elif opcion == 2:
        print(f"Ingrese los valores aproximados del parametro t{k+1}:")
        tk0_valores = [float(input(f"t{i+1}: ")) for i in range(k)]
    
    return tk0_valores

def enlace(n):
    global matriz_l0
    for i in range(n):
        expr = input(f"Ingrese la expresión simbólica para x{i+1} en términos de Tk: ")
        try:
            # Sustituimos las posibles funciones atan por atan2 de manera manual
            # Solo es un ejemplo básico. Puedes adaptarlo según tus necesidades
            expr = expr.replace("atan(", "atan2(")
            expr_simb = sympify(expr, locals={'atan2': atan2})
            matriz_l0.append([expr_simb])
        except Exception as e:
            print(f"Error al interpretar la expresión: {e}")
            break


def linealizacion(matriz_l0, tk0):
    tk = symbols(f't1:{k+1}')
    matriz_l0 = sp.Matrix(matriz_l0)
    tk0_valores = [v[0] for v in tk0]

    lb = mediciones(n)

    l0 = matriz_l0.subs(dict(zip(tk, tk0_valores)))

    L_simbolico = matriz_l0 - lb

    L_evaluado = l0 - lb

    A = matriz_l0.jacobian(tk)
    R = A.T * A
    dx = -(R.inv() * A.T * L_evaluado)
    V = A * dx + L_evaluado

    print("\n L (No evaluada):")
    sp.pprint(L_simbolico)

    print("\nEvaluación de L en valores aproximados de los parámetros:")
    sp.pprint(L_evaluado)

    print("\nMatriz de las derivadas (A):")
    sp.pprint(A)

    print("\nMatriz R:")
    sp.pprint(R)

    print("\nMatriz delta x:")
    sp.pprint(dx)

    print("\nMatriz de las correciones:")
    sp.pprint(V)


enlace(n)
#linealizacion(matriz_l0)
