from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
    
    def __str__(self):
        return '{} {}, tipo {} | {}'.format(self._marca, self._modelo, self._tipo, 'Ligado' if self._ligado else 'Desligado')
