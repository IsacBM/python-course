# IsacBM - 2K24
frase = str(input('Digite uma frase:'))

nova = frase.replace(' ', '').upper()
invert = nova.upper()[::-1]

if nova == invert:
    print(f'A frase "{frase}", é um Palíndromo!')
else:
    print('Essa frase não é um palíndromo. :(')
