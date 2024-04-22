'''
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
'''

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    tipo = "EQUILÁTERO"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "ISÓSCELES"
else:
    tipo = "ESCALENO"

print(f"O triângulo formado é {tipo}.")
