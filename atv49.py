'''
49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
'''

pares = 0
impares = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}º número: '))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram digitados {pares} números pares e {impares} números ímpares.')