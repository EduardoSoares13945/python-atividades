'''
28) Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP
'''

largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))

area = largura * comprimento

classificacao = ""
if area < 100:
    classificacao = "TERRENO POPULAR"
elif 100 <= area <= 500:
    classificacao = "TERRENO MASTER"
else:
    classificacao = "TERRENO VIP"


print(f"A área do terreno é {area} m².")
print(f"Classificação do terreno: {classificacao}")
