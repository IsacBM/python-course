# IsacBM - 2K23
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 and r1 == r3:
        print('Formam um triângulo Equilátero!')
    elif r1 != r2 and r2 == r3 or r2 != r1 and r1 == r3 or r3 != r2 and r2 == r1:
        print('Formam um triângulo Isósceles!')
    else:
      print('Formam um triângulo Escaleno!')
else:
    print('Não formam um triângulo!')
