import math

def val_ini ():
    
    print("Digite el elipsoide con el que desea trabajar")
    print("1) Internacional (DATUM - BOGOTA)")
    print("2) GRS - 80 (MAGNA - SIRGAS)")
    elip = int(input("El elipsoide que desea trabajar es: "))
    
    if elip == 1:
        
        a = 6378388
        e_cuadrado = 0.00672267
        
        print("Ingrese la Latitud Geodésica del Punto de Origen, en el siguiente orden:")
        graOr = float(input("Grados: "))
        minOr = float(input("Minutos: "))
        segOr = float(input("Segundos: "))
        latOr = graOr+(minOr/60)+(segOr/3600)
        print("Ingrese la Longitud Geodésica del Punto de Origen, en el siguiente orden:")
        graLonOr = float(input("Grados: "))
        minLonOr = float(input("Minutos: "))
        segLonOr = float(input("Segundos: "))
        lonOr = -(graLonOr+(minLonOr/60)+(segLonOr/3600))
        
        norte1 = float(input("Ingrese la Norte asignada al Origen: "))
        este1 = float(input("Ingrese la Este asignada al Origen: "))
        hpp = float(input("Ingrese la altura del plano de proyección: "))
    
        calc_coord(a,e_cuadrado,latOr,lonOr,norte1,este1,hpp)
        
    elif elip == 2:
        
        a = 6378137
        e_cuadrado = 0.00669438
        
        print("Ingrese la Latitud Geodésica del Punto de Origen, en el siguiente orden:")
        graOr = float(input("Grados: "))
        minOr = float(input("Minutos: "))
        segOr = float(input("Segundos: "))
        latOr = graOr+(minOr/60)+(segOr/3600)
        print("Ingrese la Longitud Geodésica del Punto de Origen, en el siguiente orden:")
        graLonOr = float(input("Grados: "))
        minLonOr = float(input("Minutos: "))
        segLonOr = float(input("Segundos: "))
        lonOr = -(graLonOr+(minLonOr/60)+(segLonOr/3600))
        
        norte1 = float(input("Ingrese la Norte asignada al Origen: "))
        este1 = float(input("Ingrese la Este asignada al Origen: "))
        hpp = float(input("Ingrese la altura del plano de proyección: "))
        
        calc_coord(a,e_cuadrado,latOr,lonOr,norte1,este1,hpp)
        
    else:
        
        print("Error")
        
def calc_coord(a,e_cuadrado,latOr,lonOr,norte1,este1,hpp):

    #Latitud Del punto
    print("Ingrese la Latitud Geodésica del Punto, en el siguiente orden:")
    gra = float(input("Grados: "))
    min = float(input("Minutos: "))
    seg = float(input("Segundos: "))
    lat = gra+(min/60)+(seg/3600)
    print("Ingrese la Longitud Geodésica del Punto, en el siguiente orden:")
    graLon = float(input("Grados: "))
    minLon = float(input("Minutos: "))
    segLon = float(input("Segundos: "))
    lon = -(graLon+(minLon/60)+(segLon/3600))
    
    #Proceso para la coordenada
    senSeg = math.sin(math.radians(1/3600))
    senPto = math.sin(math.radians(lat))
    cosPto = math.cos(math.radians(lat))
    tanPto = math.tan(math.radians(lat))
    N = (a/math.sqrt((1-(e_cuadrado*((senPto)**2)))))
    ro = (a*(1-e_cuadrado))/(1-(e_cuadrado*((senPto)**2)))**(3/2)
    K_n = (1+(hpp/ro))
    K_e = (1+(hpp/N))
    
    #Constantes
    A = 1/(N*senSeg)
    B = 1/(ro*senSeg)
    C = (tanPto/(2*ro*N*senSeg))
    
    #Diferencias
    dif_lat = (lat - latOr)*3600
    dif_lon = (lon - lonOr)*3600
    dif_E = (dif_lon*cosPto*K_e)/A
    dif_N = ((dif_lat+(C*(dif_E**2)))*K_n)/B
    
    este = este1 + dif_E
    norte = norte1 + dif_N
    
    print("La coordenada cartesiana para el punto de Origen y el punto seleccionado es: ")
    print(f"N = {norte}")
    print(f"E = {este}")
    
val_ini()    