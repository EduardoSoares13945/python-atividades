'''
27) Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média até 4.9: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Insira a primeira nota: '))

nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}.')

if media <= 4.9:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print(f'RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')