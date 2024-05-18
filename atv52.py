'''
52) Crie um programa que leia a idade de 10 pessoas, mostrando no final:

a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida
'''

idades = []
maior18 = []
menor5 = []

for i in range(10):
    idades.append(int(input(f'Digite a idade da {i + 1}ª pessoa: ')))
    if idades[i] > 18:
        maior18.append(idades[i])
    elif idades[i] < 5:
        menor5.append(idades[i])

media = sum(idades) / len(idades)
maior_idade = max(idades)

print(f'A média de idade do grupo é {media:.1f} anos.')
print(f'Há {len(maior18)} pessoas maiores de 18 anos.')
print(f'Há {len(menor5)} pessoas menores de 5 anos.')
print(f'A maior idade lida foi {maior_idade} anos.')