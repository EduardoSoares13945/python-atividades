'''
69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética),
mostrando na tela os 10 primeiros elementos da PA e a soma entre todos os valores da sequência.
'''

p1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

pa = []

for i in range(10):
    termo = p1 + i * razao
    pa.append(termo)

print("Os 10 termos da PA são:")
print(pa)

print(f'A soma entre todos os termos da PA equivale a: {sum(pa)}')
