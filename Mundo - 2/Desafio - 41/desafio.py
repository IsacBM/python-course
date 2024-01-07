# IsacBM - 2K23
import datetime
data = int(input('Digite o ano de nascimento: '))

anos = datetime.date.today().year - data

if anos <= 9:
    print('Você está na categoria Mirim!')
elif anos > 9 and anos <=14:
    print('Você está na categoria Infantil!')
elif anos > 14 and anos <= 19:
    print('Você está na categoria Junior!')
elif anos == 20:
    print('Você está na categoria Sênior!')
else:
    print('Você está na categoria Master!')
