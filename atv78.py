'''
78) Escreva um programa que leia 15 números e guarde-os em um vetor. No final, 
mostre o vetor inteiro na tela e em seguida mostre em que posições foram 
digitados valores que são múltiplos de 10.
'''
def main():
    vetor = []

    for i in range(15):
        numero = int(input(f"Digite o {i + 1}º número: "))
        vetor.append(numero)

    print("\nVetor inteiro:")
    print(vetor)

    posicoes_multiplos_de_10 = []
    for i in range(len(vetor)):
        if vetor[i] % 10 == 0:
            posicoes_multiplos_de_10.append(i)

    print("\nPosições dos valores múltiplos de 10:")
    if posicoes_multiplos_de_10:
        print(posicoes_multiplos_de_10)
    else:
        print("Nenhum valor múltiplo de 10 foi digitado.")

if __name__ == "__main__":
    main()