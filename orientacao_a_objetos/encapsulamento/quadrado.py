class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida

    @property
    def altura(self):
        return self.__medida

    @altura.setter
    def altura(self, valor):
        self.__medida = valor

    @property
    def largura(self):
        return self.__medida

    @largura.setter
    def largura(self, valor):
        self.__medida = valor

    def area(self):
        return self.altura * self.largura


quadrado = Quadrado(2)
quadrado.altura = 3
quadrado.largura = 4
