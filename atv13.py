'''
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
'''

salario = float(input('Quanto o funcionário recebe? '))

novo_salario = salario + (salario * 0.15)

print(f'O novo salário do funcionário é de R${novo_salario:.2f}.')