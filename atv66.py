'''
66) Escreva um programa que leia um número qualquer e mostre a tabuada desse 
número, usando a estrutura “para”.
Ex: Digite um valor: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 ...
'''

num = int(input("Digite um valor: "))

for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))
    