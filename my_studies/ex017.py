# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

from math import hypot
catop = float(input('Informe o valor do cateto oposto: '))
catadj = float(input('Informe o valor do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {hypot(catop,catadj):.2f}')
