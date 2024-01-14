# IsacBM -|- 2K24
import random
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    op = str(input('Par ou Impar: [P/I] ')).upper().strip()
    
    computador = random.randint(1, 10)
    
    soma = valor + computador
    
    parouimpar = soma % 2
    
    if op == 'P':
        if parouimpar == 0:
            cont += 1
            print(f'Você venceu {cont} vezes!')
        else:
            print(f'Você jogou {valor} e o computador jogou {computador}')
            print('Você perdeu!')
            break
    elif op == 'I':
        if parouimpar != 0:
            cont += 1
            print(f'Você venceu {cont} vezes!')
        else:
            print(f'Você jogou {valor} e o computador jogou {computador}')
            print('Você perdeu!')
            break
        
print(f'Você venceu {cont} vezes!')
