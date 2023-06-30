# Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
# lendo o nome dels e escrevendo o nome do escolhido

from random import choice

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segudno aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
print(f'O aluno escolhido para apagar o quadro foi o(a) {choice(lista)}')