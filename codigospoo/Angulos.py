class Angulos:
    
    def __init__(self):
        
        self.decimal = 0
        self.grados = 0
        self.min = 0
        self.seg = 0
        
    def ang_decimales (self):
        
        print("Ingrese el angulo en el siguiente orden(Si es oeste, escribir todos los angulos en negativo): ")
        grados = float(input("Grados: "))
        min = float(input("Minutos: "))
        seg = float(input("Segundos: "))
        self.decimal = grados + (min/60) + (seg/3600)
        print("¿ Es Norte/Este O Sur/Oeste ?")
        print("1) Norte o Este")
        print("2) Sur u Oeste")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            self.decimal = self.decimal
        elif opcion == 2:
            self.decimal = 360 - self.decimal
    
    def ang_sexagesimales():
        pass