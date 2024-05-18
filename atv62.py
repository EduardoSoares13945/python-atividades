'''
62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de 
várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou 
não continuar a digitar dados. No final, quando o usuário decidir parar, mostre 
na tela:

a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.
'''
def main():
    contador = 0
    soma_idades = 0
    maiores_21 = 0

    while True:
        idade = int(input("Digite a idade: "))
        contador += 1
        soma_idades += idade
        if idade >= 21:
            maiores_21 += 1

        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

    if contador > 0:
        media_idades = soma_idades / contador
    else:
        media_idades = 0

    print(f"a) Quantas idades foram digitadas: {contador}")
    print(f"b) Média entre as idades digitadas: {media_idades:.2f}")
    print(f"c) Quantas pessoas têm 21 anos ou mais: {maiores_21}")

if __name__ == "__main__":
    main()