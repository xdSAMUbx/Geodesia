import math

def valores_iniciales():
    
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
        
    print("Ingrese la latitud Geodésica del punto a, en el siguiente orden:")
    gra_lat_a = float(input("Grados: "))
    min_lat_a = float(input("Minutos: "))
    seg_lat_a = float(input("Segundos: "))
    lat_geo_a = gra_lat_a+(min_lat_a/60)+(seg_lat_a/3600)
    h_a = float(input("Ingrese la altura del punto a: "))
    print("Ingrese el azimut del punto a, en el siguiente orden:")
    gra_az_a = float(input("Grados: "))
    min_az_a = float(input("Minutos: "))
    seg_az_a = float(input("Segundos: "))
    az_ab = gra_az_a+(min_az_a/60)+(seg_az_a/3600)
    
    print("Ingrese la latitud Geodésica del punto b, en el siguiente orden:")
    gra_lat_b = float(input("Grados: "))
    min_lat_b = float(input("Minutos: "))
    seg_lat_b = float(input("Segundos: "))
    lat_geo_b = gra_lat_b+(min_lat_b/60)+(seg_lat_b/3600)
    h_b = float(input("Ingrese la altura del punto b: "))
    print("Ingrese el azimut del punto b, en el siguiente orden:")
    gra_az_b = float(input("Grados: "))
    min_az_b = float(input("Minutos: "))
    seg_az_b = float(input("Segundos: "))
    az_ba = gra_az_b+(min_az_b/60)+(seg_az_b/3600)
    s_1 = float(input("Ingrese la distancia medida (S1): "))
        
    return lat_geo_a,lat_geo_b,h_a,h_b,az_ab,az_ba,a,e_cuadrado,s_1

def calculo(lat_geo_a,lat_geo_b,h_a,h_b,az_ab,az_ba,a,e_cuadrado,s_1):
    
    sen_ab = math.sin(math.radians(az_ab))
    sen_ba = math.sin(math.radians(az_ba))
    cos_ab = math.cos(math.radians(az_ab))
    cos_ba = math.cos(math.radians(az_ba))
    
    sen_a = math.sin(math.radians(lat_geo_a))
    sen_b = math.sin(math.radians(lat_geo_b))
    
    normal_a = (a/math.sqrt((1-(e_cuadrado*((sen_a)**2)))))
    ro_a = (a*(1-e_cuadrado))/(1-(e_cuadrado*((sen_a)**2)))**(3/2)
    normal_b = (a/math.sqrt((1-(e_cuadrado*((sen_b)**2)))))
    ro_b = (a*(1-e_cuadrado))/(1-(e_cuadrado*((sen_b)**2)))**(3/2)
    
    rad_ab = (normal_a*ro_a)/(((ro_a)*((sen_ab)**2))+((normal_a)*((cos_ab)**2)))
    rad_ba = (normal_b*ro_b)/(((ro_b)*((sen_ba)**2))+((normal_b)*((cos_ba)**2)))
    
    radio = (rad_ab+rad_ba)/2
    
    x = (s_1**2)-(h_b-h_a)**2
    y=(1+(h_a/radio))*(1+(h_b/radio))
    co = math.sqrt(x/y)
    
    s = co + (((co)**3)/((24)*((radio)**2))) + (((co)**5)/((1920)*((radio)**4)))
    
    print(f"La distancia es de: {s}")
    
lat_geo_a,lat_geo_b,h_a,h_b,az_ab,az_ba,a,e_cuadrado,s_1 = valores_iniciales()
calculo(lat_geo_a,lat_geo_b,h_a,h_b,az_ab,az_ba,a,e_cuadrado,s_1)
    