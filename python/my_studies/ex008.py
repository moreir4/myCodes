#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

mts = float(input('Informe um valor em metros: '))
print(f'{mts}m em milímetros: {mts * 1000}mm')
print(f'{mts}m em centimetros: {mts * 100}cm')