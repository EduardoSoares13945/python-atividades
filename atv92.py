'''
92) Crie uma lógica que leia um número inteiro e passe para um procedimento
ParOuImpar() que vai verificar e mostrar na tela se o valor passado como 
parâmetro é PAR ou ÍMPAR.
'''

def ParOuImpar(num):
    if num % 2 == 0:
        print("O número {} é PAR".format(num))
    else:
        print("O número {} é ÍMPAR".format(num))

num = int(input("Digite um número inteiro: "))

ParOuImpar(num)
