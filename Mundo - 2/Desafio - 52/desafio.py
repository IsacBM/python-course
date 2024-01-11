# IsacBM - 2K24
num = int(input('Digite um valor: '))
cont = 0
for c in range(1, num+1):
    if (num % c) == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')

    print(f'{c}', end=' ')
if cont == 2:
    print('\n\033[mO número é primo!')
else:
    print('\n\033[mO valor não é primo.')