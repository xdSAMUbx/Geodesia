import math

def problema_directo(a,e_cuadrado):
    
    #Latitudes Geodesicas
    print("Ingrese la latitud Geodésica del punto 1, en el siguiente orden:")
    gra_lat_geo1 = float(input("Ingrese los Grados: "))
    min_lat_geo1 = float(input("Ingrese los Minutos: "))
    seg_lat_geo1 = float(input("Ingrese los Segundos: "))
    latgeo1 = gra_lat_geo1+(min_lat_geo1/60)+(seg_lat_geo1/3600)
    
    print("Ingrese la longitud Geodésica del punto 1, en el siguiente orden:")
    gra_lon_geo1 = float(input("Ingrese los Grados: "))
    min_lon_geo1 = float(input("Ingrese los Minutos: "))
    seg_lon_geo1 = float(input("Ingrese los Segundos: "))
    longeo1 = gra_lon_geo1+(min_lon_geo1/60)+(seg_lon_geo1/3600)
    print("La longitud esta hacia el Este (E) u Oeste (W): ")
    print("1) Este")
    print("2) Oeste")
    longitud = int(input("Ingrese la dirección de la longitud: "))
    if longitud == 1:
        longeo1 = longeo1
    elif longitud == 2:
        longeo1 = 360-longeo1
    else:
        print("Error, inicie de nuevo")
        
    print("Ingrese el azimut del punto 1 al 2, en el siguiente orden:")
    gra_az_12 = float(input("Ingrese los Grados: "))
    min_az_12 = float(input("Ingrese los Minutos: "))
    seg_az_12 = float(input("Ingrese los Segundos: "))
    az_12 = gra_az_12+(min_az_12/60)+(seg_az_12/3600)
    
    s = float(input("Ingrese la distancia: "))
    
    #Senos y cosenos del angulo fi_1 y azimut_12
    coseno_angulo1 = math.cos(math.radians(latgeo1))
    coseno_az_12 = math.cos(math.radians(az_12))
    seno_angulo1 = math.sin(math.radians(latgeo1))
    seno_az_12 = math.sin(math.radians(az_12))#se cambio cos por sen
    gran_normal_1 = (a/math.sqrt((1-(e_cuadrado*((seno_angulo1)**2)))))
    arco_seg = math.sin(math.radians(1/3600))
    ro1 = (a*(1-e_cuadrado))/(1-(e_cuadrado*((seno_angulo1)**2)))**(3/2)
    
    #Definiendo las constantes
    B = 1/(ro1*arco_seg)
    C = (((seno_angulo1/coseno_angulo1))/(2*(ro1*gran_normal_1*arco_seg)))
    D = (3*e_cuadrado*seno_angulo1*coseno_angulo1*arco_seg)/(2*(1-(e_cuadrado*((seno_angulo1)**2))))
    E = (1+(3*((seno_angulo1/coseno_angulo1)**2)))/(6*(gran_normal_1**2))
    
    #Hallar latitud geodesica punto 2
    delta_fi = (B*s*coseno_az_12)-(C*(s**2)*((seno_az_12)**2))-(B*E*(s**2)*coseno_az_12*((seno_az_12)**2))
    correccion = (D*(delta_fi**2))
    diferencia_fi = (B*s*coseno_az_12)-(C*(s**2)*((seno_az_12)**2))-(B*E*(s**2)*coseno_az_12*((seno_az_12)**2))-correccion
    diferencia_fi = diferencia_fi/3600
    fi_2 = latgeo1 + diferencia_fi
    gra_lat_geo2 = int(fi_2)
    min_lat_geo2 = int((fi_2 - gra_lat_geo2) * 60)
    seg_lat_geo2 = (fi_2 - gra_lat_geo2 - min_lat_geo2 / 60) * 3600
    print(f"La latitud Geodésica del punto 2 es: {gra_lat_geo2}° {min_lat_geo2}' {seg_lat_geo2:.4f}\"")# la cantidad de decimales despues dl punto

    #Senos y cosenos con la latitud 2
    seno_angulo2 = math.sin(math.radians(fi_2))
    coseno_angulo2 = math.cos(math.radians(fi_2))
    gran_normal_2 = (a/math.sqrt((1-(e_cuadrado*((seno_angulo2)**2)))))
    
    #Hallar longitud punto 2
    seno_s_sobre_n = math.sin(math.radians(s/gran_normal_2))
    delta_lambda = math.degrees(math.asin((seno_s_sobre_n*seno_az_12)*(1/coseno_angulo2)))
    delta_lambda = delta_lambda*(180/math.pi)
    lambda_2 = longeo1 + delta_lambda
    if lambda_2 > 180:
        lambda_2 = 360 - lambda_2
    elif lambda_2 < 180:
        lambda_2 = lambda_2
    else:
        print("Error, algo fallo")
    
    gra_lon_geo2 = int(lambda_2)
    min_lon_geo2 = int((lambda_2 - gra_lon_geo2) * 60)
    seg_lon_geo2 = (lambda_2 - gra_lon_geo2 - min_lon_geo2 / 60) * 3600
    
    print(f"La longitud Geodésica del punto 2 es: {gra_lon_geo2}° {min_lon_geo2}' {seg_lon_geo2:.4f}\"")
    
    #Hallar el azimut 21
    fi_medio = ((fi_2 + latgeo1)/2)
    seno_angulo_medio = math.sin(math.radians(fi_medio))
    coseno_angulo_medio = math.cos(math.radians(fi_medio))
    cos_ang_medsobre2 = math.cos(math.radians(fi_medio/2))
    delta_alfa = (delta_lambda*seno_angulo_medio/cos_ang_medsobre2)+((delta_lambda**3)/12)*(seno_angulo_medio*(coseno_angulo_medio**2)*(arco_seg**2))
    az_21 = az_12 + 180 + delta_alfa
    
    if az_21 > 360:
        az_21 = az_21 - 360
    elif az_21 < 0:
        az_21 = az_21 + 360
        
    gra_az21 = int(az_21)
    min_az21 = int((az_21 - gra_az21) * 60)
    seg_az21 = (az_21 - gra_az21 - min_az21 / 60) * 3600
    
    print(f"El azimut del punto 2 al 1 es: {gra_az21}° {min_az21}' {seg_az21:.4f}\"")

