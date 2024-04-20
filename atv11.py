'''
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta. (Pesquisa Livre)
'''

import math as mt

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b + mt.sqrt(delta)) / (2 * a)
    x2 = (-b - mt.sqrt(delta)) / (2 * a)
    print(f'O valor de Delta é igual a {delta:.1f}.\nO valor de x1 é igual a {x1:.1f}.\nO valor de x2 é igual a {x2:.1f}.')
elif delta == 0:
    x = -b / (2 * a)
    print(f'O valor de Delta é igual a {delta:.1f}.\nO valor de x é igual a {x:.1f}.')
elif delta < 0:
    print(f'O valor de Delta é igual a {delta:.1f}.\nNão existe raízes reais.')

