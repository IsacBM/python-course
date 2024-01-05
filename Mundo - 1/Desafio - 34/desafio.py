# IsacBM - 2K23
n1 = float(input('Digite um número: '))

if n1 > 1250:
    valor = n1 * (10/100)
    print('Seu novo salário é {}'.format(n1 + valor))
else:
    valor = n1 * (15 / 100)
    print('Seu novo salário é {}'.format(n1 + valor))
