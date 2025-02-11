from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self): # metodo abstrato, servira de modelo para as classes derivadas. diz que todas suas filhas precisam definir esse metodo
        pass