'''
53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:

a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
'''

idades = []
sexos = []
idadeHoms = []

homens = 0
mulheres = 0
mulheres20 = 0

for i in range(1, 6):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    idades.append(idade)
    sexo = input(f'Digite o sexo da {i}ª pessoa (M/F): ').upper()
    sexos.append(sexo)

    if sexo == 'M':
        homens += 1
        idadeHoms.append(idade)
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulheres20 += 1

print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres} mulheres.')
print(f'A média das idades de ambos os sexos é: {sum(idades) / len(idades)}')
print(f'A média das idades dos homens é: {sum(idadeHoms) / len(idadeHoms)}')
print(f'Há {mulheres20} mulheres que tem mais de 20 anos.')