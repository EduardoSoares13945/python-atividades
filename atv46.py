'''
46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
'''

soma = 0
for i in range(6, 101, 2):
    soma += i
    if i >= 6 and i < 100:
        print(i, end=' + ')
    elif i == 100:
        print(i)
print(f'A soma é igual a {soma}.')