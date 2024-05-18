'''
95) Refaça o exercício 90, só que agora em forma de função Somador(), que vai 
receber dois parâmetros e vai retornar o resultado da soma entre eles para o 
programa principal.
'''

def Somador(valor1, valor2):
    return valor1 + valor2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

resultado = Somador(valor1, valor2)
print(f"A soma de {valor1} e {valor2} é igual a {resultado}.")
