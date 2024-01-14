# IsacBM -|- 2K24
# 50 - 20 - 10 - 1
print('='*34)
print('            Banco Zack')
print('='*34)

valor_saque = int(input('Qual será o valor do saque? R$'))
aux = 0

cont_cinq = 0
cont_vinte = 0
cont_dez = 0
cont_um = 0

while True:
    if (aux + 50) <= valor_saque:
        aux += 50
        cont_cinq += 1
    elif (aux + 20) <= valor_saque:
        aux += 20
        cont_vinte += 1
    elif (aux + 10) <= valor_saque:
        aux += 10
        cont_dez += 1
    elif (aux + 1) <= valor_saque:
        aux += 1
        cont_um += 1
        
    if aux == valor_saque:
        print('='*34)
        print(f'Total de {cont_cinq} notas de R$50 Reais.')
        print(f'Total de {cont_vinte} notas de R$20 Reais.')
        print(f'Total de {cont_dez} notas de R$10 Reais.')
        print(f'Total de {cont_um} notas de R$1 Real.')
        print('='*34)
        print('Volte sempre! Tenha um exelente dia!!!')
        print('='*34)
        break
