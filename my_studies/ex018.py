# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo

from math import cos, sin, tan, radians
angulo = float(input("Informe um angulo: "))
angulorad = radians(angulo) 
print(f'Seno: {sin(angulorad):.2f}')
print(f'Cosseno: {cos(angulorad):.2f}')
print(f'Tangente: {tan(angulorad):.2f}')