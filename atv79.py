'''
79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor. 
No final, mostre quais são os números pares que foram digitados e em que posições eles estão armazenados.
'''

numeros = []

for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print("Números pares digitados e suas posições:")
for i, numero in enumerate(numeros):
    if numero % 2 == 0:
        print(f"Número {numero} na posição {i}")
