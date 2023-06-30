# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

aluno1 = str(input('Informe o primeiro aluno: '))
aluno2 = str(input('Informe o segundo aluno: '))
aluno3 = str(input('Informe o terceiro aluno: '))
aluno4 = str(input('Informe o quarto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print(f'A ordem para apresentar o trabalho é a seguinte: {lista}')