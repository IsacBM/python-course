# IsacBM - 2K24
num = int(input('Digite um valor: '))

for c in range(1, num+1):
    if (num % c) != 0:
        print('É primo')
