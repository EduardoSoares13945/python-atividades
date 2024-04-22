'''
22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
alistamento.
'''
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18  
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))