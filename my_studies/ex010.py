#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
#comprar. Considere US$1,00 = R$3,27

dinheiro = float(input('Informe quanto de dinheiro você tem na carteira: '))
dolar = dinheiro / 3.27
print(f'Com R${dinheiro}, você consegue comprar {dolar:.2f}US$')