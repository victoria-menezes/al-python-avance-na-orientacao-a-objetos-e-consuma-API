from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida:
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome,preco) # vai na classe 'acima' dessa e usa seu __init__
        self._tamanho = tamanho
    
    def __str__(self):
        return self._nome