# IsacBM - 2K24
valor = int(input('Digite o valor para conversão: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadécimal''')
op = int(input('Escolha uma opção: '))

if op == 1:
    print(f'O valor {valor} convertido para Binário é {bin(valor)[2:]}')
elif op == 2:
    print(f'O valor {valor} convertido para Octal é {oct(valor)[2:]}')
elif op == 3:
    print(f'O valor {valor} convertido para Hexadécimal é {hex(valor)[2:]}')
else:
    print('Opção Incorreta!')
