import math

class Inverso_Coords:
    
    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.lon1_decimal = 0
        self.fi1 = 0 
        self.fi2 = 0
        self.e_cuad = 0
        self.N = 0
        self.a = 0
        self.h = 0        
        
    def calc_fi (self):
        
        self.fi1 = math.degrees(math.atan ((1/1-self.e_cuad)*(self.z/(math.sqrt(self.x**2+self.y**2)))))
        if self.fi1 > 360:
            self.fi = self.fi1 - 360
        elif self.fi1 < 1:
            self.fi1 = 360 + self.fi1
        sin_fi1 = math.sin(math.radians(self.fi1))
        cos_fi1 = math.cos(math.radians(self.fi1))
        self.N = (self.a/math.sqrt((1-(self.e_cuad*((sin_fi1)**2))))) 
        self.h = ((math.sqrt(self.x**2+self.y**2))/cos_fi1) - self.N
        k = 0
        
        while k<7 and self.h != 0:
            
            if k == 0:
                self.fi2 = math.degrees(math.atan((self.z+self.e_cuad*self.N*sin_fi1)/(math.sqrt(self.x**2+self.y**2))))
            else:
                self.fi2 = math.degrees(math.atan((self.z+self.e_cuad*self.N*sin_fi2)/(math.sqrt(self.x**2+self.y**2))))
            
            if self.fi2 > 360:
                self.fi2 = self.fi2 - 360
            elif self.fi2 < 0:
                self.fi2 = 360 + self.fi2
            sin_fi2 = math.sin(math.radians(self.fi2))
            cos_fi2 = math.cos(math.radians(self.fi2))
            self.N = (self.a/math.sqrt((1-(self.e_cuad*((sin_fi2)**2))))) 
            self.h = ((math.sqrt(self.x**2+self.y**2))/cos_fi2) - self.N
            k += 1
            
        gra_fi_2 = int(self.fi2)
        min_fi_2 = int((self.fi2 - gra_fi_2) * 60)
        seg_fi_2 = (self.fi2 - gra_fi_2 - min_fi_2 / 60) * 3600
        seg_fi_2 = round(seg_fi_2,4)
            
        if seg_fi_2 > 60:
            min_fi_2 += 1
            seg_fi_2 -= 60
            if min_fi_2 > 60:
                gra_fi_2 += 1
                min_fi_2 -=60
        
        print(f"La latitud final (φ) aproximada del punto es: {gra_fi_2}° {min_fi_2}' {seg_fi_2:.4f}\" N")
        print(f"La altura final aproximada es de: {self.h} mts")
            
    def calc_lambda(self):
        
        self.lon1_decimal = math.atan (self.y/self.x)
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