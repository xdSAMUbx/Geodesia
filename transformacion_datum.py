import math

def calculo_coords_viejas ():
    
    print("¿Que elipsoide va a trabajar como inicial?")
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
    
    print("Ingrese la latitud Geodesica del punto (si es negativa, no importa): ")
    grad_lat = float(input("Grados: "))
    min_lat = float(input("Minutos: "))
    seg_lat = float(input("Segundos: "))
    lat_geo = grad_lat + (min_lat/60) + (seg_lat/3600)
    
    print("Ingrese la longitud Geodésica del punto 1, en el siguiente orden:")
    gra_lon = float(input("Grados: "))
    min_lon = float(input("Minutos: "))
    seg_lon = float(input("Segundos: "))
    lon_geo = gra_lon + (min_lon/60) + (seg_lon/3600)
    
    h = float(input("Ingrese la altura: "))
    coseno_angulo_geodesic = math.cos(math.radians(lat_geo))
    coseno_angulo_long = math.cos(math.radians(lon_geo))
    seno_angulo_geodesic = math.sin(math.radians(lat_geo))
    seno_angulo_long = math.sin(math.radians(lon_geo))
    gran_normal = a/(1-(e_cuadrado*((seno_angulo_geodesic)**2)))
    x = (gran_normal+h)*coseno_angulo_geodesic*coseno_angulo_long
    y = (gran_normal+h)*coseno_angulo_geodesic*seno_angulo_long
    z = (gran_normal*(1-e_cuadrado)+h)*seno_angulo_geodesic 
    
    print(f"La coordenada es: {x},{y},{z}")
    
    return x,y,z,lat_geo,lon_geo
    
def transformacion (x,y,z,lat_geo,lon_geo):  
    #los deltas estan en metros y las rotaciones en radianes  
    if lat_geo >= 10.0 and lat_geo <= 13.0 and lon_geo >= 73.0 and lon_geo <= 71.0:
    # region1  
    
        deltax = -806.413
        deltay = -263.500
        deltaz = -622.671
        deltaL = -2.081616e-5
        rot_x = 6.018583e-5
        rot_y = -1.450001e-5
        rot_z = -1.892455e-4
        
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= 9.4 and lat_geo <= 11.6 and lon_geo <= 76.0 and lon_geo >= 73.0:
    # region2
    
        deltax = 100.783
        deltay = 187.382
        deltaz = -47.000
        deltaL = -1.356561e-5
        rot_x = -4.471839e-5
        rot_y = 1.175093e-5
        rot_z = -4.027967e-5
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= 8.0 and lat_geo <= 9.4 and lon_geo <= 77.6 and lon_geo >= 74.4:
    # region3
    
        deltax = 336.026
        deltay = 348.565
        deltaz = 252.978
        deltaL = -5.771909e-6
        rot_x = -8.358813e-5
        rot_y = -3.057474e-5
        rot_z = 7.573031e-6
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= 5.0 and lat_geo <= 9.4 and lon_geo <= 74.4 and lon_geo >= 72.0:
    # region4
    
        deltax = 963.273
        deltay = 486.386
        deltaz = 190.997
        deltaL = -1.389914e-5
        rot_x = -7.992171e-5
        rot_y = -8.090696e-6
        rot_z = 1.051699e-4
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= 5.0 and lat_geo <= 8.0 and lon_geo <= 78.0 and lon_geo >= 74.4:
    # region5
    
        deltax = -90.290
        deltay = 247.559
        deltaz = -21.989
        deltaL = 2.181658e-6
        rot_x = -4.216369e-5
        rot_y = -2.030416e-5
        rot_z = -6.209623e-5
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= 3.0 and lat_geo <= 5.0 and lon_geo <= 78.0 and lon_geo >= 74.4:
    # region6
        
        deltax = -0.562
        deltay = 244.299
        deltaz = -456.938
        deltaL = 3.746560e-6
        rot_x = 3.329153e-5
        rot_y = -4.001009e-5
        rot_z = -4.507206e-5
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif lat_geo >= -1.0 and lat_geo <= 3.0 and lon_geo <= 79.0 and lon_geo >= 74.0:
    # region7
    
        deltax = -305.356
        deltay = 222.004
        deltaz = -30.023
        deltaL = 6.325747e-6
        rot_x = -4.698084e-5
        rot_y = 5.003123e-6
        rot_z = -9.578655e-5
    
        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    elif ( lat_geo >= -4.5 and lat_geo <= 3.0 and lon_geo <= 74.0 and lon_geo >= 66.5) or (lat_geo >= 3.0 and lat_geo <= 5.0 and lon_geo <= 74.0 and lon_geo >= 66.5) or (lat_geo >= 5.0 and lat_geo <= 7.3 and lon_geo <= 72.0 and lon_geo >= 66.5):
    # region8
    
        deltax = 221.899
        deltay = 274.136
        deltaz = -397.554
        deltaL = -2.199943e-6
        rot_x = 1.361573e-5
        rot_y = -2.174431e-6
        rot_z = -1.362410e-5

        x_trans = deltax + x + rot_z*y - rot_y*z + x*deltaL
        y_trans = deltay + y - rot_z*x + rot_x*z + y*deltaL
        z_trans = deltaz + z +rot_y*x - rot_x*y + z*deltaL
        
        print(f"Las coordenadas en el antigu sistema eran: {x}, {y}, {z}")
        print(f"Las coordenadas del nuevo sistema son: {x_trans}, {y_trans}, {z_trans}")
        
    else:
         
        print("No se puede hacer transformacion de Datum")
        
x,y,z,lat_geo,lon_geo = calculo_coords_viejas ()
transformacion(x,y,z,lat_geo,lon_geo)