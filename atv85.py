'''
85) Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e guarde esses dados em três vetores.
No final, mostre uma listagem contendo apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.
'''

nomes = []
sexos = []
salarios = []

for i in range(5):
    nome = input(f"Digite o nome do funcionário {i + 1}: ")
    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: "))
    
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

print("Funcionárias que ganham mais de R$5000:")
for nome, sexo, salario in zip(nomes, sexos, salarios):
    if sexo == 'F' and salario > 5000:
        print(f"Nome: {nome}, Salário: R${salario:.2f}")
