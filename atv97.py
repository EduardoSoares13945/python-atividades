'''
97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma 
adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o 
maior entre eles.
'''

def Maior(n1, n2, n3):
    return max(n1, n2, n3)

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior = Maior(n1, n2, n3)
print(f"O maior número entre {n1}, {n2} e {n3} é: {maior}")
