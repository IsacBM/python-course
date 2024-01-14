# IsacBM -|- 2K24
cont = 0
soma = 0
while True:
    num = int(input('Digite um valor: [999 para parar] '))
    if num == 999:
        print(f'A quantidade de números foi {cont} e a soma entre eles é {soma}')
        break
    else:
        cont += 1
        soma = soma + num
