#Faça um programa que leia a largura e a alutra de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
tinta = 2
area = altura * largura
ltstinta = area / tinta
print(f'Serão necessários {ltstinta:.2f}L de tinta para pintar a parede de {area:.2f}m².')
