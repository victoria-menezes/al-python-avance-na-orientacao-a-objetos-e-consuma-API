from modelos.restaurante import Restaurante

# Um objeto = uma instancia de uma classe
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('sushi rolls', 'Japonesa')

def main ():
    restaurante_praca.receber_avaliacao('Gui', 10)
    restaurante_praca.receber_avaliacao('Laís', 8)
    restaurante_praca.receber_avaliacao('Emy', 2)

    Restaurante.alternar_estado(restaurante_mexicano)
    Restaurante.listar_restaurantes()

    
if __name__ == '__main__':
    main()