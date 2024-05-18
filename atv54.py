'''
54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:

a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.
'''

pesos = []
alturas = []

mais90kg = 0
letraC = 0
letraD = 0

for i in range(1, 8):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    pesos.append(peso)
    altura = float(input(f'Digite a altura da {i}ª pessoa: '))
    alturas.append(altura)
    
    if peso > 90:
        mais90kg += 1
    if peso < 50 and altura < 1.60:
        letraC += 1
    if peso > 100 and altura > 1.90:
        letraD += 1

media = sum(alturas) / len(alturas)

print(f'A média de altura do grupo é de {media:.2f}m.')
print(f'{mais90kg} pessoas pesam mais de 90Kg.')
print(f'{letraC} pessoas pesam menos de 50Kg e tem menos de 1.60m.')
print(f'{letraD} pessoas pesam mais de 100Kg e medem mais de 1.90m.')