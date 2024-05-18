'''
82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em 
um vetor. No final, mostre: 

a) Qual é a média da turma
b) Quantos alunos estão acima da média da turma
c) Qual foi a maior nota digitada
d) Em que posições a maior nota aparece
'''

notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima_da_media = 0

for nota in notas:
    if nota > media:
        acima_da_media += 1

maior_nota = max(notas)

posicoes_maior_nota = [i for i, nota in enumerate(notas) if nota == maior_nota]

print(f"A média da turma é: {media:.2f}")
print(f"Quantidade de alunos acima da média: {acima_da_media}")
print(f"A maior nota digitada foi: {maior_nota:.2f}")
print(f"A maior nota aparece nas posições: {posicoes_maior_nota}")