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

    def gms(self):
        signo = -1 if self.decimal < 0 else 1
        decimal = abs(self.decimal)
        self.grados = int(decimal)
        minutos_decimales = (decimal - self.grados) * 60
        self.min = int(minutos_decimales)
        self.seg = (minutos_decimales - self.min) * 60

        # Aplicar el signo al valor de grados
        self.grados *= signo

    @staticmethod
    def decimal_a_gms(decimal):
        """Convierte un valor decimal dado a grados, minutos y segundos, considerando negativos."""
        signo = -1 if decimal < 0 else 1
        decimal = abs(decimal)

        grados = int(decimal)
        minutos_decimales = (decimal - grados) * 60
        minutos = int(minutos_decimales)
        segundos = (minutos_decimales - minutos) * 60

        # Aplicar signo al valor completo
        grados *= signo

        return f"{grados}° {abs(minutos)}' {abs(segundos):.4f}\""

    @staticmethod
    def matriz_a_gms(matriz):
        resultado = []
        for i in range(matriz.rows):
            valor = matriz[i]
            valor_decimal = float(valor)  # Convertir el valor a flotante
            resultado.append([Angulos.decimal_a_gms(valor_decimal)])
        return resultado
