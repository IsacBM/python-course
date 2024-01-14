# IsacBM -|- 2K24
while True:
    num = int(input('Digite um valor para saber a Tabuada: '))
    
    if num < 0:
        print('Finalizando...')
        break
    else:
        print('=' * 12)
        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')
        print('=' * 12)