def problema_inverso (a,e_cuadrado):
    
    #Datos punto 1
    print("Ingrese la latitud Geodésica del punto 1, en el siguiente orden:")
    gra_lat_geo1 = float(input("Ingrese los Grados: "))
    min_lat_geo1 = float(input("Ingrese los Minutos: "))
    seg_lat_geo1 = float(input("Ingrese los Segundos: "))
    latgeo1 = gra_lat_geo1+(min_lat_geo1/60)+(seg_lat_geo1/3600)
    
    print("Ingrese la longitud Geodésica del punto 1, en el siguiente orden:")
    gra_lon_geo1 = float(input("Ingrese los Grados: "))
    min_lon_geo1 = float(input("Ingrese los Minutos: "))
    seg_lon_geo1 = float(input("Ingrese los Segundos: "))
    longeo1 = gra_lon_geo1+(min_lon_geo1/60)+(seg_lon_geo1/3600)
    print("La longitud esta hacia el Este (E) u Oeste (W): ")
    print("1) Este")
    print("2) Oeste")
    longitud = int(input("Ingrese la dirección de la longitud: "))
    if longitud == 2:
        longeo1 = 360-longeo1
    
    #Datos punto 2
    print("Ingrese la latitud Geodésica del punto 2, en el siguiente orden:")
    gra_lat_geo2 = float(input("Ingrese los Grados: "))
    min_lat_geo2 = float(input("Ingrese los Minutos: "))
    seg_lat_geo2 = float(input("Ingrese los Segundos: "))
    latgeo2 = gra_lat_geo2+(min_lat_geo2/60)+(seg_lat_geo2/3600)
    
    print("Ingrese la longitud Geodésica del punto 2, en el siguiente orden:")
    gra_lon_geo2 = float(input("Ingrese los Grados: "))
    min_lon_geo2 = float(input("Ingrese los Minutos: "))
    seg_lon_geo2 = float(input("Ingrese los Segundos: "))
    longeo2 = gra_lon_geo2+(min_lon_geo2/60)+(seg_lon_geo2/3600)
    print("La longitud esta hacia el Este (E) u Oeste (W): ")
    print("1) Este")
    print("2) Oeste")
    longitud_2 = int(input("Ingrese la dirección de la longitud: "))
    if longitud_2 == 2:
        longeo2 = 360-longeo2
    
    #Definicion de senos, cosenos y ro1
    coseno_angulo1 = math.cos(math.radians(latgeo1))
    seno_angulo1 = math.sin(math.radians(latgeo1))
    gran_normal_1 = (a/math.sqrt(1-(e_cuadrado*((seno_angulo1)**2))))
    ro1 = (a*(1-e_cuadrado))/(1-(e_cuadrado*((seno_angulo1)**2)))**(3/2)
    seno_angulo2 = math.sin(math.radians(latgeo2))
    coseno_angulo2 = math.cos(math.radians(latgeo2))
    gran_normal_2 = (a/math.sqrt(1-(e_cuadrado*((seno_angulo2)**2))))
    
    #Definicion constantes
    arco_seg = math.sin(math.radians(1/3600))
    B = 1/(ro1*arco_seg)
    C = (((seno_angulo1/coseno_angulo1))/(2*(ro1*gran_normal_1*arco_seg)))
    D = (3*e_cuadrado*seno_angulo1*coseno_angulo1*arco_seg)/(2*(1-(e_cuadrado*((seno_angulo1)**2))))
    E = (1+(3*((seno_angulo1/coseno_angulo1)**2)))/(6*(gran_normal_1**2))

    #Diferencias longitudes
    delta_lambda = longeo2-longeo1
    delta_fi = latgeo2 - latgeo1
    delta_fi = delta_fi*3600
    delta_fi_2 = delta_fi
    sen_dif_lambda = math.sin(math.radians(delta_lambda))
    
    #Definiendo X, Y
    x = gran_normal_2*sen_dif_lambda*coseno_angulo2                                                  
    y = (delta_fi+(C*(x**2))+(D*(delta_fi_2**2)))/(B*(1-E*(x**2)))
    az_12 = math.atan(x/y)
    az_12 = (math.degrees(az_12)) 
    
    if delta_lambda > 0 and delta_fi > 0:
        az_12 = az_12 
    elif delta_lambda > 0 and delta_fi < 0:
        az_12 = az_12 - 180 
    elif delta_lambda < 0 and delta_fi < 0:
        az_12 = 180 + az_12 
    elif delta_lambda < 0 and delta_fi > 0:
        az_12 = 360 - az_12 
        
    if az_12 > 360:
        az_12 = az_12 - 360
    elif az_12 < 0:
        az_12 = az_12 + 360
    
    gra_az12 = int(az_12)
    min_az12 = int((az_12 - gra_az12) * 60)
    seg_az12 = (az_12 - gra_az12 - min_az12 / 60) * 3600
    print(f"El azimut del punto 1 al 2 es: {gra_az12}° {min_az12}' {seg_az12:.4f}\"")
        
    sen_az12 = math.sin(math.radians(az_12))
    s = abs (x/sen_az12)
    print(f"La distancia del punto 1 al 2 es de: {s} mts")
    
    #Azimut 2 a 1
    fi_medio = ((latgeo2 + latgeo1)/2)
    seno_angulo_medio = math.sin(math.radians(fi_medio))
    coseno_angulo_medio = math.cos(math.radians(fi_medio))
    cos_ang_medsobre2 = math.cos(math.radians(delta_fi/7200))
    delta_alfa = ((delta_lambda)*seno_angulo_medio/cos_ang_medsobre2)+(((delta_lambda**3))/12)*(seno_angulo_medio*(coseno_angulo_medio**2)*(arco_seg**2))
    az_21 = az_12 + 180 + delta_alfa
    
    if az_21 > 360:
        az_21 = az_21 - 360
    elif az_21 < 0:
        az_21 = az_21 + 360
        
    gra_az21 = int(az_21)
    min_az21 = int((az_21 - gra_az21) * 60)
    seg_az21 = (az_21 - gra_az21 - min_az21 / 60) * 3600
    
    print(f"El azimut del punto 2 al 1 es: {gra_az21}° {min_az21}' {seg_az21:.4f}\"")

def calculo_problema():

    print("Ingrese el Elipsoide en el cual desea resolver el problema: ")
    print("1) Internacional ")
    print("2) GRS - 80")
    elipsoide = int(input("Seleccione el elipsoide: "))
    if elipsoide == 1:
        a = 6378388
        e_cuadrado = 0.00672267
    elif elipsoide == 2:
        a = 6378137
        e_cuadrado = 0.00669438
    else:
        print("Error, vuelva a iniciar")
    print("¿Qué problema desea resolver? ")
    print("1) Problema Directo")
    print("2) Problema Inverso")
    num_problem = int(input("Digite la opción que necesita: "))
    if num_problem == 1:
        problema_directo(a,e_cuadrado)
    elif num_problem == 2:
        problema_inverso(a,e_cuadrado)
    else:
        print("Error, inicie de nuevo")
    
calculo_problema()