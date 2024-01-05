# IsacBM - 2K23
import random
num = str(input('Escolha um número entre 0 e 7: ')).strip()
computador = (random.randint(0, 5))
num2 = str(computador)
if num == num2:
    print('Parabéns, você acertou!!! :)')
else:
    print('Ops, chute errado. Era o número {} :('.format(computador))
