# IsacBM -|- 2K24
print('========| Cadastro |========')
cont_idade = 0
hm = 0
cont_mr = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).upper()
    
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        hm = hm + 1
    if sexo == 'F' and idade < 20:
        cont_mr += 1
        
    cont = str(input('Quer continuar? [S/N] ')).upper()
    
    if cont == 'N':
        print('======================================')
        print(f'Teve {cont_idade} com mais de 18 anos.')
        print(f'Teve {hm} Homens cadastrados.')
        print(f'Teve {cont_mr} Mulheres com menos de 20 anos.')
        print('======================================')
        break
