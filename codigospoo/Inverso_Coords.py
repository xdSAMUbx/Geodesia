import math

class Inverso_Coords:
    
    def __init__(self):
        
        self.coord_x = 0
        self.coord_y = 0
        self.coord_z = 0
        self.lon1_decimal = 0
        self.lat1_decimal = 0
        self.e_cuad = 0
        self.N = 0
        self.a = 0
        self.h = 0
        self.gra_fi_2 = 0
        self.min_fi_2 = 0
        self.seg_fi_2 = 0
        
        
    def calc_fi (self):
        
        #calculo 1
        self.lat1_decimal = math.atan ((1/1-self.e_cuad)*(self.coord_z/(math.sqrt(self.coord_x**2+self.coord_y**2))))
        self.lat1_decimal  = math.degrees(self.lat1_decimal)
        gra_fi = int(self.lat1_decimal )
        min_fi = int((self.lat1_decimal  - gra_fi) * 60)
        seg_fi = (self.lat1_decimal  - gra_fi - min_fi / 60) * 3600
        seg_fi = round(seg_fi,4)
            
        if seg_fi > 60:
            min_fi += 1
            seg_fi -= 60
            if min_fi > 60:
                gra_fi += 1
                min_fi -=60
    
        self.lat1_decimal  = gra_fi + (min_fi/60) + (seg_fi /3600)
        sen_fi = math.sin(math.radians(self.lat1_decimal ))
        cos_fi = math.cos(math.radians(self.lat1_decimal ))
        self.N = (self.a/math.sqrt((1-(self.e_cuad*((sen_fi)**2)))))    
        self.h = ((math.sqrt(self.coord_x**2+self.coord_y**2))/cos_fi) - self.N
        k = 0
        
        while self.h != 0 and k < 6:
            
            self.lat1_decimal = math.atan((self.coord_z+self.e_cuad*self.N*sen_fi)/(math.sqrt(self.coord_x**2+self.coord_y**2)))
            self.lat1_decimal = math.degrees(self.lat1_decimal)
            self.gra_fi_2 = int(self.lat1_decimal)
            self.min_fi_2 = int((self.lat1_decimal - self.gra_fi_2) * 60)
            self.seg_fi_2 = (self.lat1_decimal - self.gra_fi_2 - self.min_fi_2 / 60) * 3600
            self.seg_fi_2 = round(self.seg_fi_2,4)
                
            if self.seg_fi_2 > 60:
                self.min_fi_2 += 1
                self.seg_fi_2 -= 60
                if self.min_fi_2 > 60:
                    self.gra_fi_2 += 1
                    self.min_fi_2 -=60
            
            self.lat1_decimal = self.gra_fi_2 + (self.min_fi_2/60) + (self.seg_fi_2 /3600)
            sen_fi_2 = math.sin(math.radians(self.lat1_decimal))
            cos_fi_2 = math.cos(math.radians(self.lat1_decimal))
            self.N = (self.a/math.sqrt((1-(self.e_cuad*((sen_fi_2)**2)))))    
            self.h = ((math.sqrt(self.coord_x**2+self.coord_y**2))/cos_fi_2) - self.N
            
            k+=1
    
        print(f"La latitud (φ) del punto es: {self.gra_fi_2}° {self.min_fi_2}' {self.seg_fi_2:.4f}\"  N")
        print(f"La altura final aproximada es de: {self.h} mts")
        
    def calc_lambda(self):
        
        self.lon1_decimal = math.atan (self.coord_y/self.coord_x)
        self.lon1_decimal = math.degrees (self.lon1_decimal)
        
        if self.lon1_decimal < 1:
            self.lon1_decimal = abs(self.lon1_decimal)
            gra_lon = int(self.lon1_decimal)
            min_lon = int((self.lon1_decimal - gra_lon) * 60)
            seg_lon = (self.lon1_decimal - gra_lon - min_lon / 60) * 3600
            seg_lon =round(seg_lon,4)
            
            if seg_lon >= 60:
                min_lon += 1
                seg_lon -= 60
            
                if min_lon >= 60:
                    gra_lon += 1
                    min_lon -=60
                    
            print(f"La longitud(λ) del punto es: {gra_lon}° {min_lon}' {seg_lon:.4f}\" W ")
            
        else:
            
            gra_lon = int(self.lon1_decimal)
            min_lon = int((self.lon1_decimal - gra_lon) * 60)
            seg_lon = (self.lon1_decimal - gra_lon - min_lon / 60) * 3600
            seg_lon =round(seg_lon,4)
            
            if seg_lon > 60:
                min_lon += 1
                seg_lon -= 60
                if min_lon > 60:
                    gra_lon += 1
                    min_lon -=60
                    
            print(f"La longitud(λ) del punto es: {gra_lon}° {min_lon}' {seg_lon:.4f}\" E ")