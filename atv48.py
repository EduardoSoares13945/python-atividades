'''
48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
'''

soma = 0
for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))
    soma += n
print(f'A soma dos números digitados é {soma}.')