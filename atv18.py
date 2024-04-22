'''18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
dela e depois mostre se ela pode ou não votar.'''

ano = int(input('Digite o ano de nascimento: '))

idade = 2021 - ano

if idade < 18:
    print('Você ainda não pode votar!')
    print('Você tem {} anos em {}.'.format(idade, ano))
else:
    print('Você pode votar!')
