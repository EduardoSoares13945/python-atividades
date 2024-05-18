'''
77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor.
No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.
'''

nomes = []

for i in range(7):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    nomes.append(nome)

print("Nomes ao inverso:")
for nome in reversed(nomes):
    print(nome)
