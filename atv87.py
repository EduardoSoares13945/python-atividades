'''
87) Crie um programa que melhore o procedimento Gerador() da questão anterior 
para que mostre uma mensagem personalizada, passada como parâmetro.
Ex: Ao chamar Gerador("Aprendendo Python") aparece:
+-------=======------+
 Aprendendo Python 
+-------=======------+
'''

def Gerador(mensagem):
    print("+-------=======------+")
    print(f" {mensagem} ")
    print("+-------=======------+")

Gerador("Aprendendo Python")
