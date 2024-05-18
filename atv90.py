'''
90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses 
valores para um procedimento Somador() que vai calcular e mostrar a soma entre 
eles.
'''

def somador(num1, num2):
    print(num1 + num2)

num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

somador(num1, num2)