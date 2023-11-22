class Angulos:
    
    def __init__(self):
        
        self.decimal = 0
        self.grados = 0
        self.min = 0
        self.seg = 0
        
    def ang_decimales (self):
        
        print("Ingrese el angulo en el siguiente orden: ")
        grados = float(input("Grados: "))
        min = float(input("Minutos: "))
        seg = float(input("Segundos: "))
        
        self.decimal = grados+(min/60)+(seg/3600)
        if self.decimal < 1:
            self.decimal = 360 + self.decimal
    
    def ang_sexagesimales():
        pass