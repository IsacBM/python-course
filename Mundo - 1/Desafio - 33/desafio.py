# IsacBM - 2K23
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))

menor = 0
maior = 0

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
elif n1 < n2 and n1 < n2:
    menor = n1
print('O menor valor é {}'.format(menor))

if n2 < n1 and n3 < n1:
    maior = n1
elif n3 < n2 and n1 < n2:
    maior = n2
elif n1 < n3 and n2 < n3:
    maior = n3
print('O maior valor é {}'.format(maior))
