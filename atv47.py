'''
47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
'''
soma = 0
for i in range(500, -1, -50):
    soma += i
    if i <= 500 and i > 0:
        print(i, end=' + ')
    elif i == 0:
        print(i)
print(f'\nA soma é igual a {soma}')