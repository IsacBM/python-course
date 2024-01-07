# IsacBM - 2K23
peso = float(input('Digite seu Peso (Kg): '))
alt = float(input('Digite sua Altura (m): '))

imc = peso / (alt * alt)

if imc < 18.5:
    print(f'Seu IMC é de {round(imc)}! Você está Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é de {round(imc, 1)}! Você está com o Peso Ideal')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é de {round(imc)}! Você está com Sobrepeso')
elif imc > 30 and imc <=40:
    print(f'Seu IMC é de {round(imc)}! Você está com Obesidade')
else:
    print(f'Seu IMC é de {round(imc)}! Você está com Obesidade Mórbida')