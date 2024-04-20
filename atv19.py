'''
19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
'''

nota1 = float(input('Insira a primeira nota: '))

nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}.')

if media >= 7.0:
    print(f'Parabéns, você foi aprovado.')
elif media < 7.0:
    print(f'Você foi reprovado.')