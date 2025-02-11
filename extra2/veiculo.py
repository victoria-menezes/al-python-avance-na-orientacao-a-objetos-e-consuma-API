from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    def __str__(self):
        return '{} {} | {}'.format(self._marca, self._modelo, 'Ligado' if self._ligado else 'Desligado')
    
    @abstractmethod
    def ligar(self):
        pass