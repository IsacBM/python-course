# IsacBM - 2K23
frase = str(input('Digite seu nome completo: ')).strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A letra "A" aparece na posição {}'.format(frase.upper().find('A') + 1))
print('A última letra "A" aparece na posição {}'.format(frase.upper().rfind('A') + 1))

