'''
41)	Desenvolva um programa que mostre na tela a seguinte contagem:
100 95 90 85 80 ... 0 Acabou!
'''

for i in range(100, -1, -5):
    print(i, end=" ")
print("Acabou!")