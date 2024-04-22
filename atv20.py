'''
20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
'''

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))