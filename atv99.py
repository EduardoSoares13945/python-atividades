'''
99) Faça um programa que possua uma função chamada Potencia(), que vai receber 
dois parâmetros numéricos (base e expoente) e vai calcular o resultado da 
exponenciação.

Ex: Potencia(5,2) vai calcular 52 = 25 
'''

def Potencia(base, expoente):
    return base ** expoente

base = float(input("Digite o valor da base: "))
expoente = float(input("Digite o valor do expoente: "))

resultado = Potencia(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é igual a: {resultado}")
