class Type():
    def __init__(self,tipo,valor,x,y):
        self.tipo = tipo
        self.valor = valor
        self.x = x
        self.y = y

class UnidadM():
    def __init__(self,tipo,valor):
        self.tipo = tipo
        self.valor = valor
        self.x = 0

class UnidadC():
    def __init__(self,tipo):
        self.tipo = tipo
        self.y = 0

class Nodo():

    def __init__(self, tipo,informacion,siguiente = 0):
        self.tipo = tipo


