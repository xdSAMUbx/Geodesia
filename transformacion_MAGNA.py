import math
 
def const_ref ():
    print("¿Que elipsoide va a trabajar como inicial?")
    print("1) Internacional (DATUM - BOGOTA)")
    print("2) GRS - 80 (MAGNA - SIRGAS)")
    elip = int(input("El elipsoide que desea trabajar es:"))
    
    if elip == 1:
        
        #Se esta seleccionando Para hacer Datum Bogota
        a = 6378388
        e_cuadrado = 0.00672267
        b = a*math.sqrt(1-e_cuadrado)
        e_prim_cuad = e_cuadrado/(1/e_cuadrado)
        n = (a-b)/(a+b)
        #Calculando constantes que dependen de a,b,n
        alfa = ((a+b)/2)*(1+(1/4*(n**2))+(1/64*(n**4)))
        beta = (-3/2*(n))+(9/16*(n**3))+(-3/32*(n**5))
        gamma = (15/16*(n**2))+(-15/32*(n**4))
        delta = (-35/48*(n**3))+(105/256*(n**5))
        epsilon = 315/512*(n**4)
        
        calc_DATBOG (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon)
        
    elif elip == 2:
        
        #Se esta seleccionando para hacer MAGNA - SIRGAS
        a = 6378137
        e_cuadrado = 0.00669438
        b = a*math.sqrt(1-e_cuadrado)
        e_prim_cuad = e_cuadrado/(1/e_cuadrado)
        n = (a-b)/(a+b)
        #Calculando constantes que dependen de a,b,n
        alfa = ((a+b)/2)*(1+(1/4*(n**2))+(1/64*(n**4)))
        beta = (-3/2*(n))+(9/16*(n**3))+(-3/32*(n**5))
        gamma = (15/16*(n**2))+(-15/32*(n**4))
        delta = (-35/48*(n**3))+(105/256*(n**5))
        epsilon = 315/512*(n**4)
        
        calc_MGNSRGS (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon)
    else:
        print("Error")

#Calculo para MAGNA - SIRGAS
def calc_MGNSRGS (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon):
    
    print("Ingrese las coordenadsa geodésicas del punto")
    print("Ingrese la latitud geodésica:")
    gra_lat = float(input("Grados: "))
    min_lat = float(input("Minutos: "))
    seg_lat = float(input("Segundos: "))
    lat_pto = gra_lat + (min_lat/60) + (seg_lat/3600)
    
    print("Ingrese la longitud geodésica: ")
    gra_lon = float(input("Grados: "))
    min_lon = float(input("Minutos: "))
    seg_lon = float(input("Segundos: "))
    lon_pto = gra_lon + (min_lon/60) + (seg_lon/3600)

    if lon_pto >= 72.57750791667 and lon_pto <= 75.57750791667:
        #para Bogota (B)
        lat_or = 4.596200416666666
        lon_or = 74.07750791666666
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        eta = e_prim_cuad*((math.cos(math.radians(lat_pto))**2))
        
    elif lon_pto <= 72.57750791667 and lon_pto >= 69.57750791667:
        #Para Este Central (EC)
        lat_or = 4.596200416666666
        lon_or = 71.07750791666666
        
    elif lon_pto <= 69.57750791667 and lon_pto >= 66.57750791667:
        #Para Este (E)
        lat_or = 4.596200416666666
        lon_or = 68.07750791666666
        
    elif lon_pto >= 75.57750791667 and lon_pto <= 78.57750791667:
        #Para Oeste
        lat_or = 4.596200416666666
        lon_or = 77.07750791666666
        
    elif lon_pto >= 78.57750791667 and lon_pto <= 81.57750791667:
        #Para Oeste Oeste
        lat_or = 4.596200416666666
        lon_or = 80.07750791666666
        
#CALCULO PARA DATUM - BOGOTA
def calc_DATBOG (lat_geo,lon_geo):
    pass