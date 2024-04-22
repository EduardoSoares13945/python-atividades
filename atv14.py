'''14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.'''

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias foi o carro alugado? '))

preco_dia = 90
preco_km = 0.20

preco_total = (km * preco_km) + (dias * preco_dia)
print('O total a pagar é de R${:.2f}'.format(preco_total))