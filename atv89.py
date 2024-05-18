'''
89) Crie um programa que melhore o procedimento Gerador() da questão anterior 
para que o programador possa escolher uma entre três bordas:
 +-------=======------+ Borda 1
 ~~~~~~~~:::::::~~~~~~~ Borda 2
 <<<<<<<<------->>>>>>> Borda 3
'''

def Gerador(mensagem, repeticoes, borda):
    if borda == 1:
        borda_inicio = "+-------=======------+"
        borda_final = "+-------=======------+"
    elif borda == 2:
        borda_inicio = "~~~~~~~~:::::::~~~~~~~~"
        borda_final = "~~~~~~~~:::::::~~~~~~~~"
    elif borda == 3:
        borda_inicio = "<<<<<<<<------->>>>>>>"
        borda_final = "<<<<<<<<------->>>>>>>"
    else:
        print("Borda inválida!")
        return

    print(borda_inicio)
    for _ in range(repeticoes):
        print(f" {mensagem} ")
    print(borda_final)

Gerador("Aprendendo Python", 4, 3)
