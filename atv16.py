'''
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou.
Considere que um fumante perde 10 min de vida a cada cigarro.
Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
'''

cig_dia = int(input('Quantos cigarros você fuma por dia? '))
cig_anos = int(input('Por quantos anos você fumou? '))

dias_perdidos = (10 * cig_dia * cig_anos * 365) / 1440

print(f'Você perdeu {round(dias_perdidos)} dias de vida.')