# IsacBM - 2K24
maior = 0
menor = 100000
for i in range(1, 6):
    p = float(input(f'Digite o peso da {i}ª pessoa: '))
    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print(f'O maior peso é {maior}KG e o menor é {menor}KG!')
