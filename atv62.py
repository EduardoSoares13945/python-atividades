'''
62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas.
A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados.
No final, quando o usuário decidir parar, mostre na tela:

a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.
'''

idades = []
cont21 = 0

while True:
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    
    if idade >= 21:
        cont21 += 1
    
    continuar = input("Você quer continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

total_idades = len(idades)
if total_idades > 0:
    media_idades = sum(idades) / total_idades
else:
    media_idades = 0

print(f"Quantidade de idades digitadas: {total_idades}")
print(f"Média das idades: {media_idades:.2f}")
print(f"Quantidade de pessoas com 21 anos ou mais: {cont21}")
