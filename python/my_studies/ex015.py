# Escreva um program que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo
# que o carro custa R$60,00 por dia e R$0,15 Km rodado

dias = int(input('Informe quantos dias o carro ficou alugado: '))
km = float(input('Informe quantos Km o carro rodou: '))
valor = (dias * 60) + (km * 0.15)
print(f'O preço pelo aluguel do carro é: {valor}')