'''
73) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente)
um vetor numérico com 10 posições, conforme abaixo:

9 8 7 6 5 4 3 2 1 0
0 1 2 3 4 5 6 7 8 9
'''

vetor = [0] * 10
vetor_r = [0] * 10

for i in range(10):
    vetor[i] = i

for i in range(10):
    vetor_r[i] = 9-i

print(vetor_r)
print(vetor)