# IsacBM - 2K23
peso = float(input('Digite seu Peso: '))
alt = float(input('Digite sua Altura: '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <=40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')