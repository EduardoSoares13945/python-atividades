'''
59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai 
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:

a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens
'''

def calcular_dados():
    maior_idade = 0
    total_homens = 0
    total_idade_homens = 0
    quantidade_homens = 0
    menor_idade_mulher = float('inf')

    while True:
        idade = int(input("Digite a idade da pessoa: "))
        sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()

        if idade > maior_idade:
            maior_idade = idade

        if sexo == 'M':
            total_homens += 1
            total_idade_homens += idade
            quantidade_homens += 1
        elif sexo == 'F':
            if idade < menor_idade_mulher:
                menor_idade_mulher = idade
        else:
            print("Sexo inválido. Por favor, insira M ou F.")

        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    media_idade_homens = total_idade_homens / quantidade_homens if quantidade_homens > 0 else 0

    print(f"Maior idade lida: {maior_idade}")
    print(f"Quantidade de homens cadastrados: {total_homens}")
    print(f"Idade da mulher mais jovem: {menor_idade_mulher if menor_idade_mulher != float('inf') else 'Não cadastrada'}")
    print(f"Média de idade entre os homens: {media_idade_homens:.2f}")

calcular_dados()
