'''
100) Melhore o exercício 96, criando além da função Media() uma outra função chamada Situacao(), que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como parâmetro o resultado retornado pela função Media()
'''

def Media(notas):
    return sum(notas) / len(notas)

def Situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

notas = []
for i in range(4):  
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = Media(notas)

situacao = Situacao(media)

print(f"A média do aluno é: {media:.2f}")
print(f"O aluno está: {situacao}")
