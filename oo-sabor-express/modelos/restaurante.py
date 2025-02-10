from modelos.avaliacao import Avaliacao

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
    

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
    
    