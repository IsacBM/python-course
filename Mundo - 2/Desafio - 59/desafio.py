# IsacBM - 2K24
import time
num = '10'

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo valor: '))

while num != '0':
    print('''
    |======| Menu |======|
    |[1] - Somar         |
    |[2] - Multiplicar   |
    |[3] - Maior         |
    |[4] - Novos Números |
    |[0] - Sair          |
    |====================|''')
    num = str(input('Escolha uma opção: ')).strip()
    if num == '0':
        print('===============================')
        print('Saindo', end=(''))
        for i in range(1, 7):
            time.sleep(0.5)
            print(end=('.'))
        print(' | Até a próxima!!!')
        print('===============================')
        num = '0'

    elif num == '1':
        print('Calculando', end=(''))
        for i in range(1, 7):
            time.sleep(0.5)
            print(end=('.'))
        soma = valor1 + valor2
        print(f'\nA soma entre os dois valores é {soma}. :)')
        esp = input('Aperte \"ENTER\"')

    elif num == '2':
        print('Calculando', end=(''))
        for i in range(1, 7):
            time.sleep(0.5)
            print(end=('.'))
        multi = valor1 * valor2
        print(f'\nA Multiplicação entre os dois valores é {multi}. :)')
        esp = input('Aperte \"ENTER\"')

    elif num == '3':
        print('Calculando', end=(''))
        for i in range(1, 7):
            time.sleep(0.5)
            print(end=('.'))
        maior = 0

        if valor1 > valor2:
            maior = valor1
            print(f'\nO maior entre os dois valores é {maior}. :)')
        elif valor2 > valor1:
            maior = valor2
            print(f'\nO maior entre os dois valores é {maior}. :)')
        esp = input('Aperte \"ENTER\"')

    elif num == '4':
        print('-==| Digite os novos valores |==-')
        valor1 = int(input(' Digite o novo número: '))
        valor2 = int(input(' Digite o novo número: '))
    esp = input('Aperte \"ENTER\"')
