'''
96) Crie um programa que tenha uma função Media(), que vai receber as 2 notas de 
um aluno e retornar a sua média para o programa principal.
'''

def Media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

nota1 = float(input('Digite a primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))

media = Media(nota1, nota2)

print(f'A média do aluno é {media:.1f}.')
