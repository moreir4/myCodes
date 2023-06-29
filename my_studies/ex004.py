#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as 
#informações possiveis sobre ele

entrada = input('Digite algo: ')
print('O que foi digitado é do tipo: ',type(entrada))
print('É numerico? ', entrada.isnumeric())
print('É somente espaços?', entrada.isspace())
print('É alfabético?', entrada.isalpha())
print('É alfanumérico?', entrada.isalnum())
print('É decimal?', entrada.isdecimal())