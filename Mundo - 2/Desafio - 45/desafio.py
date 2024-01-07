# IsacBM - 2K23
import random
valor = str(input('Escolha entre: \n0- Pedra \n1- Papel \n2- Tesoura \nDigite o valor: ')).strip()
print('-=' * 10)
lista = ('Pedra', 'Papel', 'Tesoura')

computador = random.randint(0, 2)

if computador == 0 and valor == '1':
    print('-=' * 10)
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \n Jogador venceu!!!')
elif computador == 1 and valor == '0':
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nComputador Venceu!!')
elif computador == 2 and valor == '0':
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nJogador venceu!')
elif computador == 2 and valor == '1':
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nComputador venceu!')
elif computador == 0 and valor == '2':
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nComputador venceu!')
elif computador == 1 and valor == '2':
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nJogador venceu!')
else:
    print(f'O Computador jogou: {lista[computador]} \nO Jogador jogou: {lista[int(valor)]} \nDeu Empate!')
