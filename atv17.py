'''
17) Escreva um programa que pergunte a velocidade de um carro.
Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
'''

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você foi multado em {multa:.2f} reais.')
else:
    print(f'Você não foi multado.')