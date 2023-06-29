# Crie um program que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc 
num = float(input('Digite um número decimal: '))
print(f'A porção inteira do número digitado é: {trunc(num)}')
