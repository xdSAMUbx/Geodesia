class Angulos:
    
    def __init__(self):
        
        self.decimal = 0
        self.grados = 0
        self.min = 0
        self.seg = 0
        self.decimallon = 0
        
    def lat (self):
        
        print("Ingrese la latitud (φ) del punto: ")
        self.grados = float(input("Grados: "))
        self.min = float(input("Minutos: "))
        self.seg = float(input("Segundos: "))
        self.decimal = self.grados + (self.min/60) + (self.seg/3600)

    def lon(self):

        print("Ingrese la longitud (λ) del punto: ")
        self.gradlon = float(input("Grados: "))
        self.minlon = float(input("Minutos: "))
        self.seglon = float(input("Segundos: "))
        self.decimallon = self.gradlon + (self.minlon/60) + (self.seglon/3600)
        opcion2 = int(input("El angulo esta al este u oeste? (1 = E, 2 = W): "))
        if opcion2 == 1:
                self.decimallon = self.decimallon
        elif opcion2 == 2:
                self.decimallon = 360 - self.decimallon
        else:
            self.decimallon = self.decimallon

    def ang_sexagesimales(self):
        
        self.grados = int(self.decimal)
        minutos_decimales = (self.decimal - self.grados) * 60
        self.min = int(minutos_decimales)
        self.seg = (minutos_decimales - self.min) * 60

        # Verificación y ajuste de segundos
        if self.seg >= 60:
            self.min += 1
            self.seg -= 60

        # Verificación y ajuste de minutos
        if self.min >= 60:
            self.grados += 1
            self.min -= 60

        # Verificación y ajuste de grados
        if self.grados >= 360:
            self.grados -= 360