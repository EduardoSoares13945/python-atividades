'''
70) [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência 
de Fibonacci:
1 1 2 3 5 8 13 21...
'''

a, b = 0, 1

for i in range(11):
    print(a, end=" ")
    a, b = b, a + b

