'''
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
'''

dias_trb = int(input('Quantos dias você trabalhou? '))

salario = dias_trb * 8 * 25

print(f'Você trabalhou {dias_trb} dias e recebeu R${salario:.2f}.')