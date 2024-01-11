# IsacBM - 2K24
s = 0
for c in range(1, 7):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        s = s + valor
if s == 0:
    print('Os valores não são números pares!')
else:
    print(f'A soma entre os valores pares é {s}')
