# IsacBM - 2K24
maisvelho = ''
cont = 0
s = 0
idadev = 0
for i in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: (F) ou (M) ')).upper()
    s = s + idade

    if idade > idadev and sexo == 'M':
        idadev = idade
        maisvelho = nome
    if sexo == 'F':
        if idade < 20:
            cont += 1

media = s / 4
print(f'A média de idades é {media}, o homem mais velho é {maisvelho} e tem {cont} mulheres com menos de 20 anos!')
