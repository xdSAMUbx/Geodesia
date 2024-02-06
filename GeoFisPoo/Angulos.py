class Angulos:
    
    def __init__(self):
        
        self.decimal = 0
        self.grados = 0
        self.min = 0
        self.seg = 0
        
    def ang_decimales (self):
        
        print("Ingrese el angulo en el siguiente orden (Si es oeste, escribir todos los angulos en negativo): ")
        self.grados = float(input("Grados: "))
        self.min = float(input("Minutos: "))
        self.seg = float(input("Segundos: "))
        self.decimal = self.grados + (self.min/60) + (self.seg/3600)
        print("¿El angulo es referente a la longitud?")
        print("Si la respuesta es si, ingrese 1, si no, 0.")
        val = int(input("Ingrese su respuesta: "))
        if val == 1:
            print("¿ Es Positivo o Negativo ?")
            print("1) Positivo")
            print("2) Negativo")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                self.decimal = self.decimal
            elif opcion == 2:
                self.decimal = 360 - self.decimal
        else:
            self.decimal = self.decimal
    
    def ang_sexagesimales():
        pass