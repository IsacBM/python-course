# IsacBM - 2K24
s = 0
for c in range(0, 6):
    valor = int(input('Digite um valor: '))
    par = valor % 2

    if par == 0:
        s = s + valor

if s == 0:
    print('Os valores não são números pares!')
else:
    print(f'A soma entre os valores pares é {s}')
