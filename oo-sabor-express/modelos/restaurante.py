from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    # Variáveis criadas fora do __init__ são compartilhadas por todos os objetos da mesma classe
    restaurantes = []
    
    # Método construtor: sempre que criarmos uma instância, esse método será chamado
    # self = se refere à instância ativa, e não qualquer outra. Não precisa ser chamado de self, pode ser 'this' ou qualquer outra variavel. Só precisa ser o primeiro argumento.
    def __init__(self, nome, categoria):
        self._nome = nome.title() # coloca primeira letra sempre como maiúscula, _ indica que será uma propriedade privada, que não é setada diretamente pelo usuário
        self._categoria = categoria.upper()  # deixa tudo maiúsculo
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # Adicionar o objeto criado à lista restaurantes
    
    def __str__(self):
        # Definir como esse objeto será exibido em texto (por exemplo, em print()s)
        # para dar print nos atributos de um objeto cuja classe nao tem um __str__, se usa vars(OBJETO)
        # print (vars(restaurante_praca))
        return '{} {} {} | {}'.format(self._nome.ljust(25), self._categoria.ljust(25), self.media_avaliacoes.ljust(25),self.ativo)
    

    @property # muda como esses atributos serão lidos
    def ativo(self): # define como 'ativo' deve ser lido
        return '☑' if self._ativo else '☒'
    
    @property
    def media_avaliacoes(self):
        '''Retorna uma string da média das notas.'''
        if not self._avaliacoes:
            return 'NENHUMA AVALIAÇÃO'
        else:
            media = sum(a._nota for a in self._avaliacoes) / len(self._avaliacoes)
            return '{:.1f}'.format(media)

    @classmethod # É um método da classe, não de um objeto específico
    def listar_restaurantes(cls):
        print('{} {} {} | {}'.format('Restaurante'.ljust(25), 'Categoria'.ljust(25), 'Nota (0 - 5)'.ljust(25), 'Status').upper())
        for r in cls.restaurantes:
            print(r)
    
    @property
    def listar_cardapio(self):
        print('Cardápio do restaurante {} \n'.format(self._nome))
        for i, item in enumerate(self._cardapio, start=1): # enumerate adicionar um counter para cara item, comecando em 1 (em vez de 0)
            mensagem = '{}. Nome: {} | Preço: R${:.2f}'.format(i, item._nome, item._preco)
            if hasattr(item, 'tipo'):
                mensagem += ' | Tipo: {}'.format(item.tipo)
            if hasattr(item,'_descricao'):
                mensagem += ' | Descrição: {}'.format(item.descricao)
            if hasattr(item, 'tamanho'): 
                mensagem += ' | Tamanho: {}'.format(item.tamanho)
            print(mensagem)

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def adicionar_avaliacao(self, cliente, nota):
        if 0 <= nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)