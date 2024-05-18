'''
71) Faça um programa que preencha automaticamente um vetor numérico com 8 posições, conforme abaixo:

999 999 999 999 999 999 999 999
0 1 2 3 4 5 6 7
'''

vetor = [999] * 8
print("Vetor antes:")
print(vetor)

for i in range(8):
    vetor[i] = i

print("Vetor preenchido:")
print(vetor)
