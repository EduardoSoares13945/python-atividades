'''
65) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
100 90 80 70 60 50 40 30 20 10 0 Acabou!
'''

for i in range(100, -1, -10):
    print(i, end=' ')
print("Acabou!")