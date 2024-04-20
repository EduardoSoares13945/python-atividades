'''
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar.
Considere US$1,00 = R$3,45.
'''

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.45

print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} dolares.')