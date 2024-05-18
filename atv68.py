'''
68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura 
“para”. No final, mostre na tela:

a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres 
d) O maior peso entre os homens
'''
def main():
    total_mulheres = 0
    total_homens_100kg = 0
    soma_peso_mulheres = 0
    total_peso_mulheres = 0
    maior_peso_homens = 0

    for _ in range(8):
        sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()
        peso = float(input("Digite o peso da pessoa (em kg): "))

        if sexo == 'F':
            total_mulheres += 1
            soma_peso_mulheres += peso
            total_peso_mulheres += 1
        elif sexo == 'M':
            if peso > 100:
                total_homens_100kg += 1
            if peso > maior_peso_homens:
                maior_peso_homens = peso

    if total_peso_mulheres > 0:
        media_peso_mulheres = soma_peso_mulheres / total_peso_mulheres
    else:
        media_peso_mulheres = 0

    print(f"a) Quantas mulheres foram cadastradas: {total_mulheres}")
    print(f"b) Quantos homens pesam mais de 100Kg: {total_homens_100kg}")
    print(f"c) A média de peso entre as mulheres: {media_peso_mulheres:.2f} kg")
    print(f"d) O maior peso entre os homens: {maior_peso_homens:.2f} kg")

if __name__ == "__main__":
    main()

'''mulheres = 0

for i in range(1, 9):
    sexo = str(input("Digite o sexo da {}ª pessoa (M/F): ".format(i))).upper()
    peso = float(input("Digite o peso da {}ª pessoa: ".format(i)))
if sexo == "F":
        mulheres += 1
if sexo == "M" and peso > 100:
        print("O homem pesa mais de 100Kg")
        print("O homem pesa {}Kg".format(peso))
        print("A média de peso entre as mulheres é {}".format(peso / mulheres))
        print("O maior peso entre os homens é {}".format(peso))
        print("A média de peso entre as mulheres é {}".format(peso / mulheres))'''
