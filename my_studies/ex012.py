#Faça um algorítimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
preco = float(input('Informe o preço do produto: '))
desconto = 0.05
valordesconto = preco * desconto
valorfinal = preco - valordesconto
print(f'O valor do produto com o desconto aplicado é: {valorfinal:.2f}')