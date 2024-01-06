# IsacBM - 2K23
casa = float(input('Primeiro seguimento: '))
salario = float(input('Segundo seguimento: '))
anos = int(input('Terceiro seguimento: '))

prestacao = casa / (anos * 12)

sala = salario * 30/100

if prestacao > sala:
    print('Você infelizmente não pode financiar. :(')
else:
    print('O valor da prestação será de {:.2f} por mês. :)'.format(prestacao))
