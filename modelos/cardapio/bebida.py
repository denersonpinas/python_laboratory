from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    _tamanho   = ''

    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self) -> str:
        return self._nome