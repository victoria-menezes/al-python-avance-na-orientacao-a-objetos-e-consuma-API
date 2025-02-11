from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self._portas = portas
        self._cor = cor
    
    def __str__(self):
        return '{} {} {}, {} portas | {}'.format(self._marca, self._modelo, self._cor, self._portas, 'Ligado' if self._ligado else 'Desligado')
    
    def ligar(self):
        self._ligado = True
