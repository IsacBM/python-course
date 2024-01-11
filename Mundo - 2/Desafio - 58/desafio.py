# IsacBM - 2K24
import random
num = 200
computador = random.randint(0, 10)
cont = 0

print('-==| Jogo de advinhar |==-')

while computador != num:
    num = int(input('Chute um número de 0 a 10: '))

    if num == computador:
        cont += 1
        print('=========================')
        print(f'Você chutou {cont} e venceu o jogo!!')
        print('=========================')
    else:
        cont += 1
        print('Tente novamnete!!')
