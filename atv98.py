'''
98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois 
números como parâmetro e depois vai retornar a soma de todos os valores no 
intervalo entre os valores recebidos.
'''

def SuperSomador(valor1, valor2):
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1

    soma = sum(range(valor1, valor2 + 1))
    
    return soma

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

resultado = SuperSomador(valor1, valor2)
print(f"A soma de todos os valores no intervalo entre {valor1} e {valor2} é {resultado}")

