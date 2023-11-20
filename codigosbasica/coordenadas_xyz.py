import math

def valores():
    
    a = float(input("Ingrese el radio de la elipse: "))
    print(" ¿Con qué información contamos?")
    print(" 1) a, b")
    print(" 2) a, e^2")
    print(" 3) a, f")
    valor_1 = int(input(" Seleccione la informacion que le proporcionaron: "))
    if valor_1 == 1:
        b = float(input("Ingrese b: "))
        e_cuadrado = 1-((b/a)**2) 
    elif valor_1 == 2:
        e_cuadrado = float(input("Ingrese e^2: "))
        print(f"El elipsoide se encuentra definido por a = {a} y e^2 = {e_cuadrado}")
    elif valor_1 == 3:
        f = float(input("Ingrese f en decimal (entre más decimales el resultado va a cambiar): "))
        e_cuadrado = f*(2-f)
    else:
        print("El programa a terminado")
        
    problema(a,e_cuadrado)
    return a,e_cuadrado

def problema (a,e_cuadrado):
    
    print (" 1) Coordenadas Y,Z")
    print (" 2) Coordenadas Y,Z con Altura")    
    print (" 3) Coordenadas X,Y,Z")    
    print (" 4) Coordenadas X,Y,Z con Altura")   
    print (" Oprima 0 para salir de la pantalla" )
    opcion = int(input("Seleccione el problema que desea resolver: ")) 
    if opcion == 1:
        coordenadayz(a,e_cuadrado)
    elif opcion == 2:
        coordenadayzh(a,e_cuadrado)
    elif opcion == 3:
        coordenadaxyz(a,e_cuadrado)
    elif opcion == 4:
        coordenadaxyzh(a,e_cuadrado)
    else:
        print("El programa a terminado")

def coordenadayz(a,e_cuadrado):
    
    print("Ingrese la latitud geodésica en el siguiente orden: ")
    grados = float(input("Ingrese los grados: "))
    minutos = float(input("Ingrese los minutos: "))
    segundos = float(input("Ingrese los segundos: "))
    latitud_geodesica = grados+(minutos/60)+(segundos/3600)
    coseno_angulo = math.cos(math.radians(latitud_geodesica))
    seno_angulo = math.sin(math.radians(latitud_geodesica))
    gran_normal = a/(1-(e_cuadrado*((seno_angulo)**2)))
    y = gran_normal*coseno_angulo
    z = gran_normal*(1-e_cuadrado)*seno_angulo 
    print(f"La coordenada es: {y},{z}")
    
def coordenadayzh(a,e_cuadrado):
    
    print("Ingrese la latitud geodésica en el siguiente orden: ")
    grados = float(input("Ingrese los grados: "))
    minutos = float(input("Ingrese los minutos: "))
    segundos = float(input("Ingrese los segundos: "))
    h = float(input("Ingrese la altura: "))
    latitud_geodesica = grados+(minutos/60)+(segundos/3600)
    coseno_angulo = math.cos(math.radians(latitud_geodesica))
    seno_angulo = math.sin(math.radians(latitud_geodesica))
    gran_normal = a/(1-(e_cuadrado*((seno_angulo)**2)))
    y = (gran_normal+h)*coseno_angulo
    z = (gran_normal*(1-e_cuadrado)+h)*seno_angulo 
    print(f"La coordenada es: {y},{z}")
    
def coordenadaxyz(a,e_cuadrado):
    
    print("Ingrese la latitud geodésica en el siguiente orden: ")
    grados = float(input("Ingrese los grados: "))
    minutos = float(input("Ingrese los minutos: "))
    segundos = float(input("Ingrese los segundos: "))
    print("Ingrese la longitud en el siguiente orden: ")
    grados_long = float(input("Ingrese los grados: "))
    minutos_long = float(input("Ingrese los minutos: "))
    segundos_long = float(input("Ingrese los segundos: "))
    latitud_geodesica = grados+(minutos/60)+(segundos/3600)
    longitud = grados_long+(minutos_long/60)+(segundos_long/3600)
    coseno_angulo_geodesic = math.cos(math.radians(latitud_geodesica))
    coseno_angulo_long = math.cos(math.radians(longitud))
    seno_angulo_geodesic = math.sin(math.radians(latitud_geodesica))
    seno_angulo_long = math.sin(math.radians(longitud))
    gran_normal = a/(1-(e_cuadrado*((seno_angulo_geodesic)**2)))
    x = gran_normal*coseno_angulo_geodesic*coseno_angulo_long
    y = gran_normal*coseno_angulo_geodesic*seno_angulo_long
    z = gran_normal*(1-e_cuadrado)*seno_angulo_geodesic 
    print(f"La coordenada es: {x},{y},{z}")

def coordenadaxyzh(a,e_cuadrado):
    
    print("Ingrese la latitud geodésica en el siguiente orden: ")
    grados = float(input("Ingrese los grados: "))
    minutos = float(input("Ingrese los minutos: "))
    segundos = float(input("Ingrese los segundos: "))
    print("Ingrese la longitud en el siguiente orden: ")
    grados_long = float(input("Ingrese los grados: "))
    minutos_long = float(input("Ingrese los minutos: "))
    segundos_long = float(input("Ingrese los segundos: "))
    latitud_geodesica = grados+(minutos/60)+(segundos/3600)
    longitud = grados_long+(minutos_long/60)+(segundos_long/3600)
    h = float(input("Ingrese la altura: "))
    coseno_angulo_geodesic = math.cos(math.radians(latitud_geodesica))
    coseno_angulo_long = math.cos(math.radians(longitud))
    seno_angulo_geodesic = math.sin(math.radians(latitud_geodesica))
    seno_angulo_long = math.sin(math.radians(longitud))
    gran_normal = a/(1-(e_cuadrado*((seno_angulo_geodesic)**2)))
    x = (gran_normal+h)*coseno_angulo_geodesic*coseno_angulo_long
    y = (gran_normal+h)*coseno_angulo_geodesic*seno_angulo_long
    z = (gran_normal*(1-e_cuadrado)+h)*seno_angulo_geodesic 
    print(f"La coordenada es: {x},{y},{z}")

a,e_cuadrado = valores() 