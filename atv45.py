'''
45) O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer
situação.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o último valor: '))
n3 = int(input('Digite o incremento: '))


if n1 > n2:
    print('O primeiro valor é maior que o último!')

if n3 > 0:
    while n1 <= n2:
        print(n1, end=' ')
        n1 += n3
    print('Acabou!')
else:
    while n1 >= n2:
        print(n1, end=' ')
        n1 += n3
    print('Acabou!')