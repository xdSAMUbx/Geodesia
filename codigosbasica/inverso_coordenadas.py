import math
#valores iniciales
def valores_iniciales():
    print("Digite las coordenadas x,y,z")
    x = float(input("Coordenada x: "))
    y = float(input("Coordenada y: "))
    z = float(input("Coordenada z: "))
    
    print("¿Que elipsoide va a trabajar?")
    print("1) Internacional")
    print("2) GRS - 80")
    elip = int(input("El elipsoide que desea trabajar es:"))
    if elip == 1:
        a = 6378388
        e_cuadrado = 0.00672267
    elif elip == 2:
        a = 6378137
        e_cuadrado = 0.00669438
    else:
        print("Error")
        
    return a,e_cuadrado,x,y,z

#calculadora de lambda o longitud
def calc_lambda(x,y):
    
    lon = math.atan (y/x)
    lon = math.degrees (lon)
    
    if lon < 1:
        lon = abs(lon)
        gra_lon = int(lon)
        min_lon = int((lon - gra_lon) * 60)
        seg_lon = (lon - gra_lon - min_lon / 60) * 3600
        seg_lon =round(seg_lon,4)
        
        if seg_lon >= 60:
            min_lon += 1
            seg_lon -= 60
        
            if min_lon >= 60:
                gra_lon += 1
                min_lon -=60
                
        print(f"La longitud(λ) del punto es: {gra_lon}° {min_lon}' {seg_lon:.4f}\" W ")
        
    else:
        
        gra_lon = int(lon)
        min_lon = int((lon - gra_lon) * 60)
        seg_lon = (lon - gra_lon - min_lon / 60) * 3600
        seg_lon =round(seg_lon,4)
        
        if seg_lon > 60:
            min_lon += 1
            seg_lon -= 60
            if min_lon > 60:
                gra_lon += 1
                min_lon -=60
                
        print(f"La longitud(λ) del punto es: {gra_lon}° {min_lon}' {seg_lon:.4f}\" E ")
        
    return lon

import math

def calcular_latitud_altura(x, y, z, e_cuadrado, a):
    # Inicializar variables para la primera iteración
    fi_anterior = None
    h_anterior = None

    # Número de iteraciones
    num_iteraciones = 5

    for _ in range(num_iteraciones):
        if fi_anterior is None:
            fi = math.atan((1 / (1 - e_cuadrado)) * (z / (math.sqrt(x**2 + y**2))))
        else:
            fi = math.atan((z + e_cuadrado * gran_normal * sen_fi) / (math.sqrt(x**2 + y**2)))

        # Calcular variables auxiliares
        fi = math.degrees(fi)
        gra_fi = int(fi)
        min_fi = int((fi - gra_fi) * 60)
        seg_fi = (fi - gra_fi - min_fi / 60) * 3600
        seg_fi = round(seg_fi, 4)

        # Ajustar valores si es necesario
        if seg_fi > 60:
            min_fi += 1
            seg_fi -= 60
            if min_fi > 60:
                gra_fi += 1
                min_fi -= 60

        fi = gra_fi + (min_fi / 60) + (seg_fi / 3600)

        sen_fi = math.sin(math.radians(fi))
        cos_fi = math.cos(math.radians(fi))
        gran_normal = (a / math.sqrt((1 - (e_cuadrado * ((sen_fi)**2)))))
        h = ((math.sqrt(x**2 + y**2)) / cos_fi) - gran_normal

        # Almacenar valores para la siguiente iteración
        fi_anterior = fi
        h_anterior = h

    print(f"La latitud final (φ) aproximada del punto es: {gra_fi}° {min_fi}' {seg_fi:.4f}\" N")
    print(f"La altura final aproximada es de: {h} mts")
a,e_cuadrado,x,y,z = valores_iniciales()
calc_lambda (x,y)
calcular_latitud_altura(x,y,z,e_cuadrado,a)
