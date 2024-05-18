'''
93) Faça um programa que tenha um procedimento chamado Contador() que recebe 
três valores como parâmetro: o início, o fim e o incremento de uma contagem. O
programa principal deve solicitar a digitação desses valores e passá-los ao 
procedimento, que vai mostrar a contagem na tela.

Ex: Para os valores de início (4), fim (20) e incremento(3) teremos
Contador(4, 20, 3) vai mostrar na tela 4 >> 7 >> 10 >> 13 >> 16 >> 19 >> FIM
'''

def Contador(inicio, fim, incremento):
    contador = inicio
    while contador <= fim:
        print(contador, end=" >> ")
        contador += incremento
    print("FIM")

inicio = int(input("Digite o valor de início da contagem: "))
fim = int(input("Digite o valor de fim da contagem: "))
incremento = int(input("Digite o valor do incremento da contagem: "))

Contador(inicio, fim, incremento)
