class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return

        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return

        if self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return

        if self.volume < self.volume_max:
            self.volume += 1

    def diminuir_volume(self):
        if not self.ligada:
            return

        if self.volume > self.volume_min:
            self.volume -= 1


tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
