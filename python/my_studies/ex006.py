#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = float(input('Digite um número: '))
print(f'O dobro do valor digitado: {num * 2}')
print(f'O triplo do valor digitado: {num * 3}')
print(f'A raiz quadrada do valor digitado: {pow(num,(1/2))}')