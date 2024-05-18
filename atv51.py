'''
51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
'''

for i in range(1, 9):
    produto = float(input(f'Insira o preço do produto {i}: '))
    if i == 1:
        maior = produto
        menor = produto
    else:
        if produto > maior:
            maior = produto
        if produto < menor:
            menor = produto

print(f'O maior preço é R${maior:.2f} e o menor preço é R${menor:.2f}.')