#Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de desconto
salario = float(input('Informe o salário: '))
aumento = 0.15
novosalario = salario + (salario * aumento)
print(f'O salario com o aumento ficará no valor de {novosalario:.2f}')