# IsacBM - 2K23
v = int(input('Digite a velocidade do veículo: '))
multa = (v - 80) * 7
if v > 80:
    print('Você estava acima da velocidade! O valor da multa será de R${} reais.'.format(multa))
else:
    print('Tudo certo durante o trajeto! :)')