# IsacBM - 2K24
nao = 'i'
maior = 0
menor = 999999
soma = 0
aux = 0
while nao != 'N':
    num = int(input('Digite um valor: '))
    cont = str(input('Quer continuar? [S/N]')).upper()
    
    aux += 1
    soma = soma + num
    media = soma / aux
    
    if cont == 'N':
        print(f'O maior valor foi {maior}, o menor foi {menor}, a média entre eles foi {media}')
        break
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
