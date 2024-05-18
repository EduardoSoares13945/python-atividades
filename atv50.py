'''
50) Função : Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3

Dica: Precisa Importar o Pacote Random
'''

import random

numeros = []
maior5 = []
div3 = []

for i in range(20):
    numeros.append(random.randint(0, 10))
    print(numeros[i], end=' ')
    if numeros[i] > 5:
        maior5.append(numeros[i])
    if numeros[i] % 3 == 0:
        div3.append(numeros[i])

print(f'\n{maior5} estão acima de 5 e {div3} são divisiveis por 3.')