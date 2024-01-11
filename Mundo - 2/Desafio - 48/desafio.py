# IsacBM - 2K24
s = 0
for cont in range(1, 501):
    impar = cont % 2
    if impar == 1:
        multi = cont % 3
        if multi == 0:
            s = s + cont
print(f'A soma final é {s}')
