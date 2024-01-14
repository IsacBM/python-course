tupla_num = (0, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20)
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
c = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    aux = tupla_num.count(num)
    
    if aux == 1:
        aux2 = tupla[num]
        print(f'Você digitou o número {aux2}')
        break
    else:
        print('Tente novamente!')