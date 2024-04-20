'''
29) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
Até 3 anos de empresa: aumento de 3%
entre 3 e 10 anos: aumento de 12.5%
10 anos ou mais: aumento de 20%
'''

nome = input('Qual é o nome do funcionário? ')
salario = float(input('Qual é o salário deste funcionário? R$'))
anos = int(input('Há quantos anos trabalha na empresa? '))

print(f'O funcionário {nome} trabalha há {anos} anos na empresa.')

if anos <= 3:
    novo_salario = salario + (salario * 0.03)
    print(f'O novo salário é de R${novo_salario:.2f}')

elif anos > 3 and anos < 10:
    novo_salario = salario + (salario * 0.125)
    print(f'O novo salário é de R${novo_salario:.2f}')

elif anos >= 10:
    novo_salario = salario + (salario * 0.20)
    print(f'O novo salário é de R${novo_salario:.2f}')
