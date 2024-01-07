# IsacBM - 2K23
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year

result = anoatual - ano
alistamento = anoatual - (result - 18)

if result < 18:
    s = 18 - result
    print('Você irá se alistar daqui a {} anos! :)'.format(s))
    print(f'Seu alistamento será no ano de {alistamento}')
elif result == 18:
    print('Já é a hora de você se alistar!')
else:
    s = result - 18
    print('Já passou {} anos do período de se alistar...'.format(s))
    print(f'Seu alistamento era no ano de {alistamento}')
