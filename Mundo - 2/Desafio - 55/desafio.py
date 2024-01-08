# IsacBM - 2K24
maior = 0
menor = 100000
for i in range(0, 5):
    p = float(input('Digite seu peso: '))

    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print(f'O maior peso é {maior} e o menor é {menor}!')
