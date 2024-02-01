from banco_delas.classes.banco import Banco


class Cliente(Banco):
    def __init__(self, sexo, saldo, cheque_especial, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.sexo = sexo
        self.__saldo = saldo
        self.__cheque_especial = cheque_especial

    @property
    def deposita(self):
        return self.__saldo

    @deposita.setter
    def deposita(self, valor):
        self.__saldo = valor

    @property
    def saca(self):
        return self.__saldo

    @saca.setter
    def saca(self, valor):
        self.__saldo -= valor

    @property
    def possui_cheque_especial(self):
        return self.__cheque_especial

    @possui_cheque_especial.setter
    def possui_cheque_especial(self, valor):
        if self.sexo == 'F' or self.sexo == 'f' and valor > 0:
            self.__cheque_especial = self.renda_mensal
        else:
            self.__cheque_especial = 0
