# IsacBM - 2K24
p1 = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))
d = p1 + (10 - 1) * r

for c in range(p1, d, r):
    print(f'{c}', end=' -> ')
print('FIM')
