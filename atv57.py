'''
57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. 
No final, mostre o total de salários pagos aos homens e o total pago às 
mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não 
sempre que ler os dados de um funcionário.
'''

def calcular_salarios():
    total_salarios_homens = 0
    total_salarios_mulheres = 0

    while True:
        salario = float(input("Digite o salário do funcionário: "))
        sexo = input("Digite o sexo do funcionário (M/F): ").strip().upper()

        if sexo == 'M':
            total_salarios_homens += salario
        elif sexo == 'F':
            total_salarios_mulheres += salario
        else:
            print("Sexo inválido. Por favor, insira M ou F.")

        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    print(f"Total de salários pagos aos homens: R${total_salarios_homens:.2f}")
    print(f"Total de salários pagos às mulheres: R${total_salarios_mulheres:.2f}")

calcular_salarios()
