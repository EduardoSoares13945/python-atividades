'''
34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade mórbida
'''

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso ideal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 40:
        return "Obesidade"
    else:
        return "Obesidade mórbida"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é {peso / (altura ** 2):.2f}, e você está classificado como {classificacao}.")
