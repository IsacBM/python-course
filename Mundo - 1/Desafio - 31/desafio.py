# IsacBM - 2K23
dis = int(input('Digite a distância: '))
if dis <= 200:
    valor = dis * 0.50
    print('O preço da passagem é {:.2f}'.format(valor))
else:
    valor = dis * 0.45
    print('O preço da passagem é {:.2f}'.format(valor))
