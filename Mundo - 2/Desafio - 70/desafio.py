# IsacBM -|- 2K24
total = 0
cont_preco = 0
mais_barato = ''
menor_preco = 99999
while True:
    nome = str(input('Digite o nome do produto: '))
    preco =  float(input('Digite o preço: '))
    
    total = total + preco
    
    if preco > 1000:
        cont_preco += 1
        
    if preco < menor_preco:
        menor_preco = preco
        mais_barato = nome
    
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    
    if cont == 'N':
        break
    
print(f'O total foi de {total}, {cont_preco} produtos passaram de mil reais e o produto mais parato foi o/a {mais_barato}')
