'''
81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No final, mostre:

a) Qual é a média de idade das pessoas cadastradas
b) Em quais posições temos pessoas com mais de 25 anos
c) Qual foi a maior idade digitada (podem haver repetições)
d) Em que posições digitamos a maior idade
'''

idades = []

for i in range(8):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    idades.append(idade)

media_idade = sum(idades) / len(idades)
print(f"Média de idade: {media_idade:.2f}")

print("Posições com pessoas com mais de 25 anos:")
for i, idade in enumerate(idades):
    if idade > 25:
        print(i)

maior_idade = max(idades)
print(f"Maior idade digitada: {maior_idade}")

print("Posições com a maior idade digitada:")
for i, idade in enumerate(idades):
    if idade == maior_idade:
        print(i)
