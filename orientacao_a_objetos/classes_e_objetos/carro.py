class Carro:
    def __init__(self, ligado, cor, modelo, velociddade):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velociddade = velociddade

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False

    def cor(self):
        return self.cor

    def modelo(self):
        return self.modelo

    def velocidade(self):
        return self.velociddade

    def __str__(self) -> str:
        return f"O carro é um {self.modelo} de cor {self.cor} e seu estado de ligado é {self.ligado}."


carro_novo = Carro(False, "preto", "Fusca", 0)
carro_novo.ligado = True

segundo_carro_novo = Carro(True, "azul", "Fiesta", 0)
segundo_carro_novo.ligado = False

print(carro_novo)
print(segundo_carro_novo)
