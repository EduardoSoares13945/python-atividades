'''
36) Um programa de vida saudável quer dar pontos atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
 - Cada hora de atividade física no mês vale pontos
 - até 10h de atividade no mês: ganha 2 pontos por hora
 - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
 - acima de 20h de atividade no mês: ganha 10 pontos por hora
 - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos) 
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
'''

horas_atividade = float(input("Digite o total de horas de atividade física no mês: "))

pontos = 0
dinheiro = 0

if horas_atividade <= 10:
    pontos = horas_atividade * 2
elif 10 < horas_atividade <= 20:
    pontos = 10 * 2 + (horas_atividade - 10) * 5
else:
    pontos = 10 * 2 + 10 * 5 + (horas_atividade - 20) * 10

dinheiro = pontos * 0.05

print(f"Total de pontos: {pontos}")
print(f"Dinheiro ganho: R${dinheiro:.2f}")
