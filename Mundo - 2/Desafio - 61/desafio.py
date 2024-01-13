# IsacBM - 2K24
p1 = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))
termo = p1
cont = 1

while cont <= 10:
    print(f'{termo} ->', end='')
    termo += r
    cont += 1
print('Fim...')
