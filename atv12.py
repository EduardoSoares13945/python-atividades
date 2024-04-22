'''12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.'''

preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print(f'O produto custa R${preco:.2f}, com 5% de desconto, custa R${desconto:.2f}.')