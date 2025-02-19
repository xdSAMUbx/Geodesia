import sympy as sp

xa = 4
ya = 3
xb = 4
yb = 14.5

def young(xa,ya,xb,yb):
            
    print('Para este programa se necesitan los valores xa(Este a),ya(Norte a),xb(Este b),yb (Este b),α,β')
    print("Ingrese el valor de α")
    alfa = angulos()
    print("Ingrese el valor de β (Angulo a corregir)")
    beta = angulos()

    cota = (sp.cot(alfa))
    cotb = (sp.cot(beta))

    #calculando coordenadas del punto desconocido
    a = (xa*cotb) + (xb*cota) + (yb - ya)
    b = cota + cotb
    xp = a/b # El valor Este del parametro aproximado

    c = (ya*cotb) + (yb*cota) + (xa - xb)
    d = cota + cotb
    yp = c/d #El valor Norte del parametro aproximado  

    print(f"El valor Este del parametro aproximado es: {xp}")
    print(f"El valor Norte del parametro aproximado es: {yp}")

def angulos():
    grados = float(input("Grados: "))
    min = float(input("Minutos: "))
    seg = float(input("Segundos: "))
    decimal = grados + (min/60) + (seg/3600)

    return decimal 

young(xa,ya,xb,yb)