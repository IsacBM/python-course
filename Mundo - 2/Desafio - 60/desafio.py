# IsacBM - 2K24
num = int(input('Digite uma valor para descobrir o fatorial: '))
i = 1
fat = 0
while i < num:
    if i == 1:
        fat = num * i
    fat = fat * i
    i += 1

print(f'O fatorial de {num}! é {fat}.')
