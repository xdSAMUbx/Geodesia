from ecuaciones import Ecuaciones

misEcuaciones = Ecuaciones()

class Parametrico:

    def __init__(self):
        
        self.n = 0
        self.k = 0
        self.r = 0
        self.tk = []

    def menu (self):
        
        misEcuaciones.parametros()
        self.n = misEcuaciones.n
        self.k = misEcuaciones.k
        self.r = self.n - self.k
        misEcuaciones.val_aprox_parametros()
        self.tk = misEcuaciones.tk
        print(f"parametros aproximados = {self.tk}")

miInteractuador = Parametrico()
miInteractuador.menu()