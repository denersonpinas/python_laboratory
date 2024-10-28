from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    _descricao   = ''

    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self) -> str:
        return self._nome