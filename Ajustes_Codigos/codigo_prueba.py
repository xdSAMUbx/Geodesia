import sympy as sp
from sympy import symbols, sympify

tk0 = [[189.641], [197.967],[190.950]]
matriz_l0 = []

n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))


def mediciones(n):
    mediciones_lista = []
    print("¿Las mediciones son angulares o longitudes?")
    print("""1. Angulares
2. Longitudes""")
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

def grad ():
        
    grados = float(input("Grados: "))
    min = float(input("Minutos: "))
    seg = float(input("Segundos: "))
    decimal = grados + (min/60) + (seg/3600)
    
    return decimal

def enlace(n):
    global matriz_l0
    for i in range(n):
        expr = input(f"Ingrese la expresión simbólica para x{i+1} en términos de Tk: ")
        try:
            expr_simb = sympify(expr)
            matriz_l0.append([expr_simb])
        except Exception as e:
            print(f"Error al interpretar la expresión: {e}")
            break

def linealizacion(matriz_l0, tk0):

    # Crear variables simbólicas t1, t2, ..., tk
    tk = symbols(f't1:{k+1}')  # Genera t1, t2, ..., tk como símbolos   
    matriz_l0 = sp.Matrix(matriz_l0)
    tk0_valores = [v[0] for v in tk0]

    # definiento lb
    lb = mediciones(n)

    # Evaluar l0 en los valores iniciales tk0
    l0 = matriz_l0.subs(dict(zip(tk, tk0_valores)))

    # Función que define la diferencia simbólica sin evaluar
    L_simbolico = matriz_l0 - lb  # Esta es la función simbólica completa

    # Evaluar L en t0 (solo para referencia)
    L_evaluado = l0 - lb

    # Matriz Jacobiana
    A = matriz_l0.jacobian(tk)
    R = A.T * A
    dx = -(R.inv() * A.T * L_evaluado)
    V = A*dx + L_evaluado

    print("\n L (No evaluada):")
    sp.pprint(L_simbolico)

    print("\nEvaluación de L en valores aproximados de los parametros:")
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
linealizacion(matriz_l0, tk0)


