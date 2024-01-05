# IsacBM - 2K23
name = str(input('Digite seu nome completo: ')).strip()
print(name.upper())
print(name.lower())
print('Seu nome completo tem {} Letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} Letras'.format(name.find(' ')))
