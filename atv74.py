'''
74) Crie um programa que preencha automaticamente (usando lógica, não apenas 
atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:

5 3 5 3 5 3 5 3 5 3
0 1 2 3 4 5 6 7 8 9
'''

def main():

    vetor_alternado = []
    vetor_sequencial = []

    for i in range(10):
        if i % 2 == 0:
            vetor_alternado.append(5)
        else:
            vetor_alternado.append(3)

    for i in range(10):
        vetor_sequencial.append(i)

    print("Vetor alternado 5 e 3:")
    print(" ".join(map(str, vetor_alternado)))
    
    print("\nVetor sequencial de 0 a 9:")
    print(" ".join(map(str, vetor_sequencial)))

if __name__ == "__main__":
    main()
