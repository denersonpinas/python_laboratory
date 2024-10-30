from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    ''' Descrição do restaurante
    -   Nome
    -   Categoria
    -   Status
    ''' 

    _nome           = ''
    _categoria      = ''
    _ativo          = False
    _avaliacao      = []
    _cardapio       = []
    restaurantes    = []
    

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return self._nome

    @classmethod
    def listar_restaurantes(cls):
        titulo = f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}'
        linha = ('-' * len(titulo))
        print(f'{titulo}')
        print(f'{linha}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
    
    def alternar_estado_restaurante(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            nova_avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(nova_avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome:{item._nome.ljust(20)} | Descrição:{item._descricao.ljust(20)} | Preço: R${item._preco}'
            else:
                mensagem = f'{i}. Nome:{item._nome.ljust(20)} | Tamanho:{item._tamanho.ljust(20)} | Preço: R${item._preco}'
            print(mensagem)
