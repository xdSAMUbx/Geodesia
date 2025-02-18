class Angulos:
    
    def __init__(self):
        
        self.decimal = 0
        self.grados = 0
        self.min = 0
        self.seg = 0
        self.decimal = 0
        
    def grad (self):
        
        self.grados = float(input("Grados: "))
        self.min = float(input("Minutos: "))
        self.seg = float(input("Segundos: "))
        self.decimal = self.grados + (self.min/60) + (self.seg/3600)
