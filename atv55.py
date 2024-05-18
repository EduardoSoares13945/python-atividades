'''
55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32.
A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.
'''

import random

def jogo():
    # Sorteia um número entre 1 e 10
    numero_sorteado = random.randint(1, 10)
    
    # Pede ao jogador para adivinhar
    tentativa = int(input("Tente adivinhar o número sorteado (entre 1 e 10): "))
    contador = 1
    while tentativa != numero_sorteado and contador < 4:
        tentativa = int(input("Tente adivinhar o número sorteado (entre 1 e 10): "))
        contador += 1
    if tentativa == numero_sorteado:
        print(f'Parabéns! Você acertou o número sorteado em {contador} tentativas.')
    else:
        print(f'Que pena! O número sorteado foi {numero_sorteado}.')

# Inicia o jogo

jogo()