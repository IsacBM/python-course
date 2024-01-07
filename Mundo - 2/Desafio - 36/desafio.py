# IsacBM - 2K24
casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Quantos anos: '))

prestacao = casa / (anos * 12)

sala = salario * 30/100

if prestacao > sala:
    print(f'A prestação seriá de {round(prestacao, 2)}! Você infelizmente não pode financiar por não conseguir o empréstimo. :(')
else:
    print('O valor da prestação será de {:.2f} por mês. :)'.format(prestacao))
