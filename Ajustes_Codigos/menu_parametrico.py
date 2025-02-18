from ecuaciones import Ecuaciones

misEcuaciones = Ecuaciones()

class Parametrico:

    def __init__(self):
        
        self.n = 0
        self.k = 0
        self.r = 0
        self.tk = []
        self.tk0 = []

    def menu (self):
        
        misEcuaciones.parametros()
        self.n = misEcuaciones.n
        self.k = misEcuaciones.k
        self.r = self.n - self.k
        misEcuaciones.val_aprox_parametros()
        self.tk = misEcuaciones.tk
        self.tk0 = misEcuaciones.tk0
        print(f"parametros aproximados = {self.tk0}")
        misEcuaciones.matrices()
        print(f"""La matriz de las mediciones es: 
{misEcuaciones.lb}""")
        pass

miInteractuador = Parametrico()
miInteractuador.menu()