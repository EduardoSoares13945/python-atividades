'''
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Dica: ("Altura (m²): ")
      leia (Alt)
      escreva ("Comprimentos (m²): ")
      Leia (Comp)
      Area <- Alt * Comp
      Tinta <- Area / 2
'''

Alt = float(input('Altura (m): '))
Larg = float(input('Largura (m): '))

Area = Alt * Larg
Tinta = Area / 2

print(f'A área da parede é de {Area:.2f}m²')
print(f'A quantidade de tinta necessária é de {Tinta:.2f} litros de tinta')

