'''
60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. 
O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:

a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos
'''

nomes = []
idades = []
sexos = []

MaisVelhoNome = str()
MaisJovemMulher = str()

Homens30 = 0
Mulheres18 = 0

MaisVelhoIdade = 0
MaisJovemMulherIdade = 18

while True:
    nome = str(input('Nome: '))
    nomes.append(nome)

    idade = int(input('Idade: '))
    idades.append(idade)

    sexo = str(input('Sexo [M/F]: ').upper())
    sexos.append(sexo)
    
    if sexo == 'M':
        if idade > 30:
            Homens30 += 1
    if sexo == 'F':
        if idade < 18:
            Mulheres18 += 1

    if idade > MaisVelhoIdade:
        MaisVelhoIdade = idade
        MaisVelhoNome = nome

    if idade < MaisJovemMulherIdade and sexo == 'F':
        MaisJovemMulherIdade = idade
        MaisJovemMulher = nome

    continuar = str(input('Deseja continuar? [S/N]: ').upper())

    if continuar == 'N':
        break


print(f'A média de idade do grupo é {(sum(idades) / len(idades)):.2f}')

print(f'O nome da pessoa mais velha é {MaisVelhoNome}')

if Mulheres18 == 0:
    print('Não há mulheres com menos de 18 anos.')
else:
    print(f'O nome da mulher mais jovem é {MaisJovemMulher}')
    print(f'Há {Mulheres18} mulheres com menos de 18 anos')

if Homens30 == 0:
    print('Não há homens com mais de 30 anos.')
else:
    print(f'Há {Homens30} homens com mais de 30 anos')