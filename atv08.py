'''
8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
Ex: 
Digite uma distância em metros: 185.72
A distância de 185.72m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''

dist = float(input('Digite uma distância em metros: '))

km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print(f'A distância de {dist}m corresponde a:')
print(f'{km}Km\n{hm}Hm\n{dam}Dam\n{dm}dm\n{cm}cm\n{mm}mm')