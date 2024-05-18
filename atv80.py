'''
80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e 
15 sorteados pelo computador. Depois disso, peça para o usuário digitar um 
número (chave) e seu programa deve mostrar em que posições essa chave foi 
encontrada. Mostre também quantas vezes a chave foi sorteada.
'''

import random

def main():
    vetor = [random.randint(1, 15) for _ in range(30)]

    print("Vetor sorteado:")
    print(vetor)

    chave = int(input("\nDigite um número (chave) entre 1 e 15: "))

    posicoes = [i for i, num in enumerate(vetor) if num == chave]
    quantidade = len(posicoes)

    if quantidade > 0:
        print(f"\nA chave {chave} foi encontrada nas posições: {posicoes}")
        print(f"A chave {chave} foi sorteada {quantidade} vezes.")
    else:
        print(f"\nA chave {chave} não foi encontrada no vetor.")

if __name__ == "__main__":
    main()