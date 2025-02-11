from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
    
    def __str__(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo.capitalize()

    @property
    def tamanho(self):
        return self._tamanho.capitalize()
    
    def aplicar_desconto(self):
        pass