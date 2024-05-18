'''
58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa 
vai parar quando for digitada a idade 999. No final, mostre quantos alunos 
existem na turma e qual é a média de idade do grupo.
'''

def calcular_idades():
    idades = []

    while True:
        idade = int(input("Digite a idade do aluno (999 para parar): "))
        if idade == 999:
            break
        idades.append(idade)

    quantidade_alunos = len(idades)
    media_idade = sum(idades) / quantidade_alunos if quantidade_alunos > 0 else 0

    print(f"Total de alunos na turma: {quantidade_alunos}")
    print(f"Média de idade do grupo: {media_idade:.2f}")

calcular_idades()
