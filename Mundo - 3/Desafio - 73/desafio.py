tupla = ('Vasco', 'Botafogo', 'Palmeiras', 'Cruzeiro', 'Athletico', 'Flamengo', 'Fluminence', 'Santos', 'Bragantino', 'Internacional', 'Fortaleza', 'Bahia', 'Esporte FC', 'São Paulo', 'Corinthians', 'Coritiba', 'Grêmio', 'América-MG', 'Goiás', 'Cuiabá', 'Athletico-PR')
while True:
    print('Os primeiros 5 colocados são:', end=' ')
    for i in range(0, 5):
        print(f'{tupla[i]}', end=', ')

    print(f'\nOs ultimos 4 colocados são: {tupla[-1:-5:-1]}')
    
    print(f'Em ordem alfabetica: {sorted(tupla)}')
    
    print(f'O Vasco está na {tupla.index('Vasco')+1}ª Posição.')
        
    break
