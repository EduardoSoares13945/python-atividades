'''
84) Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses 
valores em dois vetores, em posições relacionadas. No final, mostre uma listagem 
contendo apenas os dados das pessoas menores de idade.
'''

nomes = []
idades = []

for i in range(9):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    nomes.append(nome)
    idades.append(idade)

print("\nPessoas menores de idade:")
for i in range(9):
    if idades[i] < 18:
        print(f"Nome: {nomes[i]}, Idade: {idades[i]}")
 