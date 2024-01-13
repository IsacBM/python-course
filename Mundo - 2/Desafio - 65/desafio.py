# IsacBM - 2K24
nao = 'r'
aux = 0
soma = 0
media = 0
maior = 0
menor = 999999
while nao != 'N':
    num = int(input('Digite um valor:'))
    cont = str(input('Desaja continuar? [S/N]')).upper()
    aux +=1
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if cont == 'N':
        media = soma / aux
        print(f'A média entre os valor é {round(media, 2)}, o maior valor é {maior} e o menor é {menor}.')
        break