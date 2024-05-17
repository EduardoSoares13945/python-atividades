'''
63) Crie um programa usando a estrutura “faça enquanto” que leia vários números. 
A cada laço, pergunte se o usuário quer continuar ou não.
No final, mostre na tela:

a) O somatório entre todos os valores
b) Qual foi o menor valor digitado
c) A média entre todos os valores
d) Quantos valores são pares
'''

numeros = []
soma = 0
menor = None
cont_pares = 0

while True:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    soma += numero
    
    if menor is None or numero < menor:
        menor = numero
    
    if numero % 2 == 0:
        cont_pares += 1
    
    continuar = input("Você quer continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

total_numeros = len(numeros)
if total_numeros > 0:
    media = soma / total_numeros
else:
    media = 0

print(f"Somatório de todos os valores: {soma}")
print(f"Menor valor digitado: {menor}")
print(f"Média dos valores: {media:.2f}")
print(f"Quantidade de valores pares: {cont_pares}")
