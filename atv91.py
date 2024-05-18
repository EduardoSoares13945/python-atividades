'''
91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses 
valores para um procedimento Maior() que vai verificar qual deles é o maior e 
mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem 
informando essa característica.
'''

def Maior(valor1, valor2):
    if valor1 > valor2:
        print(f"O maior valor é: {valor1}")
    elif valor2 > valor1:
        print(f"O maior valor é: {valor2}")
    else:
        print("Os dois valores são iguais.")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

Maior(valor1, valor2)
