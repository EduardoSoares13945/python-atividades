'''
56) Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.

Obs: O programa será interrompido quando o número 1111 for digitado
'''

soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 1111:
        break
    soma += n

print(f'A soma entre todos os números digitados é {soma}.')