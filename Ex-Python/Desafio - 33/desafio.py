# IsacBM - 2K23
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 & n2 > n3:
    print('O maior número é {}'.format(n1))
elif n1 < n2 & n2 > n3:
    print('O maior número é {}'.format(n2))
else:
    print('O maior número é {}'.format(n3))
