'''
37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores.
Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
No final, mostre o seu novo salário, baseado na tabela a seguir:

- Mulheres
menos de 15 anos de empresa: +5%
de 15 até 20 anos de empresa: +12%
mais de 20 anos de empresa: +23%

- Homens
menos de 20 anos de empresa: +3%
de 20 até 30 anos de empresa: +13%
mais de 30 anos de empresa: +25%
'''

salario = float(input('Digite o salário atual: R$'))
sexo = input('Qual é o gênero do(a) funcionário(a)? [M/F] ')
anos = int(input('Há quantos anos o(a) funcionário(a) trabalha na empresa? '))

if sexo.upper() == 'F':
    if anos < 15:
        novo_salario = salario * 1.05
    elif anos >= 15 and anos <= 20:
        novo_salario = salario * 1.12
    elif anos > 20:
        novo_salario = salario * 1.23
    print(f'O novo salário é de R${novo_salario:.2f}')

elif sexo.upper() == 'M':
    if anos < 20:
        novo_salario = salario * 1.03
    elif anos >= 20 and anos <= 30:
        novo_salario = salario * 1.13
    elif anos > 30:
        novo_salario = salario * 1.25
    print(f'O novo salário é de R${novo_salario:.2f}')

else:
    print('Opção de gênero inválida. Por favor, tente novamente.')