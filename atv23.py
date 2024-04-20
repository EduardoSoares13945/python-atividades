'''
23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres.
Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto.
Sabendo que:
Homens ganham 5% de desconto
Mulheres ganham 13% de desconto
'''

nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo [M/F]: ')

if sexo == 'M':
    preco = float(input('Digite o custo total das compras: '))
    desconto = preco * 0.05
    preco -= desconto
    print(f'Olá, {nome}! O seu carrinho custou R${preco:.2f} com desconto de R${desconto:.2f}')
    print(f'Por ser do sexo Masculino ({sexo}), recebeu 5% de desconto!')
elif sexo == 'F':
    preco = float(input('Digite o custo total das compras: '))
    desconto = preco * 0.13
    preco -= desconto
    print(f'Olá {nome}! O seu carrinho custou R${preco:.2f} com desconto de R${desconto:.2f}')
    print(f'Por ser do sexo Feminino ({sexo}), recebeu 13% de desconto!')
