from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

# Um objeto = uma instancia de uma classe
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('sushi rolls', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'Melhor pão da cidade')
sobremesa_sundae = Sobremesa('Sundae de Morango', 4,'Sorvete', 'pequeno')

restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_paozinho)
restaurante_praca.adicionar_item_cardapio(sobremesa_sundae)

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

def main():
    restaurante_praca.listar_cardapio

    
if __name__ == '__main__':
    main()