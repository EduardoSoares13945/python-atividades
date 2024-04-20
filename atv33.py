'''
33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Quanto custa a casa? R$'))
salario = float(input('Quanto de salário você recebe? R$'))
anos = int(input('Quantos anos você irá pagar pela casa? '))

qtd_prest = anos * 12
prestacao = valor_casa / qtd_prest

if salario * 0.3 > prestacao:
    print('Empréstimo aprovado!')
    print(f'Você pagará {qtd_prest} prestações de R${prestacao:.2f} por {anos} anos')
else:
    print('Empréstimo negado.')