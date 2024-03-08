from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_foms = Restaurante("Fom's", 'Lanchonete')
bebida_suco = Bebida('Suco de Laranja', 15.0, 'Grande')
prato_lanche = Prato('4 em 1', 19.9, 'Irresistivel')
restaurante_foms.adicionar_no_cardapio(bebida_suco)
restaurante_foms.adicionar_no_cardapio(prato_lanche)


def main():
    restaurante_foms.exibier_cardapio

if __name__ == '__main__':
    main()