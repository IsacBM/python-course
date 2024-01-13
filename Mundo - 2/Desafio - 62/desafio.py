# IsacBM - 2K24
p1 = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))
termo = p1
tempo = 11
cont = 1

while cont <= tempo:
    print(f'{termo} ->', end='')
    termo += r
    cont += 1
    
    if cont == tempo:
        maistemp = str(input('Você quer mostrar mais termos? [S/N] ')).upper()
        
        if maistemp == 'S':
            novotemp = int(input('Mais quantos termos: '))
            tempo = tempo + novotemp
        elif maistemp == 'N':
            print('Até a próxima!')
            break
        else:
            break
print('Fim...')
