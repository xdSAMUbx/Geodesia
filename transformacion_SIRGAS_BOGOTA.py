import math

#Calculo para MAGNA - SIRGAS
def calc_MGNSRGS (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon):
    
    print("Ingrese las coordenadsa geodésicas del punto")
    print("Ingrese la latitud geodésica:")
    gra_lat = float(input("Grados: "))
    min_lat = float(input("Minutos: "))
    seg_lat = float(input("Segundos: "))
    lat_pto = gra_lat + (min_lat/60) + (seg_lat/3600)
    
    print("Ingrese la longitud geodésica (Escribirla negativa porque estamos en el oeste del geoide): ")
    gra_lon = float(input("Grados: "))
    min_lon = float(input("Minutos: "))
    seg_lon = float(input("Segundos: "))
    lon_pto = gra_lon + (min_lon/60) + (seg_lon/3600)
    
    eta_cuad = e_prim_cuad*((math.cos(math.radians(lat_pto)))**2)
    sen_pto = math.sin(math.radians(lat_pto))
    cos_pto = math.cos(math.radians(lat_pto))
    gran_normal = (a/math.sqrt((1-(e_cuadrado*((sen_pto)**2)))))

    if lon_pto <= -72.57750791667 and lon_pto >= -75.57750791667:
        
        #para Bogota (B)
        lat_or = 4.59620041667
        lon_or = -74.0775079667
        
        l = math.radians(lon_pto - lon_or)
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(math.radians(lat_pto)+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(math.radians(lat_or)+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este

        norte = (arc_merid_pto-arc_merid_or)+((t/2)*gran_normal*(l**2)*(cos_pto**2))+((t/24)*gran_normal*(cos_pto**4)*(5-(t**2)+(9*(eta_cuad))+(4*(eta_cuad**2)))*(l**4))+((t/720)*gran_normal*(cos_pto**6)*(61-(58*(t**2))+(t**4)+(270*(eta_cuad))-(330*(t**2)*(eta_cuad)))*(l**6))+((t/40320)*gran_normal*(cos_pto**8)*(1385-(3111*(t**2))+(543*(t**4))-(t**6))*(l**8))+1000000.0
        este = (gran_normal*l*cos_pto)+((1/6)*gran_normal*(cos_pto**3)*(1-(t**2)+(eta_cuad))*(l**3))+((1/120)*gran_normal*(cos_pto**5)*(5-(18*(t**2))+(t**4)+(14*(eta_cuad))-(58*(t**2)*(eta_cuad)))*(l**5))+((1/5040)*gran_normal*(cos_pto**7)*(61-(479*(t**2))+(179*(t**4))-(t**6))*(l**7))+1000000.0
        
        print(f"La coordenada Norte para Bogotá - MAGNA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Bogotá - MAGNA con origen gauss - Krüeger  es: {este}")
        
    elif lon_pto >= -72.57750791667 and lon_pto <= -69.57750791667:
        
        #Para Este Central (EC)
        lat_or = 4.596200416666666
        lon_or = -71.07750791666666
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Este Central - MAGNA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Este Central - MAGNA con origen gauss - Krüeger  es: {este}")
        
    elif lon_pto >= -69.57750791667 and lon_pto <= -66.57750791667:
        
        #Para Este (E)
        lat_or = 4.596200416666666
        lon_or = -68.07750791666666
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Este - MAGNA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Este - MAGNA con origen gauss - Krüeger  es: {este}")
        
    elif lon_pto >= -75.57750791667 and lon_pto <= -78.57750791667:
        
        #Para Oeste
        lat_or = 4.596200416666666
        lon_or = -77.07750791666666
    
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste - MAGNA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste - MAGNA con origen gauss - Krüeger  es: {este}")
        
    elif lon_pto <= -78.57750791667 and lon_pto >= -81.57750791667:
        
        #Para Oeste Oeste
        lat_or = 4.596200416666666
        lon_or = -80.07750791666666
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - MAGNA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - MAGNA con origen gauss - Krüeger es: {este}")
    
    else:
        
        print("No estas usando coordenadas en la dentro de la zona de Colombia")
        
#CALCULO PARA DATUM - BOGOTA
def calc_DATBOG (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon):
    
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
    
    eta = e_prim_cuad*((math.cos(math.radians(lat_pto))**2))
    sen_pto = math.sin(math.radians(lat_pto))
    gran_normal = (a/math.sqrt((1-(e_cuadrado*((sen_pto)**2)))))
    
    if lon_pto >= 72.58091667 and lon_pto <= 75.58091667:
        
        #para Bogota (B)
        lat_or = 4.599047222222222
        lon_or = 74.08091666666667
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger es: {este}")
        
    elif lon_pto <= 72.58091667 and lon_pto >= 69.58091667:
        
        #Para Este Central (EC)
        lat_or = 4.599047222222222
        lon_or = 71.08091666666667
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger es: {este}")
        
    elif lon_pto <= 69.58091667 and lon_pto >= 66.58091667:
        
        #Para Este (E)
        lat_or = 4.599047222222222
        lon_or = 68.08091666666667
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger es: {este}")
        
    elif lon_pto >= 75.58091667 and lon_pto <= 78.58091667:
        
        #Para Oeste
        lat_or = 4.599047222222222
        lon_or = 77.08091666666667
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger es: {este}")
        
    elif lon_pto >= 78.58091667 and lon_pto <= 81.58091667:
        
        #Para Oeste Oeste
        lat_or = 4.599047222222222
        lon_or = 80.08091666666667
        
        l = lon_pto - lon_or
        t = math.tan(math.radians(lat_pto))
        arc_merid_pto = alfa*(lat_pto+beta*(math.sin(2*math.radians(lat_pto)))+gamma*(math.sin(4*math.radians(lat_pto)))+delta*(math.sin(6*math.radians(lat_pto)))+epsilon*(math.sin(8*math.radians(lat_pto))))
        arc_merid_or = alfa*(lat_or+beta*(math.sin(2*math.radians(lat_or)))+gamma*(math.sin(4*math.radians(lat_or)))+delta*(math.sin(6*math.radians(lat_or)))+epsilon*(math.sin(8*math.radians(lat_or))))
        
        #Coordenadas Norte y Este
        norte = (arc_merid_or-arc_merid_pto)+((t/2)*gran_normal*(l**2)*((math.cos(math.radians(lat_pto)))**2))+((t/24)*gran_normal*(l**4)*((math.cos(math.radians(lat_pto)))**4)*(5-(t**2)+9*(eta**2)+4*(eta**4)))+((t/720)*gran_normal*(l**6)*((math.cos(math.radians(lat_pto)))**6)*(61-58*(t**2)+t**4+270*(eta**2)-330*(t**2)*(eta**2)))+((t/40320)*gran_normal*(l**8)*((math.cos(math.radians(lat_pto)))**8)*(1385-3111*(t**2)+543*(t**4)-(t**6)))+1000000.0
        este = (gran_normal*l*(math.cos(math.radians(lat_pto))))+(1/6*gran_normal*(l**3)*((math.cos(math.radians(lat_pto)))**3)*(1-t**2+eta**2))+(1/120*gran_normal*(l**5)*((math.cos(math.radians(lat_pto)))**5)*(5-18*(t**2)+t**4+14*(eta**2)-58*(t**2)*(eta**2)))+(1/5040*gran_normal*(l**7)*((math.cos(math.radians(lat_pto)))**7)*(61-479*(t**2)+179*(t**4)-t**6))+1000000.0
        
        print(f"La coordenada Norte para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger  es: {norte}")
        print(f"La coordenada Este para Oeste Oeste - DATUM BOGOTA con origen gauss - Krüeger es: {este}")
        
    else:
        
        print("No estas usando coordenadas en la dentro de la zona de Colombia")
    
def const_ref ():
    print("¿Que elipsoide va a trabajar como inicial?")
    print("1) Internacional (DATUM - BOGOTA)")
    print("2) GRS - 80 (MAGNA - SIRGAS)")
    elip = int(input("El elipsoide que desea trabajar es: "))
    
    if elip == 1:
        
        #Se esta seleccionando Para hacer Datum Bogota
        a = 6378388
        e_cuadrado = 0.00672267
        b = a*math.sqrt(1-e_cuadrado)
        e_prim_cuad = e_cuadrado/(1 - e_cuadrado)
        n = (a-b)/(a+b)
        
        #Calculando constantes que dependen de a,b,n
        alfa = ((a+b)/2)*(1+((1/4)*(n**2))+((1/64)*(n**4)))
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
        e_prim_cuad = e_cuadrado/(1-e_cuadrado)
        n = (a-b) / (a+b)
        
        #Calculando constantes que dependen de a,b,n
        alfa = ((a+b)/2)*(1+((1/4)*(n**2))+((1/64)*(n**4)))
        beta = (-3/2*(n))+(9/16*(n**3))+(-3/32*(n**5))
        gamma = (15/16*(n**2))+(-15/32*(n**4))
        delta = (-35/48*(n**3))+(105/256*(n**5))
        epsilon = 315/512*(n**4)
        
        calc_MGNSRGS (a,e_cuadrado,b,e_prim_cuad,alfa,beta,gamma,delta,epsilon)
    else:
        print("Error")
        
const_ref()