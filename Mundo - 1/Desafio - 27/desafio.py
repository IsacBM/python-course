# IsacBM - 2K23
name = str(input('Digite seu nome completo: ')).strip()

result = name.split()

print('Seu primeiro nome é: {}'.format(result[0]))
print('Seu último nome é: {}'.format(result[len(result) - 1]))
