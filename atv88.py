'''
88) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem vário Ex: Ao chamar Gerador("Aprendendo Python", 4) aparece: +-------====== =------+ Aprendendo Python Aprendendo Python Aprendendo Python Aprendendo Python +-------=======------+
'''
def Gerador(mensagem, repeticoes):
    largura = len(mensagem) + 4
    borda = "+" + "-" * (largura // 2 - 1) + "=====" + "-" * (largura // 2 - 1) + "+"
    
    print(borda)
    for _ in range(repeticoes):
        print(f" {mensagem} ")
    print(borda)

Gerador("Aprendendo Python", 4)