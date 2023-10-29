import math
#Para pasar a MAGNA SIRGAS recordar que se va a usar datos GRS - 80
a = 6378137
e_cuadrado = 0.00669438

def val_ini():
    
    print("Ingrese las coordenadsa geodésicas del punto")
    print("Ingrese la latitud geodésica:")
    gra_lat = float(input("Grados: "))
    min_lat = float(input("Minutos: "))
    seg_lat = float(input("Segundos: "))
    lat_geo = gra_lat + (min_lat/60) + (seg_lat/3600)
    
    print("Ingrese la longitud geodésica: ")
    gra_lon = float(input("Grados: "))
    min_lon = float(input("Minutos: "))
    seg_lon = float(input("Segundos: "))
    lon_geo = gra_lon + (min_lon/60) + (seg_lon/3600)
    
    print("¿Qué origen desea usar?")
    print("1) MAGNA - SIRGAS")
    print("2) Datum BOGOTA")
    origen = int(input("Seleccione el Datum: "))
    
    if origen == 1:
        
        calc_MGNSRGS (lat_geo,lon_geo)
        
    elif origen == 2:
        
        calc_DATBOG (lat_geo,lon_geo)
        
def calc_MGNSRGS (lat_geo,lon_geo):
    pass

def calc_DATBOG (lat_geo,lon_geo):
    pass