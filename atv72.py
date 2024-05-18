'''
72) Crie um programa que preencha automaticamente (usando lógica, não apenas 
atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:

5 10 15 20 25 30 35 40 45 50
0 1 2 3 4 5 6 7 8 9
'''

def main():
   
    vetor_multiplo_5 = []
    vetor_sequencial = []


    for i in range(1, 11):
        vetor_multiplo_5.append(i * 5)

   
    for i in range(10):
        vetor_sequencial.append(i)

  
    print("Vetor com múltiplos de 5:")
    print(" ".join(map(str, vetor_multiplo_5)))
    
    print("\nVetor sequencial de 0 a 9:")
    print(" ".join(map(str, vetor_sequencial)))

if __name__ == "__main__":
    main()
