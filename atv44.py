'''
44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:

Ex: 
Digite o primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o último valor: '))
n3 = int(input('Digite o incremento: '))

while n1 <= n2:
    print(n1, end=' ')
    n1 += n3
    
print('Acabou!')
