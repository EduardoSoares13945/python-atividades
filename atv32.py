'''
32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
'''

import random

def jogo():
    # Sorteia um número entre 1 e 5
    numero_sorteado = random.randint(1, 5)
    
    # Pede ao jogador para adivinhar
    tentativa = int(input("Tente adivinhar o número sorteado (entre 1 e 5): "))
    
    # Verifica se a tentativa está correta
    if tentativa == numero_sorteado:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! O número sorteado foi {numero_sorteado}.")

# Inicia o jogo
jogo()
