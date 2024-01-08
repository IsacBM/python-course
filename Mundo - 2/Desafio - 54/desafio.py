# IsacBM - 2K24
import datetime
cont1 = 0
cont2 = 0
for i in range(0, 7):
    data = int(input('Digite seu ano de nascimento: '))
    idade = datetime.date.today().year - data

    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print(f'Tem {cont1} pessoas possuem a maioridade, e {cont2} pessoas que ainda não antigiram.')
