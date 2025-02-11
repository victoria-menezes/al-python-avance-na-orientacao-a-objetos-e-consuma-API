from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # vai herdar os atributos de ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco) # vai na classe 'acima' dessa e usa seu __init__
        self._descricao = descricao
    
    def __str__(self):
        return self._nome