'''
67) Faça um programa usando a estrutura “para” que leia um número inteiro positivo e mostre na tela uma contagem de 0 até o valor digitado:
Ex: Digite um valor: 9
Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!
'''

r = int(input('Digite um número: '))
print('Contagem: ', end='')
for i in range(r):
    i+=1
    print(i, end=', ')
    if i == r:
        print(i, end=', FIM!')