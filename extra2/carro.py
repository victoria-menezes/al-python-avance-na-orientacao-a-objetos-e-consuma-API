from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        return '{} {}, {} portas | {}'.format(self._marca, self._modelo, self._portas, 'Ligado' if self._ligado else 'Desligado')
