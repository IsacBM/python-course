# IsacBM - 2K24
num = 0
soma = 0
while num != 999:
    n = int(input('Digite um valor: [999 para a aplicação]'))
    if n == 999:
        num = 999
        print(f'A soma entre eles foi {soma}')
    soma = soma + n
    