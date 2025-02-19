from ecuaciones import Ecuaciones

import sympy as sp

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
        misEcuaciones.mediciones()
        print(f"""\nLa matriz de las mediciones es: 
{sp.pprint(sp.Matrix(misEcuaciones.lb))}\n
Digite las Ecuaciones de Enlace:\n
{misEcuaciones.enlace()}\n
Las ecuaciones de enlace son:\n
{sp.pprint(sp.Matrix(misEcuaciones.l0))}\n 
El ajuste por metodo paramterico es:\n
{misEcuaciones.linealizacion()}\n""")


        pass

miInteractuador = Parametrico()
miInteractuador.menu()