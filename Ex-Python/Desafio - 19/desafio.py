# IsacBM - 2K23
import random
aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(lista)

print('O Aluno(a) escolhido foi: {}'.format(sorteio))
