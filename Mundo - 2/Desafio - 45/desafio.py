# IsacBM - 2K23
import random
valor = str(input('Escolha entre: \n1- Pedra \n2- Papel \n3- Tesoura \nDigite o valor: ')).strip()

# PEDRA 1
# PAPEL 2
# TESOURA 3

computador = random.randint(1, 3)

if computador == 1 and valor == '2':
    print('Jogador venceu!!!')
elif computador == 2 and valor == '1':
    print('Computador Venceu!!')
elif computador == 3 and valor == '1':
    print('Jogador venceu!')
elif computador == 3 and valor == '2':
    print('Computador venceu!')
elif computador == 1 and valor == '3':
    print('Computador venceu!')
elif computador == 2 and valor == '3':
    print('Jogador venceu!')
else:
    print('Deu Empate!')
