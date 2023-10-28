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

def calc_fi (x,y,z,e_cuadrado,a):
    #calculo iteraciones (manuales #1)
    fi = math.atan ((1/1-e_cuadrado)*(z/(math.sqrt(x**2+y**2))))
    fi = math.degrees(fi)
    gra_fi = int(fi)
    min_fi = int((fi - gra_fi) * 60)
    seg_fi = (fi - gra_fi - min_fi / 60) * 3600
    seg_fi = round(seg_fi,4)
        
    if seg_fi > 60:
        min_fi += 1
        seg_fi -= 60
        if min_fi > 60:
            gra_fi += 1
            min_fi -=60
    
    fi = gra_fi + (min_fi/60) + (seg_fi /3600)
    sen_fi = math.sin(math.radians(fi))
    cos_fi = math.cos(math.radians(fi))
    gran_normal = (a/math.sqrt((1-(e_cuadrado*((sen_fi)**2)))))    
    h = ((math.sqrt(x**2+y**2))/cos_fi) - gran_normal

    #calculo iteraciones (manuales #2)
    fi_2 = math.atan((z+e_cuadrado*gran_normal*sen_fi)/(math.sqrt(x**2+y**2)))
    fi_2 = math.degrees(fi_2)
    gra_fi_2 = int(fi_2)
    min_fi_2 = int((fi_2 - gra_fi_2) * 60)
    seg_fi_2 = (fi_2 - gra_fi_2 - min_fi_2 / 60) * 3600
    seg_fi_2 = round(seg_fi_2,4)
        
    if seg_fi_2 > 60:
        min_fi_2 += 1
        seg_fi_2 -= 60
        if min_fi_2 > 60:
            gra_fi_2 += 1
            min_fi_2 -=60
    
    fi_2 = gra_fi_2 + (min_fi_2/60) + (seg_fi_2 /3600)
    sen_fi_2 = math.sin(math.radians(fi_2))
    cos_fi_2 = math.cos(math.radians(fi_2))
    gran_normal_2 = (a/math.sqrt((1-(e_cuadrado*((sen_fi_2)**2)))))    
    h_2 = ((math.sqrt(x**2+y**2))/cos_fi_2) - gran_normal_2

    
    #calculo iteraciones (manuales #3)
    fi_3 = math.atan((z+e_cuadrado*gran_normal_2*sen_fi_2)/(math.sqrt(x**2+y**2)))
    fi_3 = math.degrees(fi_3)
    gra_fi_3 = int(fi_3)
    min_fi_3 = int((fi_3 - gra_fi_3) * 60)
    seg_fi_3 = (fi_3 - gra_fi_3 - min_fi_3 / 60) * 3600
    seg_fi_3 = round(seg_fi_3,4)
        
    if seg_fi_3 > 60:
        min_fi_3 += 1
        seg_fi_3 -= 60
        if min_fi_3 > 60:
            gra_fi_3 += 1
            min_fi_3 -=60
    
    fi_3 = gra_fi_3 + (min_fi_3/60) + (seg_fi_3/3600)
    sen_fi_3 = math.sin(math.radians(fi_3))
    cos_fi_3 = math.cos(math.radians(fi_3))
    gran_normal_3 = (a/math.sqrt((1-(e_cuadrado*((sen_fi_3)**2)))))    
    h_3 = ((math.sqrt(x**2+y**2))/cos_fi_3) - gran_normal_3
    
    #calculo iteraciones (manuales #4)
    fi_4 = math.atan((z+e_cuadrado*gran_normal_3*sen_fi_3)/(math.sqrt(x**2+y**2)))
    fi_4 = math.degrees(fi_4)
    gra_fi_4 = int(fi_4)
    min_fi_4 = int((fi_4 - gra_fi_4) * 60)
    seg_fi_4 = (fi_4 - gra_fi_4 - min_fi_4 / 60) * 3600
    seg_fi_4 = round(seg_fi_4,4)
        
    if seg_fi_4 > 60:
        min_fi_4 += 1
        seg_fi_4 -= 60
        if min_fi_4 > 60:
            gra_fi_4 += 1
            min_fi_4 -=60
    
    fi_4 = gra_fi_4 + (min_fi_4/60) + (seg_fi_4/3600)
    sen_fi_4 = math.sin(math.radians(fi_4))
    cos_fi_4 = math.cos(math.radians(fi_4))
    gran_normal_4 = (a/math.sqrt((1-(e_cuadrado*((sen_fi_4)**2)))))    
    h_4 = ((math.sqrt(x**2+y**2))/cos_fi_4) - gran_normal_4
    
    #calculo iteraciones (manuales #5)
    fi_5 = math.degrees(math.atan((z+e_cuadrado*gran_normal_4*sen_fi_4)/(math.sqrt(x**2+y**2))))
    gra_fi_5 = int(fi_5)
    min_fi_5 = int((fi_5 - gra_fi_5) * 60)
    seg_fi_5 = (fi_5 - gra_fi_5 - min_fi_5 / 60) * 3600
    seg_fi_5 = round(seg_fi_5,4)
        
    if seg_fi_5 > 60:
        min_fi_5 += 1
        seg_fi_5 -= 60
        if min_fi_5 > 60:
            gra_fi_5 += 1
            min_fi_5 -=60
    
    fi_5 = gra_fi_5 + (min_fi_5/60) + (seg_fi_5/3600)
    sen_fi_5 = math.sin(math.radians(fi_5))
    cos_fi_5 = math.cos(math.radians(fi_5))
    gran_normal_5 = (a/math.sqrt((1-(e_cuadrado*((sen_fi_5)**2)))))    
    h_5 = ((math.sqrt(x**2+y**2))/cos_fi_5) - gran_normal_5
    
    print(f"La latitud final (φ) aproximada del punto es: {gra_fi_5}° {min_fi_5}' {seg_fi_5:.4f}\" E ")
    print(f"La altura final aproximada es de: {h_5} mts")
        
a,e_cuadrado,x,y,z = valores_iniciales()
calc_lambda (x,y)
calc_fi(x,y,z,e_cuadrado,a)
